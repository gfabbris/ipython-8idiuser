"""
Rigaku Ultra-Fast X-ray Camera area detector (LabView, not EPICS)

* detector name: RIGAKU500K_NoGap
* detector number: 46

Mimics an ophyd.areaDetector object without subclassing it.
"""

__all__ = [
    "rigaku",
]

from instrument.session_logs import logger

logger.info(__file__)

from .ad_acquire_detector_base import AD_AcquireDetectorBase
from .ad_acquire_detector_base import AD_AcquireDetectorCamBase
from .data_management import DM_DeviceMixinAreaDetector, dm_pars
from .shutters import shutter_control, shutter_override, shutteroff
from bluesky import plan_stubs as bps
from ophyd import Component, Device, DeviceStatus
from ophyd import Signal, EpicsSignal, EpicsSignalRO
import apstools.utils
import itertools
import os
import psutil
import subprocess
import time
import uuid


def get_process_info(pid):
    process_info = psutil.Process(pid)
    logger.info("process_info status: %s", process_info.status())
    return process_info


class UnixCommandSignal(Signal):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.unix_command = None
        self.unix_output = None
        self.unix_error = None
        self.process = None

    def set(self, unix_command):
        status = DeviceStatus(self)
        self.unix_command = unix_command

        # see: https://github.com/aps-8id-dys/ipython-8idiuser/issues/195

        self.process = subprocess.Popen(
            unix_command,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        pi = get_process_info(self.process.pid)
        logger.info(
            "command: %s - process info: pid=%s, info=%s",
            unix_command,
            self.process.pid,
            pi,
        )

        @apstools.utils.run_in_thread
        def watch_process():
            self.unix_output, self.unix_error = self.process.communicate()
            self.process = None
            status._finished()

        watch_process()
        return status

    def put(self, unix_command):
        status = self.set(unix_command)
        while not status.done:
            time.sleep(0.001)

    def get(self):
        return self.unix_output.decode(), self.unix_error.decode()


class ShutterModeSignal(EpicsSignal):
    """Enhanced EpicsSignal"""

    ALIGN_MODE = "1UFXC"
    DATA_MODE = "UFXC"

    def align_mode(self):
        """Blocking method, not a bluesky plan, continuous imaging"""
        self.put(self.ALIGN_MODE)
        shutteroff()
        logger.info(
            "Shutter will remain OPEN for alignment" " if **showbeam** is called."
        )

    def data_mode(self):
        """Blocking method, not a bluesky plan, triggered imaging"""
        self.put(self.DATA_MODE)
        shutteroff()
        logger.info(
            "Shutter will be controlled by UFXC"
            " if shutter is left in the **showbeam** state."
        )


class RigakuFakeCam(AD_AcquireDetectorCamBase, Device):
    """
    mimic ophyd support for Cam Plugin
    """

    EXT_TRIGGER = 0
    array_size_x = Component(Signal, value=1024.0)  # FIXME:  1024x512 ?or? 512x1024
    array_size_y = Component(Signal, value=512.0)

    def setup_modes(self, num_triggers):
        """
        Rigaku detector will ignore this request
        """
        yield from bps.null()

    def setTime(self, *args):
        """
        Rigaku detector will ignore this request
        """
        yield from bps.null()


class RigakuFakeImage(Device):
    """
    mimic ophyd support for Image Plugin
    """

    shape = []

    def set(self, *args, **kwargs):
        pass  # TODO: what to do


class Rigaku_8IDI(AD_AcquireDetectorBase, DM_DeviceMixinAreaDetector, Device):
    """
    Supports non-epics communication with the new Rigaku detector

    How to use:

    1. rigaku = Rigaku_8IDI(name = 'rigaku')
    2. yield from bps.mv(rigaku.batch_name, 'A001_Test')
    3. yield from bps.count([rigaku])
    """

    qmap_file = "qzhang202002_Rq0_Log_S270_D27.h5"

    acquire_start = Component(EpicsSignal, "8idi:Unidig2Bo7.VAL")
    acquire_complete = Component(EpicsSignalRO, "8idi:Unidig2Bi2.VAL")

    shutter_mode = ShutterModeSignal(
        "8idi:softGlueC:AND-4_IN2_Signal", name="shutter_mode"
    )

    unix_process = Component(UnixCommandSignal)

    batch_name = Component(Signal, value="A001")

    detector_number = 46  # 8-ID-I numbering of this detector

    _assets_docs_cache = []
    _datum_counter = None
    _file_name = None
    _resource_uid = None

    cam = Component(RigakuFakeCam)
    image = Component(RigakuFakeImage)

    def stage(self):
        # prepare to write the document stream for Xi-CAM handling
        root = os.path.join("/", "home", "8-id-i-stage/")
        folder = self._file_name
        fname = (
            f"{folder}"
            f"_{dm_pars.data_begin.get():05.0f}"
            f"-{dm_pars.data_end.get():05.0f}"
            ".bin"
        )
        self._resource_uid = str(uuid.uuid4())

        resource_doc = {
            "uid": self._resource_uid,
            "spec": "RIGAKU",  # FIXME: What format for Rigaku?
            "resource_path": os.path.join(folder, fname),
            "root": root,
            "resource_kwargs": {"frames_per_point": self.get_frames_per_point(),},
            "path_semantics": "posix",
            # can't add new stuff, such as: 'full_name': full_name,
        }
        self._datum_counter = itertools.count()
        self.image.shape = [
            self.get_frames_per_point(),
            self.cam.array_size_y.get(),
            self.cam.array_size_x.get(),
        ]
        self._assets_docs_cache.append(("resource", resource_doc))

        self.shutter_mode.data_mode()  # also calls shutteroff()
        # shutter_control.put() is required for data mode
        # For legacy reasons, it is here and not in data_mode().
        shutter_control.put("Open")
        cmd = f"echo FILE:F:{self.batch_name.get()} | nc rigaku1.xray.aps.anl.gov 10000"
        self.unix_process.put(cmd)

    def trigger(self):
        # Tell Rigaku to stop acquisition and wait until it's ready
        # self.acquire_start.put(0)
        while self.acquire_complete.get() in (1, "High"):
            time.sleep(0.1)

        # Getting ready to watch acquisition complete
        status = DeviceStatus(self)

        def watch_acquire(value, old_value, **kwargs):
            if value == 1 and old_value == 0:
                # self.acquire_start.put(0)
                self.acquire_complete.clear_sub(watch_acquire)
                status._finished()

        # Start acquisition
        self.acquire_complete.subscribe(watch_acquire)
        time.sleep(0.1)  # QZ 06/28/20: No reason. Put it there to improve stability
        # self.acquire_start.put(1)
        self.unix_process.put("echo EXPOSURE | nc rigaku1.xray.aps.anl.gov 10000")
        time.sleep(0.1)  # could be shorter, this works now
        # self.acquire_start.put(0)  # Stop acquisition

        # write the document stream for Xi-CAM handling
        index = next(self._datum_counter)
        datum_id = f"{self._resource_uid}/{index}"
        datum_doc = {
            "resource": self._resource_uid,
            "datum_id": datum_id,
            "datum_kwargs": {"index": index},
        }
        self.image.set(datum_id)
        self._assets_docs_cache.append(("datum", datum_doc))

        return status

    def collect_asset_docs(self):
        cache = self._assets_docs_cache.copy()
        yield from cache
        self._assets_docs_cache.clear()

    def get_frames_per_point(self):
        return self.images_received

    @property
    def plugin_file_name(self):
        """
        return the file name the plugin wrote

        from DM_DeviceMixinAreaDetector
        """
        return f"{self.batch_name.get()}.bin"

    @property
    def images_received(self):
        """Rigaku tells us not to change this.  100k images every time."""
        return 100000

    def staging_setup_DM(self, *args, **kwargs):
        """
        setup the detector's stage_sigs for acquisition with the DM workflow

        from DM_DeviceMixinAreaDetector
        """
        if len(args) != 5:
            raise IndexError(
                f"expected 5 parameters, received {len(args)}: args={args}"
            )
        # file_path = args[0]
        self._file_name = args[1]
        # num_images = args[2]
        # acquire_time = args[3]
        # acquire_period = args[4]

        self.batch_name.put(self._file_name)


try:
    rigaku = Rigaku_8IDI(name="rigaku", labels=["rigaku",])
except TimeoutError:
    logger.warning("Could not connect Rigaku detector")
    rigaku = None
