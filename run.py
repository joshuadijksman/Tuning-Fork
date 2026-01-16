import sys

sys.path.append("../tuning-fork")

from PySide6 import QtWidgets

from threading import Thread
from time import sleep

from serial import SerialException

from main_ui import Ui_MainWindow

from rigol_dg1022 import RigolDG
from LockIn_Amplifier import SR830
from Height_Gauge import mitutoyo
from measurements import frequencyDependence


class ObjectsGroup:
    def __init__(self) -> None:
        pass

    def add_atribute(self, name: str, value):
        self.__setattr__(name, value)


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Lock-In Amplifier - Normal
        self.LockInNormalConnected = False
        self.ui.ConnectLockInNormal.clicked.connect(self.LockInNormalConnect)
        self.LockInNormal = SR830()

        # Lock-In Amplifier - Shear
        self.LockInShearConnected = False
        self.ui.ConnectLockInShear.clicked.connect(self.LockInShearConnect)
        self.LockInShear = SR830()

        # Frequency Generator
        self.FreqGenConnected = False
        self.ui.ConnectFreqGen.clicked.connect(self.FreqGenConnect)
        self.FreqGen: RigolDG

        # Height Gauge
        self.HeightGaugeConnected = False
        self.ui.ConnectHeightGauge.clicked.connect(self.HeightGaugeConnect)

        # Z-Stage Controller
        self.ZStageConnected = False
        self.ui.ConnectZStage.clicked.connect(self.ZStageConnect)

        self.TimeConstNormal = self.TimeConstantLockInNormal(self.ui)
        self.SensNormal = self.SensitivityLockInNormal(self.ui)
        self.TimeConstShear = self.TimeConstantLockInShear(self.ui)
        self.SensNormal = self.SensitivityLockInShear(self.ui)

    def LockInNormalConnect(self) -> None:
        def Connect(SN):
            try:
                self.LockInShear.connect(SN=SN)
            except Exception as e:
                self.ui.ConnectLockInNormal.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectLockInNormal.setText("Connect")

            self.ui.ConnectLockInNormal.setEnabled(True)

        self.ui.ConnectLockInNormal.setText("Connecting...")
        self.ui.ConnectLockInNormal.setEnabled(False)
        SN = self.ui.SNLockInNormal.text()
        Thread(
            target=Connect, name="Connecting Lock-In Amplifier Normal", args=[SN]
        ).start()

    def LockInShearConnect(self) -> None:
        SN = self.ui.SNLockInShear.text()
        try:
            self.LockInShear.connect(SN=SN)
        except:
            ...

    def FreqGenConnect(self) -> None:
        visa = self.ui.VISAFreqGen.text()
        if visa != "":
            try:
                self.FreqGen = RigolDG(resource_string=visa)
            except Exception:
                self.FreqGen = RigolDG()
        else:
            RigolDG()

    def HeightGaugeConnect(self) -> None:
        pass

    def ZStageConnect(self) -> None:
        pass

    class TimeConstantLockInNormal:
        def __init__(self, ui: Ui_MainWindow) -> None:
            self.slider = ui.TimeNormalSlider
            self.widget = ui.TimeConstantNormal

            self.Time1 = ui.TimeNormal1
            self.Time2 = ui.TimeNormal2
            self.Timex1 = ui.TimeNormalx1
            self.Timex10 = ui.TimeNormalx10
            self.Timex100 = ui.TimeNormalx100
            self.Timemicros = ui.TimeNormalmicros
            self.Timems = ui.TimeNormalms
            self.Times = ui.TimeNormals
            self.Timeks = ui.TimeNormalks

    class SensitivityLockInNormal:
        def __init__(self, ui: Ui_MainWindow) -> None:
            self.slider = ui.SensNormalSlider
            self.widget = ui.SensitivityNormal

            self.Sens1 = ui.SensNormal1
            self.Sens3 = ui.SensNormal3
            self.Sens5 = ui.SensNormal5
            self.Sensx1 = ui.SensNormalx1
            self.Sensx10 = ui.SensNormalx10
            self.Sensx100 = ui.SensNormalx100
            self.Sensmicros = ui.SensNormalnV
            self.Sensms = ui.SensNormalmicroV
            self.Senss = ui.SensNormalmV
            self.Sensks = ui.SensNormalV

    class TimeConstantLockInShear:
        def __init__(self, ui: Ui_MainWindow) -> None:
            self.slider = ui.TimeShearSlider
            self.widget = ui.TimeConstantShear

            self.Time1 = ui.TimeShear1
            self.Time2 = ui.TimeShear2
            self.Timex1 = ui.TimeShearx1
            self.Timex10 = ui.TimeShearx10
            self.Timex100 = ui.TimeShearx100
            self.Timemicros = ui.TimeShearmicros
            self.Timems = ui.TimeShearms
            self.Times = ui.TimeShears
            self.Timeks = ui.TimeShearks

    class SensitivityLockInShear:
        def __init__(self, ui: Ui_MainWindow) -> None:
            self.slider = ui.SensShearSlider
            self.widget = ui.SensitivityShear

            self.Sens1 = ui.SensShear1
            self.Sens3 = ui.SensShear3
            self.Sens5 = ui.SensShear5
            self.Sensx1 = ui.SensShearx1
            self.Sensx10 = ui.SensShearx10
            self.Sensx100 = ui.SensShearx100
            self.Sensmicros = ui.SensShearnV
            self.Sensms = ui.SensShearmicroV
            self.Senss = ui.SensShearmV
            self.Sensks = ui.SensShearV


def run():
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
