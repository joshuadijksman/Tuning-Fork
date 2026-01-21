import sys

from threading import Thread
from time import sleep

from serial import SerialException
from serial.tools import list_ports

from PySide6 import QtWidgets
from main_ui import Ui_MainWindow

from rigol_dg1022 import RigolDG
from LockIn_Amplifier import SR830
from Height_Gauge import mitutoyo
from Piezo_Controller import E625


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
        self.HeightGauge = mitutoyo()

        # Z-Stage Controller
        self.ZStageConnected = False
        self.ui.ConnectZStage.clicked.connect(self.ZStageConnect)
        self.ZStage = E625()

        self.TimeConstNormal = self.TimeConstantLockInNormal(self.ui)
        self.SensNormal = self.SensitivityLockInNormal(self.ui)
        self.TimeConstShear = self.TimeConstantLockInShear(self.ui)
        self.SensShear = self.SensitivityLockInShear(self.ui)

    def LockInNormalConnect(self) -> None:
        def Connect(SN) -> None:
            try:
                self.LockInNormal.connect(SN=SN)
            except Exception as e:
                self.ui.ConnectLockInNormal.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectLockInNormal.setText("Connect")
                self.ui.ConnectLockInNormal.setChecked(False)
            self.ui.ConnectLockInNormal.setEnabled(True)

        def Disconnect() -> None:
            self.LockInNormal.close()
            self.ui.ConnectLockInNormal.setText("Connect")

        if self.LockInNormal:
            Thread(
                target=Disconnect, name="Disconnecting Lock-In Amplifier Normal"
            ).start()
        else:
            self.ui.ConnectLockInNormal.setText("Connecting...")
            self.ui.ConnectLockInNormal.setEnabled(False)
            SN = self.ui.SNLockInNormal.text()
            Thread(
                target=Connect, name="Connecting Lock-In Amplifier Normal", args=[SN]
            ).start()

    def LockInShearConnect(self) -> None:
        def Connect(SN) -> None:
            try:
                self.LockInShear.connect(SN=SN)
            except Exception as e:
                self.ui.ConnectLockInShear.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectLockInShear.setText("Connect")
                self.ui.ConnectLockInShear.setChecked(False)
            self.ui.ConnectLockInShear.setEnabled(True)

        def Disconnect() -> None:
            self.LockInShear.close()
            self.ui.ConnectLockInShear.setText("Connect")

        if self.LockInShear:
            Thread(
                target=Disconnect, name="Disconnecting Lock-In Amplifier Shear"
            ).start()
        else:
            self.ui.ConnectLockInShear.setText("Connecting...")
            self.ui.ConnectLockInShear.setEnabled(False)
            SN = self.ui.SNLockInShear.text()
            Thread(
                target=Connect, name="Connecting Lock-In Amplifier Shear", args=[SN]
            ).start()

    def FreqGenConnect(self) -> None:
        def Connect(visa) -> None:
            try:
                if visa != "":
                    self.FreqGen = RigolDG(resource_string=visa)
                else:
                    RigolDG()
                self.ui.ConnectFreqGen.setText("Connected")
            except Exception as e:
                self.ui.ConnectFreqGen.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectFreqGen.setText("Connect")
                self.ui.ConnectFreqGen.setChecked(False)
            self.ui.ConnectFreqGen.setEnabled(True)

        def Disconnect() -> None:
            self.FreqGen.close()
            self.ui.ConnectFreqGen.setText("Connect")

        if self.FreqGenConnected:
            Thread(target=Disconnect, name="Disconnecting Frequency Generator").start()
        else:
            self.ui.ConnectFreqGen.setEnabled(False)
            visa = self.ui.VISAFreqGen.text()
            Thread(
                target=Connect, name="Connecting Frequency Generator", args=[visa]
            ).start()

    def HeightGaugeConnect(self) -> None:
        def Connect(port):
            try:
                self.HeightGauge.connect(port=port)
                self.ui.ConnectHeightGauge.setText("Connected")
            except Exception as e:
                self.ui.ConnectHeightGauge.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectHeightGauge.setText("Connect")
                self.ui.ConnectHeightGauge.setChecked(False)
            self.ui.ConnectHeightGauge.setEnabled(True)

        def Disconnect() -> None:
            self.HeightGauge.close()
            self.ui.ConnectHeightGauge.setText("Connect")

        if self.HeightGauge:
            Thread(target=Disconnect, name="Disconnecting Frequency Generator").start()
        else:
            port = self.ui.PortHeightGauge.text()
            Thread(
                target=Connect, name="Connecting Frequency Generator", args=[port]
            ).start()

    def ZStageConnect(self) -> None:
        def Connect(SN):
            try:
                self.ZStage.connect(SN=SN)
                self.ui.ConnectZStage.setText("Connected")
            except Exception as e:
                self.ui.ConnectZStage.setText("Connection failed...")
                print(e)
                sleep(5)
                self.ui.ConnectZStage.setText("Connect")
                self.ui.ConnectZStage.setChecked(False)
            self.ui.ConnectZStage.setEnabled(True)

        def Disconnect() -> None:
            self.ZStage.close()
            self.ui.ConnectZStage.setText("Connect")

        if self.ZStage:
            Thread(target=Disconnect, name="Disconnecting Z-Stage").start()
        else:
            port = self.ui.PortZStage.text()
            Thread(target=Connect, name="Connecting Z-Stage", args=[port]).start()

    class TimeConstantLockInNormal:
        __table = [
            10e-6,
            30e-6,
            100e-6,
            300e-6,
            1e-3,
            3e-3,
            10e-3,
            30e-3,
            100e-3,
            300e-3,
            1e0,
            3e0,
            10e0,
            30e0,
            100e0,
            300e0,
            1e3,
            3e3,
            10e3,
            30e3,
        ]
        # Indices for the table above
        # Table is from the manual of the SR830
        # User might notice that there is no 1e-6/3e-6 and 100e3/300e3. Limitations of SR830
        BaseIndex: int = 0
        MultIndex: int = 0
        UnitIndex: int = 2
        IndexValue: int = BaseIndex + 2 * MultIndex + 6 * UnitIndex - 2
        Value: float = __table[IndexValue]

        def __init__(self, ui: Ui_MainWindow) -> None:
            self.widget = ui.TimeConstantNormal

            self.slider = ui.TimeNormalSlider
            self.slider.valueChanged.connect(self.UpdateSlider)

            # To update in next ui change
            self.slider.setMinimum(0)
            self.slider.setMaximum(19)
            self.slider.setInvertedAppearance(True)
            self.slider.setInvertedControls(False)
            self.slider.setSingleStep(1)
            self.slider.setPageStep(1)

            self.Time1 = ui.TimeNormal1
            self.Time3 = ui.TimeNormal3
            self.Timex1 = ui.TimeNormalx1
            self.Timex10 = ui.TimeNormalx10
            self.Timex100 = ui.TimeNormalx100
            self.Timemicros = ui.TimeNormalmicros
            self.Timems = ui.TimeNormalms
            self.Times = ui.TimeNormals
            self.Timeks = ui.TimeNormalks

            self.BaseGroup = QtWidgets.QButtonGroup()
            self.Time1.pressed.connect(self.UpdateC00)
            self.BaseGroup.addButton(self.Time1)
            self.Time3.pressed.connect(self.UpdateC01)
            self.BaseGroup.addButton(self.Time3)

            self.MultGroup = QtWidgets.QButtonGroup()
            self.Timex1.pressed.connect(self.UpdateC10)
            self.MultGroup.addButton(self.Timex1)
            self.Timex10.pressed.connect(self.UpdateC11)
            self.MultGroup.addButton(self.Timex10)
            self.Timex100.pressed.connect(self.UpdateC12)
            self.MultGroup.addButton(self.Timex100)

            self.UnitGroup = QtWidgets.QButtonGroup()
            self.Timemicros.pressed.connect(self.UpdateC20)
            self.UnitGroup.addButton(self.Timemicros)
            self.Timems.pressed.connect(self.UpdateC21)
            self.UnitGroup.addButton(self.Timems)
            self.Times.pressed.connect(self.UpdateC22)
            self.UnitGroup.addButton(self.Times)
            self.Timeks.pressed.connect(self.UpdateC23)
            self.UnitGroup.addButton(self.Timeks)

            self.slider.setValue(self.IndexValue)

        def __updateTotal(self, updateSlider: bool = True) -> None:
            self.IndexValue = (
                self.BaseIndex + 2 * self.MultIndex + 6 * self.UnitIndex - 2
            )
            self.Value = self.__table[self.IndexValue]
            if updateSlider:
                self.slider.setValue(self.IndexValue)
            print("New total: " + str(self.IndexValue))

        def __reverseIndex(self, index: int) -> tuple[int, int, int]:
            unit = index // 6
            rem = index % 6
            mult = rem // 2
            base = rem % 2
            return base, mult, unit

        def UpdateSlider(self) -> None:
            index = self.slider.value() + 2  # Compensation for 1e-6 and 3e-6

            self.Base, self.Mult, self.Unit = self.__reverseIndex(index)

            match self.Base:
                case 0:
                    self.Time1.setChecked(True)
                    self.BaseIndex = 0

                case 1:
                    self.Time3.setChecked(True)
                    self.BaseIndex = 1

            match self.Mult:
                case 0:
                    self.Timex1.setChecked(True)
                    self.MultIndex = 0

                case 1:
                    self.Timex10.setChecked(True)
                    self.MultIndex = 1

                case 2:
                    self.Timex100.setChecked(True)
                    self.MultIndex = 2

            match self.Unit:
                case 0:
                    self.Timex1.setEnabled(False)
                    match self.UnitIndex:
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Timemicros.setChecked(True)
                    self.UnitIndex = 0

                case 1:
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Timems.setChecked(True)
                    self.UnitIndex = 1

                case 2:
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Times.setChecked(True)
                    self.UnitIndex = 2

                case 3:
                    self.Timex100.setEnabled(False)
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)

                    self.Timeks.setChecked(True)
                    self.UnitIndex = 3

            self.__updateTotal(False)

        # See GUI from bottom left to top right.
        # This is more logical than top left to bottom right, trust me...
        # Left Column
        def UpdateC00(self) -> None:
            self.BaseIndex = 0
            self.__updateTotal()

        def UpdateC01(self) -> None:
            self.BaseIndex = 1
            self.__updateTotal()

        # Middle Column
        def UpdateC10(self) -> None:
            self.MultIndex = 0
            self.__updateTotal()

        def UpdateC11(self) -> None:
            self.MultIndex = 1
            self.__updateTotal()

        def UpdateC12(self) -> None:
            self.MultIndex = 2
            self.__updateTotal()

        # Right Column
        def UpdateC20(self) -> None:
            match self.UnitIndex:
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 0

            self.Timex1.setEnabled(False)
            # 1e-6 and 3e-6 do not exist
            if self.MultIndex == 0:
                self.Timex10.setChecked(True)
                self.UpdateC11()
            else:
                self.__updateTotal()

        def UpdateC21(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 1
            self.__updateTotal()

        def UpdateC22(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 2
            self.__updateTotal()

        def UpdateC23(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
            self.UnitIndex = 3

            # 1e3 and 3e3 do not exist
            self.Timex100.setEnabled(False)
            if self.MultIndex == 2:
                self.Timex10.setChecked(True)
                self.UpdateC11()
            else:
                self.__updateTotal()

    class SensitivityLockInNormal:
        def __init__(self, ui: Ui_MainWindow) -> None:
            self.widget = ui.SensitivityNormal

            self.slider = ui.SensNormalSlider

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
        __table = [
            10e-6,
            30e-6,
            100e-6,
            300e-6,
            1e-3,
            3e-3,
            10e-3,
            30e-3,
            100e-3,
            300e-3,
            1e0,
            3e0,
            10e0,
            30e0,
            100e0,
            300e0,
            1e3,
            3e3,
            10e3,
            30e3,
        ]
        # Indices for the table above
        # Table is from the manual of the SR830
        # User might notice that there is no 1e-6/3e-6 and 100e3/300e3. Limitations of SR830
        BaseIndex: int = 0
        MultIndex: int = 0
        UnitIndex: int = 2
        IndexValue: int = BaseIndex + 2 * MultIndex + 6 * UnitIndex - 2
        Value: float = __table[IndexValue]

        def __init__(self, ui: Ui_MainWindow) -> None:
            self.widget = ui.TimeConstantShear

            self.slider = ui.TimeShearSlider
            self.slider.valueChanged.connect(self.UpdateSlider)

            self.Time1 = ui.TimeShear1
            self.Time3 = ui.TimeShear3
            self.Timex1 = ui.TimeShearx1
            self.Timex10 = ui.TimeShearx10
            self.Timex100 = ui.TimeShearx100
            self.Timemicros = ui.TimeShearmicros
            self.Timems = ui.TimeShearms
            self.Times = ui.TimeShears
            self.Timeks = ui.TimeShearks

            self.BaseGroup = QtWidgets.QButtonGroup()
            self.Time1.pressed.connect(self.UpdateC00)
            self.BaseGroup.addButton(self.Time1)
            self.Time3.pressed.connect(self.UpdateC01)
            self.BaseGroup.addButton(self.Time3)

            self.MultGroup = QtWidgets.QButtonGroup()
            self.Timex1.pressed.connect(self.UpdateC10)
            self.MultGroup.addButton(self.Timex1)
            self.Timex10.pressed.connect(self.UpdateC11)
            self.MultGroup.addButton(self.Timex10)
            self.Timex100.pressed.connect(self.UpdateC12)
            self.MultGroup.addButton(self.Timex100)

            self.UnitGroup = QtWidgets.QButtonGroup()
            self.Timemicros.pressed.connect(self.UpdateC20)
            self.UnitGroup.addButton(self.Timemicros)
            self.Timems.pressed.connect(self.UpdateC21)
            self.UnitGroup.addButton(self.Timems)
            self.Times.pressed.connect(self.UpdateC22)
            self.UnitGroup.addButton(self.Times)
            self.Timeks.pressed.connect(self.UpdateC23)
            self.UnitGroup.addButton(self.Timeks)

            self.slider.setValue(self.IndexValue)

        def __updateTotal(self, updateSlider: bool = True) -> None:
            self.IndexValue = (
                self.BaseIndex + 2 * self.MultIndex + 6 * self.UnitIndex - 2
            )
            self.Value = self.__table[self.IndexValue]
            if updateSlider:
                self.slider.setValue(self.IndexValue)
            print("New total: " + str(self.IndexValue))

        def __reverseIndex(self, index: int) -> tuple[int, int, int]:
            unit = index // 6
            rem = index % 6
            mult = rem // 2
            base = rem % 2
            return base, mult, unit

        def UpdateSlider(self) -> None:
            index = self.slider.value() + 2  # Compensation for 1e-6 and 3e-6
            self.Base, self.Mult, self.Unit = self.__reverseIndex(index)

            match self.Base:
                case 0:
                    self.Time1.setChecked(True)
                    self.BaseIndex = 0

                case 1:
                    self.Time3.setChecked(True)
                    self.BaseIndex = 1

            match self.Mult:
                case 0:
                    self.Timex1.setChecked(True)
                    self.MultIndex = 0

                case 1:
                    self.Timex10.setChecked(True)
                    self.MultIndex = 1

                case 2:
                    self.Timex100.setChecked(True)
                    self.MultIndex = 2

            match self.Unit:
                case 0:
                    self.Timex1.setEnabled(False)
                    match self.UnitIndex:
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Timemicros.setChecked(True)
                    self.UnitIndex = 0

                case 1:
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Timems.setChecked(True)
                    self.UnitIndex = 1

                case 2:
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)
                        case 3:
                            self.Timex100.setEnabled(True)

                    self.Times.setChecked(True)
                    self.UnitIndex = 2

                case 3:
                    self.Timex100.setEnabled(False)
                    match self.UnitIndex:
                        case 0:
                            self.Timex1.setEnabled(True)

                    self.Timeks.setChecked(True)
                    self.UnitIndex = 3

            self.__updateTotal(False)

        # See GUI from bottom left to top right.
        # This is more logical than top left to bottom right, trust me...
        # Left Column
        def UpdateC00(self) -> None:
            self.BaseIndex = 0
            self.__updateTotal()

        def UpdateC01(self) -> None:
            self.BaseIndex = 1
            self.__updateTotal()

        # Middle Column
        def UpdateC10(self) -> None:
            self.MultIndex = 0
            self.__updateTotal()

        def UpdateC11(self) -> None:
            self.MultIndex = 1
            self.__updateTotal()

        def UpdateC12(self) -> None:
            self.MultIndex = 2
            self.__updateTotal()

        # Right Column
        def UpdateC20(self) -> None:
            match self.UnitIndex:
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 0

            # 1e-6 and 3e-6 do not exist
            self.Timex1.setEnabled(False)
            if self.MultIndex == 0:
                self.Timex10.setChecked(True)
                self.UpdateC11()
            else:
                self.__updateTotal()

        def UpdateC21(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 1
            self.__updateTotal()

        def UpdateC22(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
                case 3:
                    self.Timex100.setEnabled(True)
            self.UnitIndex = 2
            self.__updateTotal()

        def UpdateC23(self) -> None:
            match self.UnitIndex:
                case 0:
                    self.Timex1.setEnabled(True)
            self.UnitIndex = 3

            # 1e3 and 3e3 do not exist
            self.Timex100.setEnabled(False)
            if self.MultIndex == 2:
                self.Timex10.setChecked(True)
                self.UpdateC11()
            else:
                self.__updateTotal()

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
