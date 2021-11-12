
"""
Acquire an XPCS measurement with a supported area detector
"""

# __all__ = [
#     'select_sample',
#     'te_qnw',
# ]

from instrument.session_logs import logger
logger.info(__file__)

from ..devices import aps, detu, I0Mon, soft_glue
from ..devices import Atten1, Atten2, scaler1
from ..devices import timebase, pind1, pind2, T_A, T_SET
from ..devices import rigaku500k
from ..framework import db, RE
from bluesky import plan_stubs as bps
from bluesky import preprocessors as bpp
import apstools.utils
import datetime
import ophyd.signal
from ophyd import Device, Signal, Component
import os



class Info_User(Device): 
    det_directory = Component(Signal, value=None)
    scan_directory = Component(Signal, value=None)

    def select_path(self, user_index):
        yield from bps.mv(self.det_directory, f'/home/8idiuser/{aps.aps_cycle.get()}/{user_index}')
        yield from bps.mv(self.scan_directory, f'/home/beams10/8IDIUSER/bluesky_data/{aps.aps_cycle.get()}')

class Info_Detector(Device): 

    # def __init__(self):
    #     self.detector_name = None
    #     self.qmapname = None
    #     self.filename = None
    #     self.trigger_mode = None
    #     self.acquisition_mode = None
    #     self.acquisition_time = None
    #     self.acquisition_period = None

    detector_name = Component(Signal, value=None)
    filename = Component(Signal, value=None)
    trigger_mode = Component(Signal, value=None)
    acquisition_mode = Component(Signal, value=None)

    qmapname = Component(Signal, value=None)
    acquisition_time = Component(Signal, value=None)
    acquisition_period = Component(Signal, value=None)

    def select_qmap(self, qmap_name: str):
        """
        set qmap
        """
        yield from bps.mv(self.qmapname, f'/home/8-id-i/{aps.aps_cycle.get()}/{qmap_name}')
        # self.qmapname.put(f'/home/8-id-i/{aps.aps_cycle.get()}/{qmap_name}')

    def select_det_mode(self, detector_name, trigger_mode, acquisition_mode):
        yield from bps.mv(self.detector_name, detector_name)
        yield from bps.mv(self.trigger_mode, trigger_mode)
        yield from bps.mv(self.acquisition_mode, acquisition_mode)
        
        if detector_name == 'rigaku500k' and trigger_mode == 0 and acquisition_mode == 'fast':
            self.stage_sigs = {}
            self.stage_sigs["cam.acquire"] = 0
            self.stage_sigs["cam.acquire_time"] = 20e-6
            self.stage_sigs["cam.image_mode"] = "2 Bit, Zero-Deadtime"
            self.stage_sigs["cam.trigger_mode"] = "ZDT Fixed Time"
            self.stage_sigs["cam.num_images"] = 100_000  # "_" is a visual separator
            self.stage_sigs["cam.corrections"] = "Enabled"
            self.stage_sigs["cam.data_type"] = "UInt32"

            rigaku500k.cam.acquire_time.put(30e-6)


class Run_Object(Device):
    info_user = Component(Info_User)
    info_detector = Component(Info_Detector)



# class Info_Sample: 
#     def __init__(self):
#         self.sample_name = None
#         self.id_char = None
#         self.samx_center = None
#         self.samx_scan_halfwidth = None
#         self.samx_num_points = None
#         self.samz_center = None
#         self.samz_scan_halfwidth = None
#         self.samz_num_points = None
#         self.qnw_position = None
#         self.qnw_name = None
        
#     def select(self, sample_index):
        # """Load sample information from json file"""
        # # read the json file
        # # find the sample_index
        # config = json_dict[sample_index]
        # self.sample_name = ["sample_name"]
        # self.id_char = ["samp_id_char"]

    