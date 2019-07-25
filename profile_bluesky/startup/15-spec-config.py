logger.info(__file__)

"""converted from SPEC config file using apstools.migration.spec2ophyd"""

flyz = EpicsMotor('8idiAERO:aero:c0:m1', name='flyz')
# line 1: MOT001 =    NONE:2/64   2000  1  2000  200   50  125    0 0x003  StrainN  StrainN
ti3y = EpicsMotor('8idi:m16', name='ti3y')
si6b = EpicsMotor('8idi:m41', name='si6b')
si6t = EpicsMotor('8idi:m42', name='si6t')
si5x = EpicsMotor('8idi:m55', name='si5x')
si5z = EpicsMotor('8idi:m56', name='si5z')
si6B = EpicsMotor('8idi:m43', name='si6B')
si6T = EpicsMotor('8idi:m44', name='si6T')
tth = EpicsMotor('8idi:sm1', name='tth')
sa1vgap = EpicsMotor('8ida:Slit1Vsize', name='sa1vgap')
sa1vcen = EpicsMotor('8ida:Slit1Vcenter', name='sa1vcen')
sa1hgap = EpicsMotor('8ida:Slit1Hsize', name='sa1hgap')
sa1hcen = EpicsMotor('8ida:Slit1Hcenter', name='sa1hcen')
ta1_x = EpicsMotor('8ida:TA1:x', name='ta1_x')
ta1_z = EpicsMotor('8ida:TA1:y', name='ta1_z')
ta2_x = EpicsMotor('8ida:TA2:x', name='ta2_x')
ta2_z = EpicsMotor('8ida:TA2:y', name='ta2_z')
ta2fine = EpicsMotor('8ida:sm9', name='ta2fine')
diamx = EpicsMotor('8idd:m1', name='diamx')
diamz = EpicsMotor('8idd:m2', name='diamz')
ti2_x = EpicsMotor('8idi:TI2:x', name='ti2_x')
ti2_z = EpicsMotor('8idi:TI2:y', name='ti2_z')
ti3_x = EpicsMotor('8idi:TI3:x', name='ti3_x')
ti3_z = EpicsMotor('8idi:TI3:y', name='ti3_z')
ti1_x = EpicsMotor('8idi:TI1:x', name='ti1_x')
ti1_z = EpicsMotor('8idi:TI1:y', name='ti1_z')
si1vgap = EpicsMotor('8idi:Slit1Vsize', name='si1vgap')
si1vcen = EpicsMotor('8idi:Slit1Vcenter', name='si1vcen')
si1hgap = EpicsMotor('8idi:Slit1Hsize', name='si1hgap')
si1hcen = EpicsMotor('8idi:Slit1Hcenter', name='si1hcen')
pind1z = EpicsMotor('8idi:m3', name='pind1z')
shuttz = EpicsMotor('8idi:m2', name='shuttz')
bewinx = EpicsMotor('8idi:m17', name='bewinx')
bewinz = EpicsMotor('8idi:m11', name='bewinz')
si1x = EpicsMotor('8idi:m18', name='si1x')
pind2z = EpicsMotor('8idi:m4', name='pind2z')
si3hgap = EpicsMotor('8idi:Slit3Hsize', name='si3hgap')
si3hcen = EpicsMotor('8idi:Slit3Hcenter', name='si3hcen')
si3vcen = EpicsMotor('8idi:Slit3Vcenter', name='si3vcen')
si3vgap = EpicsMotor('8idi:Slit3Vsize', name='si3vgap')
si4vgap = EpicsMotor('8idi:Slit4Vsize', name='si4vgap')
si4vcen = EpicsMotor('8idi:Slit4Vcenter', name='si4vcen')
si4hgap = EpicsMotor('8idi:Slit4Hsize', name='si4hgap')
si4hcen = EpicsMotor('8idi:Slit4Hcenter', name='si4hcen')
samx = EpicsMotor('8idi:m54', name='samx')
samy = EpicsMotor('8idi:m49', name='samy')
samz = EpicsMotor('8idi:m50', name='samz')
samth = EpicsMotor('8idi:m51', name='samth')
sampit = EpicsMotor('8idi:m52', name='sampit')
samchi = EpicsMotor('8idi:m53', name='samchi')
tth_act = EpicsMotor('8idi:m63', name='tth_act')
bstop = EpicsMotor('8idi:m27', name='bstop')
si2vgap = EpicsMotor('8idi:Slit2Vsize', name='si2vgap')
si2vcen = EpicsMotor('8idi:Slit2Vcenter', name='si2vcen')
si2hgap = EpicsMotor('8idi:Slit2Hsize', name='si2hgap')
si2hcen = EpicsMotor('8idi:Slit2Hcenter', name='si2hcen')
ti4_x = EpicsMotor('8idi:TI4:x', name='ti4_x')
ti4_z = EpicsMotor('8idi:TI4:y', name='ti4_z')
shuttx = EpicsMotor('8idi:m1', name='shuttx')
monoE = EpicsMotor('8idimono:sm2', name='monoE')
monoth = EpicsMotor('8idimono:sm1', name='monoth')
piezo = EpicsMotor('8idimono:m4', name='piezo')
monopic = EpicsMotor('8idimono:m1', name='monopic')
ccdz = EpicsMotor('8idi:m91', name='ccdz')
alpha = EpicsMotor('8idi:sm2', name='alpha')
ti4zu = EpicsMotor('8idi:m30', name='ti4zu')
ti4zdo = EpicsMotor('8idi:m31', name='ti4zdo')
ti4zdi = EpicsMotor('8idi:m32', name='ti4zdi')
ti4xu = EpicsMotor('8idi:m28', name='ti4xu')
ti4xd = EpicsMotor('8idi:m29', name='ti4xd')
tthAPD = EpicsMotor('8idi:sm3', name='tthAPD')
ccdx = EpicsMotor('8idi:m90', name='ccdx')
fccdx = EpicsMotor('8idi:m25', name='fccdx')
fccdz = EpicsMotor('8idi:m83', name='fccdz')
foceye = EpicsMotor('8idi:m37', name='foceye')
crlz = EpicsMotor('8idi:m62', name='crlz')
crlpit = EpicsMotor('8idi:m67', name='crlpit')
crlx = EpicsMotor('8idi:m65', name='crlx')
crlyaw = EpicsMotor('8idi:m66', name='crlyaw')
# line 80: MOT080 =    NONE:2/68   2000  1  2000  200   50  125    0 0x003     crly  crly
sa1zu = EpicsMotor('8ida:m11', name='sa1zu')
sa1xu = EpicsMotor('8ida:m14', name='sa1xu')
sa1zd = EpicsMotor('8ida:m15', name='sa1zd')
sa1xd = EpicsMotor('8ida:m16', name='sa1xd')
piezox = EpicsMotor('8idi:m69', name='piezox')
piezoz = EpicsMotor('8idi:m70', name='piezoz')
si6vgap = EpicsMotor('8idi:Slit6Vsize', name='si6vgap')
si6vcen = EpicsMotor('8idi:Slit6Vcenter', name='si6vcen')
si6hgap = EpicsMotor('8idi:Slit6Hsize', name='si6hgap')
si6hcen = EpicsMotor('8idi:Slit6Hcenter', name='si6hcen')
si5hgap = EpicsMotor('8idi:Slit5Hsize', name='si5hgap')
si5hcen = EpicsMotor('8idi:Slit5Hcenter', name='si5hcen')
si5vgap = EpicsMotor('8idi:Slit5Vsize', name='si5vgap')
si5vcen = EpicsMotor('8idi:Slit5Vcenter', name='si5vcen')
sipvgap = EpicsMotor('8idi:SlitpinkVsize', name='sipvgap')
sipvcen = EpicsMotor('8idi:SlitpinkVcenter', name='sipvcen')
siphgap = EpicsMotor('8idi:SlitpinkHsize', name='siphgap')
siphcen = EpicsMotor('8idi:SlitpinkHcenter', name='siphcen')
dsbstpx = EpicsMotor('8idisoft:m1', name='dsbstpx')
dsbstpz = EpicsMotor('8idisoft:m2', name='dsbstpz')
dsccdx = EpicsMotor('8idi:m81', name='dsccdx')
si2t = EpicsMotor('8idi:m46', name='si2t')
si2b = EpicsMotor('8idi:m45', name='si2b')
si2i = EpicsMotor('8idi:m47', name='si2i')
si2o = EpicsMotor('8idi:m48', name='si2o')
dsccdz = EpicsMotor('8idi:m68', name='dsccdz')
# Macro Motor: SpecMotor(mne='si2vg', config_line='107', name='si2vg', macro_prefix='Slit2SoftV') # read_mode=0
nano = EpicsMotor('8idimono:m5', name='nano') # read_mode=0
scaler1 = ScalerCH('8idi:scaler1', name='scaler1')
# counter: sec = SpecCounter(mne='sec', config_line='0', name='Seconds', unit='0', chan='0', pvname=8idi:scaler1.S1)
# counter: pind1 = SpecCounter(mne='pind1', config_line='1', name='pind1', unit='0', chan='1', pvname=8idi:scaler1.S2)
# counter: I0Mon = SpecCounter(mne='I0Mon', config_line='2', name='I0Mon', unit='0', chan='7', pvname=8idi:scaler1.S8)
# counter: pind2 = SpecCounter(mne='pind2', config_line='3', name='pind2', unit='0', chan='2', pvname=8idi:scaler1.S3)
# counter: pind3 = SpecCounter(mne='pind3', config_line='4', name='pind3', unit='0', chan='3', pvname=8idi:scaler1.S4)
# counter: pind4 = SpecCounter(mne='pind4', config_line='5', name='pind4', unit='0', chan='4', pvname=8idi:scaler1.S5)
# counter: pdbs = SpecCounter(mne='pdbs', config_line='6', name='pdbs', unit='0', chan='5', pvname=8idi:scaler1.S6)
# counter: I_APS = SpecCounter(mne='I_APS', config_line='7', name='I_APS', unit='0', chan='6', pvname=8idi:scaler1.S7)
# line 8: CNT008 =     NONE  2  0      1 0x000     ccdc  ccdc
Atten1 = EpicsSignal('8idi:userTran1.P', name='Atten1')
Atten2 = EpicsSignal('8idi:userTran3.P', name='Atten2')
T_A = EpicsSignal('8idi:LS336:TC4:IN1', name='T_A')
T_SET = EpicsSignal('8idi:LS336:TC4:OUT1:SP', name='T_SET')
# counter: APD = SpecCounter(mne='APD', config_line='13', name='APD', unit='0', chan='8', pvname=8idi:scaler1.S9)
