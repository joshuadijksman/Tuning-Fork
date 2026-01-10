# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QScrollBar, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.HardwareWidget = QWidget(self.centralwidget)
        self.HardwareWidget.setObjectName(u"HardwareWidget")
        self.HardwareWidget.setGeometry(QRect(0, 0, 800, 546))
        sizePolicy.setHeightForWidth(self.HardwareWidget.sizePolicy().hasHeightForWidth())
        self.HardwareWidget.setSizePolicy(sizePolicy)
        self.HardwareWidget.setMaximumSize(QSize(16777215, 16777215))
        self.HardwareWidget.setBaseSize(QSize(800, 546))
        self.HardwareWidgetGrid = QGridLayout(self.HardwareWidget)
        self.HardwareWidgetGrid.setSpacing(0)
        self.HardwareWidgetGrid.setObjectName(u"HardwareWidgetGrid")
        self.HardwareWidgetGrid.setContentsMargins(5, 5, 5, 5)
        self.FreqGenWidgetGroup = QWidget(self.HardwareWidget)
        self.FreqGenWidgetGroup.setObjectName(u"FreqGenWidgetGroup")
        self.FreqGenWidget = QWidget(self.FreqGenWidgetGroup)
        self.FreqGenWidget.setObjectName(u"FreqGenWidget")
        self.FreqGenWidget.setGeometry(QRect(0, 0, 262, 541))
        sizePolicy.setHeightForWidth(self.FreqGenWidget.sizePolicy().hasHeightForWidth())
        self.FreqGenWidget.setSizePolicy(sizePolicy)
        self.FreqGenWidget.setBaseSize(QSize(262, 544))
        self.gridLayout_12 = QGridLayout(self.FreqGenWidget)
        self.gridLayout_12.setSpacing(3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(6, 6, 6, 6)
        self.FreqGenFrame = QFrame(self.FreqGenWidget)
        self.FreqGenFrame.setObjectName(u"FreqGenFrame")
        self.FreqGenFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FreqGenFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.labelFreqGen = QLabel(self.FreqGenFrame)
        self.labelFreqGen.setObjectName(u"labelFreqGen")
        self.labelFreqGen.setGeometry(QRect(10, 0, 233, 22))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelFreqGen.sizePolicy().hasHeightForWidth())
        self.labelFreqGen.setSizePolicy(sizePolicy1)
        self.labelFreqGen.setMinimumSize(QSize(50, 22))
        self.labelFreqGen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FreqGenOptionsFrame = QFrame(self.FreqGenFrame)
        self.FreqGenOptionsFrame.setObjectName(u"FreqGenOptionsFrame")
        self.FreqGenOptionsFrame.setGeometry(QRect(0, 22, 251, 507))
        sizePolicy1.setHeightForWidth(self.FreqGenOptionsFrame.sizePolicy().hasHeightForWidth())
        self.FreqGenOptionsFrame.setSizePolicy(sizePolicy1)
        self.gridLayout_26 = QGridLayout(self.FreqGenOptionsFrame)
        self.gridLayout_26.setSpacing(3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.FreqGenChan1Box = QGroupBox(self.FreqGenOptionsFrame)
        self.FreqGenChan1Box.setObjectName(u"FreqGenChan1Box")
        self.gridLayout_39 = QGridLayout(self.FreqGenChan1Box)
        self.gridLayout_39.setSpacing(6)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(1, 1, 1, 1)
        self.FreqGenChan1AmpUnitFrame = QFrame(self.FreqGenChan1Box)
        self.FreqGenChan1AmpUnitFrame.setObjectName(u"FreqGenChan1AmpUnitFrame")
        self.FreqGenChan1AmpUnitFrame.setEnabled(False)
        self.verticalLayout = QVBoxLayout(self.FreqGenChan1AmpUnitFrame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.labFreqGenChan1AmpUnit = QLabel(self.FreqGenChan1AmpUnitFrame)
        self.labFreqGenChan1AmpUnit.setObjectName(u"labFreqGenChan1AmpUnit")
        self.labFreqGenChan1AmpUnit.setEnabled(False)

        self.verticalLayout.addWidget(self.labFreqGenChan1AmpUnit)

        self.FreqGenChan1AmpUnitOptionsFrame = QFrame(self.FreqGenChan1AmpUnitFrame)
        self.FreqGenChan1AmpUnitOptionsFrame.setObjectName(u"FreqGenChan1AmpUnitOptionsFrame")
        self.gridLayout_43 = QGridLayout(self.FreqGenChan1AmpUnitOptionsFrame)
        self.gridLayout_43.setSpacing(2)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.gridLayout_43.setContentsMargins(1, 1, 1, 1)
        self.FreqGeqChan1Vpp = QPushButton(self.FreqGenChan1AmpUnitOptionsFrame)
        self.FreqGeqChan1Vpp.setObjectName(u"FreqGeqChan1Vpp")

        self.gridLayout_43.addWidget(self.FreqGeqChan1Vpp, 0, 0, 1, 1)

        self.FreqGeqChan1Vrms = QPushButton(self.FreqGenChan1AmpUnitOptionsFrame)
        self.FreqGeqChan1Vrms.setObjectName(u"FreqGeqChan1Vrms")

        self.gridLayout_43.addWidget(self.FreqGeqChan1Vrms, 0, 1, 1, 1)

        self.FreqGeqChan1dBm = QPushButton(self.FreqGenChan1AmpUnitOptionsFrame)
        self.FreqGeqChan1dBm.setObjectName(u"FreqGeqChan1dBm")

        self.gridLayout_43.addWidget(self.FreqGeqChan1dBm, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.FreqGenChan1AmpUnitOptionsFrame)


        self.gridLayout_39.addWidget(self.FreqGenChan1AmpUnitFrame, 2, 0, 1, 1)

        self.FreqGenChan1WaveformFrame = QFrame(self.FreqGenChan1Box)
        self.FreqGenChan1WaveformFrame.setObjectName(u"FreqGenChan1WaveformFrame")
        self.verticalLayout_3 = QVBoxLayout(self.FreqGenChan1WaveformFrame)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.labFreqGenChan1Waveform = QLabel(self.FreqGenChan1WaveformFrame)
        self.labFreqGenChan1Waveform.setObjectName(u"labFreqGenChan1Waveform")

        self.verticalLayout_3.addWidget(self.labFreqGenChan1Waveform)

        self.FreqGenChan1WaveformOptionsFrame = QFrame(self.FreqGenChan1WaveformFrame)
        self.FreqGenChan1WaveformOptionsFrame.setObjectName(u"FreqGenChan1WaveformOptionsFrame")
        self.gridLayout_44 = QGridLayout(self.FreqGenChan1WaveformOptionsFrame)
        self.gridLayout_44.setSpacing(2)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(1, 1, 1, 1)
        self.FreqGeqChan1Ramp = QPushButton(self.FreqGenChan1WaveformOptionsFrame)
        self.FreqGeqChan1Ramp.setObjectName(u"FreqGeqChan1Ramp")

        self.gridLayout_44.addWidget(self.FreqGeqChan1Ramp, 0, 2, 1, 1)

        self.FreqGeqChan1Sine = QPushButton(self.FreqGenChan1WaveformOptionsFrame)
        self.FreqGeqChan1Sine.setObjectName(u"FreqGeqChan1Sine")

        self.gridLayout_44.addWidget(self.FreqGeqChan1Sine, 0, 0, 1, 1)

        self.FreqGeqChan1Square = QPushButton(self.FreqGenChan1WaveformOptionsFrame)
        self.FreqGeqChan1Square.setObjectName(u"FreqGeqChan1Square")

        self.gridLayout_44.addWidget(self.FreqGeqChan1Square, 0, 1, 1, 1)

        self.FreqGeqChan1Pulse = QPushButton(self.FreqGenChan1WaveformOptionsFrame)
        self.FreqGeqChan1Pulse.setObjectName(u"FreqGeqChan1Pulse")

        self.gridLayout_44.addWidget(self.FreqGeqChan1Pulse, 0, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.FreqGenChan1WaveformOptionsFrame)


        self.gridLayout_39.addWidget(self.FreqGenChan1WaveformFrame, 3, 0, 1, 1)

        self.FreqGenChan1Output = QCheckBox(self.FreqGenChan1Box)
        self.FreqGenChan1Output.setObjectName(u"FreqGenChan1Output")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.FreqGenChan1Output.sizePolicy().hasHeightForWidth())
        self.FreqGenChan1Output.setSizePolicy(sizePolicy2)
        self.FreqGenChan1Output.setChecked(True)

        self.gridLayout_39.addWidget(self.FreqGenChan1Output, 0, 0, 1, 1)

        self.FreqGenChan1FreqAmpFrame = QFrame(self.FreqGenChan1Box)
        self.FreqGenChan1FreqAmpFrame.setObjectName(u"FreqGenChan1FreqAmpFrame")
        self.gridLayout_67 = QGridLayout(self.FreqGenChan1FreqAmpFrame)
        self.gridLayout_67.setSpacing(6)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setContentsMargins(1, 1, 1, 1)
        self.labFreqGenChan1Amplitude = QLabel(self.FreqGenChan1FreqAmpFrame)
        self.labFreqGenChan1Amplitude.setObjectName(u"labFreqGenChan1Amplitude")
        self.labFreqGenChan1Amplitude.setEnabled(False)

        self.gridLayout_67.addWidget(self.labFreqGenChan1Amplitude, 1, 0, 1, 1)

        self.FreqGenChan1Amplitude = QDoubleSpinBox(self.FreqGenChan1FreqAmpFrame)
        self.FreqGenChan1Amplitude.setObjectName(u"FreqGenChan1Amplitude")
        self.FreqGenChan1Amplitude.setEnabled(False)
        self.FreqGenChan1Amplitude.setDecimals(4)
        self.FreqGenChan1Amplitude.setMinimum(0.002500000000000)
        self.FreqGenChan1Amplitude.setMaximum(10.000000000000000)
        self.FreqGenChan1Amplitude.setSingleStep(0.000100000000000)
        self.FreqGenChan1Amplitude.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_67.addWidget(self.FreqGenChan1Amplitude, 1, 1, 1, 1)

        self.labFreqGenChan1Frequency = QLabel(self.FreqGenChan1FreqAmpFrame)
        self.labFreqGenChan1Frequency.setObjectName(u"labFreqGenChan1Frequency")

        self.gridLayout_67.addWidget(self.labFreqGenChan1Frequency, 0, 0, 1, 1)

        self.FreqGenChan1Frequency = QDoubleSpinBox(self.FreqGenChan1FreqAmpFrame)
        self.FreqGenChan1Frequency.setObjectName(u"FreqGenChan1Frequency")
        self.FreqGenChan1Frequency.setDecimals(6)
        self.FreqGenChan1Frequency.setMinimum(0.000001000000000)
        self.FreqGenChan1Frequency.setMaximum(30000000.000000000000000)
        self.FreqGenChan1Frequency.setSingleStep(0.000001000000000)
        self.FreqGenChan1Frequency.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.FreqGenChan1Frequency.setValue(800.000000000000000)

        self.gridLayout_67.addWidget(self.FreqGenChan1Frequency, 0, 1, 1, 1)


        self.gridLayout_39.addWidget(self.FreqGenChan1FreqAmpFrame, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.FreqGenChan1Box, 2, 0, 1, 1)

        self.ConnectFreqGen = QPushButton(self.FreqGenOptionsFrame)
        self.ConnectFreqGen.setObjectName(u"ConnectFreqGen")
        sizePolicy2.setHeightForWidth(self.ConnectFreqGen.sizePolicy().hasHeightForWidth())
        self.ConnectFreqGen.setSizePolicy(sizePolicy2)

        self.gridLayout_26.addWidget(self.ConnectFreqGen, 1, 0, 1, 1)

        self.FreqGenVisaFrame = QFrame(self.FreqGenOptionsFrame)
        self.FreqGenVisaFrame.setObjectName(u"FreqGenVisaFrame")
        sizePolicy2.setHeightForWidth(self.FreqGenVisaFrame.sizePolicy().hasHeightForWidth())
        self.FreqGenVisaFrame.setSizePolicy(sizePolicy2)
        self.FreqGenVisaFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FreqGenVisaFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_36 = QGridLayout(self.FreqGenVisaFrame)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 0, 0, 0)
        self.VISAFreqGen = QLineEdit(self.FreqGenVisaFrame)
        self.VISAFreqGen.setObjectName(u"VISAFreqGen")
        sizePolicy1.setHeightForWidth(self.VISAFreqGen.sizePolicy().hasHeightForWidth())
        self.VISAFreqGen.setSizePolicy(sizePolicy1)

        self.gridLayout_36.addWidget(self.VISAFreqGen, 0, 1, 1, 1)

        self.labVISAFreqGen = QLabel(self.FreqGenVisaFrame)
        self.labVISAFreqGen.setObjectName(u"labVISAFreqGen")

        self.gridLayout_36.addWidget(self.labVISAFreqGen, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.FreqGenVisaFrame, 0, 0, 1, 1)

        self.FreqGenChan2Box = QGroupBox(self.FreqGenOptionsFrame)
        self.FreqGenChan2Box.setObjectName(u"FreqGenChan2Box")
        self.gridLayout_40 = QGridLayout(self.FreqGenChan2Box)
        self.gridLayout_40.setSpacing(6)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(1, 1, 1, 1)
        self.FreqGenChan2Output = QCheckBox(self.FreqGenChan2Box)
        self.FreqGenChan2Output.setObjectName(u"FreqGenChan2Output")
        self.FreqGenChan2Output.setChecked(True)

        self.gridLayout_40.addWidget(self.FreqGenChan2Output, 0, 0, 1, 1)

        self.FreqGenChan2WaveformFrame = QFrame(self.FreqGenChan2Box)
        self.FreqGenChan2WaveformFrame.setObjectName(u"FreqGenChan2WaveformFrame")
        self.verticalLayout_16 = QVBoxLayout(self.FreqGenChan2WaveformFrame)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.labFreqGenChan2Waveform = QLabel(self.FreqGenChan2WaveformFrame)
        self.labFreqGenChan2Waveform.setObjectName(u"labFreqGenChan2Waveform")

        self.verticalLayout_16.addWidget(self.labFreqGenChan2Waveform)

        self.FreqGenChan2WaveformOptionsFrame = QFrame(self.FreqGenChan2WaveformFrame)
        self.FreqGenChan2WaveformOptionsFrame.setObjectName(u"FreqGenChan2WaveformOptionsFrame")
        self.gridLayout_66 = QGridLayout(self.FreqGenChan2WaveformOptionsFrame)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setHorizontalSpacing(2)
        self.gridLayout_66.setVerticalSpacing(6)
        self.gridLayout_66.setContentsMargins(1, 1, 1, 1)
        self.FreqGenChan2Ramp = QPushButton(self.FreqGenChan2WaveformOptionsFrame)
        self.FreqGenChan2Ramp.setObjectName(u"FreqGenChan2Ramp")

        self.gridLayout_66.addWidget(self.FreqGenChan2Ramp, 0, 2, 1, 1)

        self.FreqGeqChan2Sine = QPushButton(self.FreqGenChan2WaveformOptionsFrame)
        self.FreqGeqChan2Sine.setObjectName(u"FreqGeqChan2Sine")

        self.gridLayout_66.addWidget(self.FreqGeqChan2Sine, 0, 0, 1, 1)

        self.FreqGenChan2Sqaure = QPushButton(self.FreqGenChan2WaveformOptionsFrame)
        self.FreqGenChan2Sqaure.setObjectName(u"FreqGenChan2Sqaure")

        self.gridLayout_66.addWidget(self.FreqGenChan2Sqaure, 0, 1, 1, 1)

        self.FreqGenChan2Pulse = QPushButton(self.FreqGenChan2WaveformOptionsFrame)
        self.FreqGenChan2Pulse.setObjectName(u"FreqGenChan2Pulse")

        self.gridLayout_66.addWidget(self.FreqGenChan2Pulse, 0, 3, 1, 1)


        self.verticalLayout_16.addWidget(self.FreqGenChan2WaveformOptionsFrame)


        self.gridLayout_40.addWidget(self.FreqGenChan2WaveformFrame, 4, 0, 1, 1)

        self.FreqGenChan2FreqAmpFrame = QFrame(self.FreqGenChan2Box)
        self.FreqGenChan2FreqAmpFrame.setObjectName(u"FreqGenChan2FreqAmpFrame")
        self.gridLayout_61 = QGridLayout(self.FreqGenChan2FreqAmpFrame)
        self.gridLayout_61.setSpacing(6)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.gridLayout_61.setContentsMargins(1, 1, 1, 1)
        self.FreqGenChan2Amplitude = QDoubleSpinBox(self.FreqGenChan2FreqAmpFrame)
        self.FreqGenChan2Amplitude.setObjectName(u"FreqGenChan2Amplitude")
        self.FreqGenChan2Amplitude.setEnabled(False)
        self.FreqGenChan2Amplitude.setDecimals(4)
        self.FreqGenChan2Amplitude.setMinimum(0.002500000000000)
        self.FreqGenChan2Amplitude.setMaximum(10.000000000000000)
        self.FreqGenChan2Amplitude.setSingleStep(0.000100000000000)
        self.FreqGenChan2Amplitude.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_61.addWidget(self.FreqGenChan2Amplitude, 1, 1, 1, 1)

        self.labFreqGenChan2Frequency = QLabel(self.FreqGenChan2FreqAmpFrame)
        self.labFreqGenChan2Frequency.setObjectName(u"labFreqGenChan2Frequency")

        self.gridLayout_61.addWidget(self.labFreqGenChan2Frequency, 0, 0, 1, 1)

        self.labFreqGenChan2Amplitude = QLabel(self.FreqGenChan2FreqAmpFrame)
        self.labFreqGenChan2Amplitude.setObjectName(u"labFreqGenChan2Amplitude")
        self.labFreqGenChan2Amplitude.setEnabled(False)

        self.gridLayout_61.addWidget(self.labFreqGenChan2Amplitude, 1, 0, 1, 1)

        self.FreqGenChan2Frequency = QDoubleSpinBox(self.FreqGenChan2FreqAmpFrame)
        self.FreqGenChan2Frequency.setObjectName(u"FreqGenChan2Frequency")
        self.FreqGenChan2Frequency.setDecimals(6)
        self.FreqGenChan2Frequency.setMinimum(0.000001000000000)
        self.FreqGenChan2Frequency.setMaximum(30000000.000000000000000)
        self.FreqGenChan2Frequency.setSingleStep(0.000001000000000)
        self.FreqGenChan2Frequency.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.FreqGenChan2Frequency.setValue(452.000000000000000)

        self.gridLayout_61.addWidget(self.FreqGenChan2Frequency, 0, 1, 1, 1)


        self.gridLayout_40.addWidget(self.FreqGenChan2FreqAmpFrame, 1, 0, 1, 1)

        self.FreqGenChan2AmpUnitFrame = QFrame(self.FreqGenChan2Box)
        self.FreqGenChan2AmpUnitFrame.setObjectName(u"FreqGenChan2AmpUnitFrame")
        self.FreqGenChan2AmpUnitFrame.setEnabled(False)
        self.verticalLayout_15 = QVBoxLayout(self.FreqGenChan2AmpUnitFrame)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.labFreqGenChan2AmpUnit = QLabel(self.FreqGenChan2AmpUnitFrame)
        self.labFreqGenChan2AmpUnit.setObjectName(u"labFreqGenChan2AmpUnit")
        self.labFreqGenChan2AmpUnit.setEnabled(False)

        self.verticalLayout_15.addWidget(self.labFreqGenChan2AmpUnit)

        self.FreqGenChan2AmpUnitOptionsFrame = QFrame(self.FreqGenChan2AmpUnitFrame)
        self.FreqGenChan2AmpUnitOptionsFrame.setObjectName(u"FreqGenChan2AmpUnitOptionsFrame")
        self.gridLayout_65 = QGridLayout(self.FreqGenChan2AmpUnitOptionsFrame)
        self.gridLayout_65.setSpacing(2)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setContentsMargins(1, 1, 1, 1)
        self.FreqGeqChan2Vpp = QPushButton(self.FreqGenChan2AmpUnitOptionsFrame)
        self.FreqGeqChan2Vpp.setObjectName(u"FreqGeqChan2Vpp")

        self.gridLayout_65.addWidget(self.FreqGeqChan2Vpp, 0, 0, 1, 1)

        self.FreqGeqChan2Vrms = QPushButton(self.FreqGenChan2AmpUnitOptionsFrame)
        self.FreqGeqChan2Vrms.setObjectName(u"FreqGeqChan2Vrms")

        self.gridLayout_65.addWidget(self.FreqGeqChan2Vrms, 0, 1, 1, 1)

        self.FreqGeqChan2dBm = QPushButton(self.FreqGenChan2AmpUnitOptionsFrame)
        self.FreqGeqChan2dBm.setObjectName(u"FreqGeqChan2dBm")

        self.gridLayout_65.addWidget(self.FreqGeqChan2dBm, 0, 2, 1, 1)


        self.verticalLayout_15.addWidget(self.FreqGenChan2AmpUnitOptionsFrame)


        self.gridLayout_40.addWidget(self.FreqGenChan2AmpUnitFrame, 2, 0, 1, 1)


        self.gridLayout_26.addWidget(self.FreqGenChan2Box, 3, 0, 1, 1)


        self.gridLayout_12.addWidget(self.FreqGenFrame, 0, 0, 1, 1)


        self.HardwareWidgetGrid.addWidget(self.FreqGenWidgetGroup, 0, 1, 1, 1)

        self.HeightGaugeZstageGroup = QWidget(self.HardwareWidget)
        self.HeightGaugeZstageGroup.setObjectName(u"HeightGaugeZstageGroup")
        self.HeightGaugeZstageWidget = QWidget(self.HeightGaugeZstageGroup)
        self.HeightGaugeZstageWidget.setObjectName(u"HeightGaugeZstageWidget")
        self.HeightGaugeZstageWidget.setGeometry(QRect(0, 0, 262, 544))
        sizePolicy.setHeightForWidth(self.HeightGaugeZstageWidget.sizePolicy().hasHeightForWidth())
        self.HeightGaugeZstageWidget.setSizePolicy(sizePolicy)
        self.HeightGaugeZstageWidget.setBaseSize(QSize(262, 544))
        self.gridLayout_11 = QGridLayout(self.HeightGaugeZstageWidget)
        self.gridLayout_11.setSpacing(3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.ZStageFrame = QFrame(self.HeightGaugeZstageWidget)
        self.ZStageFrame.setObjectName(u"ZStageFrame")
        self.ZStageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ZStageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_34 = QGridLayout(self.ZStageFrame)
        self.gridLayout_34.setSpacing(3)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(1, 1, 1, 1)
        self.ZStagePortFrame = QFrame(self.ZStageFrame)
        self.ZStagePortFrame.setObjectName(u"ZStagePortFrame")
        sizePolicy1.setHeightForWidth(self.ZStagePortFrame.sizePolicy().hasHeightForWidth())
        self.ZStagePortFrame.setSizePolicy(sizePolicy1)
        self.ZStagePortFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ZStagePortFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_35 = QGridLayout(self.ZStagePortFrame)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.labPortZStage = QLabel(self.ZStagePortFrame)
        self.labPortZStage.setObjectName(u"labPortZStage")

        self.gridLayout_35.addWidget(self.labPortZStage, 0, 0, 1, 1)

        self.PortZStage = QLineEdit(self.ZStagePortFrame)
        self.PortZStage.setObjectName(u"PortZStage")
        sizePolicy1.setHeightForWidth(self.PortZStage.sizePolicy().hasHeightForWidth())
        self.PortZStage.setSizePolicy(sizePolicy1)

        self.gridLayout_35.addWidget(self.PortZStage, 0, 1, 1, 1)


        self.gridLayout_34.addWidget(self.ZStagePortFrame, 2, 0, 1, 1)

        self.ConnectZStage = QPushButton(self.ZStageFrame)
        self.ConnectZStage.setObjectName(u"ConnectZStage")

        self.gridLayout_34.addWidget(self.ConnectZStage, 3, 0, 1, 1)

        self.labelZStage = QLabel(self.ZStageFrame)
        self.labelZStage.setObjectName(u"labelZStage")
        sizePolicy1.setHeightForWidth(self.labelZStage.sizePolicy().hasHeightForWidth())
        self.labelZStage.setSizePolicy(sizePolicy1)
        self.labelZStage.setMinimumSize(QSize(50, 22))
        self.labelZStage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_34.addWidget(self.labelZStage, 0, 0, 1, 1)

        self.tabZStageFrame = QTabWidget(self.ZStageFrame)
        self.tabZStageFrame.setObjectName(u"tabZStageFrame")
        sizePolicy.setHeightForWidth(self.tabZStageFrame.sizePolicy().hasHeightForWidth())
        self.tabZStageFrame.setSizePolicy(sizePolicy)
        self.ZStageVolt = QWidget()
        self.ZStageVolt.setObjectName(u"ZStageVolt")
        self.ZStageVoltFrame = QFrame(self.ZStageVolt)
        self.ZStageVoltFrame.setObjectName(u"ZStageVoltFrame")
        self.ZStageVoltFrame.setGeometry(QRect(0, 0, 241, 151))
        sizePolicy.setHeightForWidth(self.ZStageVoltFrame.sizePolicy().hasHeightForWidth())
        self.ZStageVoltFrame.setSizePolicy(sizePolicy)
        self.gridLayout_37 = QGridLayout(self.ZStageVoltFrame)
        self.gridLayout_37.setSpacing(3)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(5, 5, 5, 5)
        self.ZStageVButton = QPushButton(self.ZStageVoltFrame)
        self.ZStageVButton.setObjectName(u"ZStageVButton")

        self.gridLayout_37.addWidget(self.ZStageVButton, 0, 0, 1, 1)

        self.ZStageV = QDoubleSpinBox(self.ZStageVoltFrame)
        self.ZStageV.setObjectName(u"ZStageV")
        self.ZStageV.setMaximum(140.000000000000000)
        self.ZStageV.setSingleStep(0.010000000000000)
        self.ZStageV.setValue(10.000000000000000)

        self.gridLayout_37.addWidget(self.ZStageV, 0, 1, 1, 1)

        self.tabZStageFrame.addTab(self.ZStageVolt, "")
        self.ZStageCalibrate = QWidget()
        self.ZStageCalibrate.setObjectName(u"ZStageCalibrate")
        self.ZStageCalibrateOptionsWidgetWidget = QWidget(self.ZStageCalibrate)
        self.ZStageCalibrateOptionsWidgetWidget.setObjectName(u"ZStageCalibrateOptionsWidgetWidget")
        self.ZStageCalibrateOptionsWidgetWidget.setGeometry(QRect(0, 22, 227, 136))
        sizePolicy.setHeightForWidth(self.ZStageCalibrateOptionsWidgetWidget.sizePolicy().hasHeightForWidth())
        self.ZStageCalibrateOptionsWidgetWidget.setSizePolicy(sizePolicy)
        self.ZStageCalibrateOptionsWidgetWidget.setBaseSize(QSize(227, 136))
        self.ZStageCalibrateOptionsWidget = QWidget(self.ZStageCalibrateOptionsWidgetWidget)
        self.ZStageCalibrateOptionsWidget.setObjectName(u"ZStageCalibrateOptionsWidget")
        self.ZStageCalibrateOptionsWidget.setGeometry(QRect(0, 0, 231, 131))
        self.gridLayout_38 = QGridLayout(self.ZStageCalibrateOptionsWidget)
        self.gridLayout_38.setSpacing(3)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(5, 5, 5, 5)
        self.labZStageStepV = QLabel(self.ZStageCalibrateOptionsWidget)
        self.labZStageStepV.setObjectName(u"labZStageStepV")

        self.gridLayout_38.addWidget(self.labZStageStepV, 2, 0, 1, 1)

        self.labZStageMaxV = QLabel(self.ZStageCalibrateOptionsWidget)
        self.labZStageMaxV.setObjectName(u"labZStageMaxV")

        self.gridLayout_38.addWidget(self.labZStageMaxV, 1, 0, 1, 1)

        self.labZStageMinV = QLabel(self.ZStageCalibrateOptionsWidget)
        self.labZStageMinV.setObjectName(u"labZStageMinV")

        self.gridLayout_38.addWidget(self.labZStageMinV, 0, 0, 1, 1)

        self.ZStageMinV = QDoubleSpinBox(self.ZStageCalibrateOptionsWidget)
        self.ZStageMinV.setObjectName(u"ZStageMinV")
        self.ZStageMinV.setMaximum(140.000000000000000)
        self.ZStageMinV.setValue(10.000000000000000)

        self.gridLayout_38.addWidget(self.ZStageMinV, 0, 1, 1, 1)

        self.ZStageMaxV = QDoubleSpinBox(self.ZStageCalibrateOptionsWidget)
        self.ZStageMaxV.setObjectName(u"ZStageMaxV")
        self.ZStageMaxV.setMaximum(140.000000000000000)
        self.ZStageMaxV.setValue(120.000000000000000)

        self.gridLayout_38.addWidget(self.ZStageMaxV, 1, 1, 1, 1)

        self.ZStageStepV = QDoubleSpinBox(self.ZStageCalibrateOptionsWidget)
        self.ZStageStepV.setObjectName(u"ZStageStepV")
        self.ZStageStepV.setDecimals(2)
        self.ZStageStepV.setMinimum(0.010000000000000)
        self.ZStageStepV.setSingleStep(0.010000000000000)
        self.ZStageStepV.setValue(1.000000000000000)

        self.gridLayout_38.addWidget(self.ZStageStepV, 2, 1, 1, 1)

        self.ZStageCalibrateButton = QPushButton(self.ZStageCalibrate)
        self.ZStageCalibrateButton.setObjectName(u"ZStageCalibrateButton")
        self.ZStageCalibrateButton.setGeometry(QRect(0, 0, 231, 26))
        sizePolicy2.setHeightForWidth(self.ZStageCalibrateButton.sizePolicy().hasHeightForWidth())
        self.ZStageCalibrateButton.setSizePolicy(sizePolicy2)
        self.tabZStageFrame.addTab(self.ZStageCalibrate, "")

        self.gridLayout_34.addWidget(self.tabZStageFrame, 4, 0, 1, 1)


        self.gridLayout_11.addWidget(self.ZStageFrame, 1, 0, 1, 1)

        self.HeightGaugeFrame = QFrame(self.HeightGaugeZstageWidget)
        self.HeightGaugeFrame.setObjectName(u"HeightGaugeFrame")
        self.HeightGaugeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeightGaugeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.HeightGaugeFrame)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(1, 1, 1, 1)
        self.labelHeightGauge = QLabel(self.HeightGaugeFrame)
        self.labelHeightGauge.setObjectName(u"labelHeightGauge")
        sizePolicy1.setHeightForWidth(self.labelHeightGauge.sizePolicy().hasHeightForWidth())
        self.labelHeightGauge.setSizePolicy(sizePolicy1)
        self.labelHeightGauge.setMinimumSize(QSize(50, 22))
        self.labelHeightGauge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_27.addWidget(self.labelHeightGauge, 0, 0, 1, 1)

        self.ConnecHeightGauge = QPushButton(self.HeightGaugeFrame)
        self.ConnecHeightGauge.setObjectName(u"ConnecHeightGauge")

        self.gridLayout_27.addWidget(self.ConnecHeightGauge, 2, 0, 1, 1)

        self.HeightGaugePortFrame = QFrame(self.HeightGaugeFrame)
        self.HeightGaugePortFrame.setObjectName(u"HeightGaugePortFrame")
        sizePolicy1.setHeightForWidth(self.HeightGaugePortFrame.sizePolicy().hasHeightForWidth())
        self.HeightGaugePortFrame.setSizePolicy(sizePolicy1)
        self.HeightGaugePortFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeightGaugePortFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.HeightGaugePortFrame)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.labHeightGaugePort = QLabel(self.HeightGaugePortFrame)
        self.labHeightGaugePort.setObjectName(u"labHeightGaugePort")

        self.gridLayout_28.addWidget(self.labHeightGaugePort, 0, 0, 1, 1)

        self.PortHeightGauge = QLineEdit(self.HeightGaugePortFrame)
        self.PortHeightGauge.setObjectName(u"PortHeightGauge")
        sizePolicy1.setHeightForWidth(self.PortHeightGauge.sizePolicy().hasHeightForWidth())
        self.PortHeightGauge.setSizePolicy(sizePolicy1)

        self.gridLayout_28.addWidget(self.PortHeightGauge, 0, 1, 1, 1)


        self.gridLayout_27.addWidget(self.HeightGaugePortFrame, 1, 0, 1, 1)

        self.HeightGaugeUtilityFrame = QFrame(self.HeightGaugeFrame)
        self.HeightGaugeUtilityFrame.setObjectName(u"HeightGaugeUtilityFrame")
        self.gridLayout_29 = QGridLayout(self.HeightGaugeUtilityFrame)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.HeightGaugeTare = QPushButton(self.HeightGaugeUtilityFrame)
        self.HeightGaugeTare.setObjectName(u"HeightGaugeTare")

        self.gridLayout_29.addWidget(self.HeightGaugeTare, 0, 0, 1, 1)

        self.HeightGaugeMeasure = QPushButton(self.HeightGaugeUtilityFrame)
        self.HeightGaugeMeasure.setObjectName(u"HeightGaugeMeasure")

        self.gridLayout_29.addWidget(self.HeightGaugeMeasure, 1, 0, 1, 1)

        self.HeightGaugeResult = QLineEdit(self.HeightGaugeUtilityFrame)
        self.HeightGaugeResult.setObjectName(u"HeightGaugeResult")
        self.HeightGaugeResult.setAcceptDrops(False)
        self.HeightGaugeResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.HeightGaugeResult.setReadOnly(True)

        self.gridLayout_29.addWidget(self.HeightGaugeResult, 2, 0, 1, 1)


        self.gridLayout_27.addWidget(self.HeightGaugeUtilityFrame, 3, 0, 1, 1)


        self.gridLayout_11.addWidget(self.HeightGaugeFrame, 0, 0, 1, 1)


        self.HardwareWidgetGrid.addWidget(self.HeightGaugeZstageGroup, 0, 2, 1, 1)

        self.LockInAmpGroup = QWidget(self.HardwareWidget)
        self.LockInAmpGroup.setObjectName(u"LockInAmpGroup")
        self.LockInAmpGroupWidget = QWidget(self.LockInAmpGroup)
        self.LockInAmpGroupWidget.setObjectName(u"LockInAmpGroupWidget")
        self.LockInAmpGroupWidget.setGeometry(QRect(0, 0, 257, 541))
        sizePolicy.setHeightForWidth(self.LockInAmpGroupWidget.sizePolicy().hasHeightForWidth())
        self.LockInAmpGroupWidget.setSizePolicy(sizePolicy)
        self.LockInAmpGroupWidget.setBaseSize(QSize(257, 528))
        self.gridLayout_13 = QGridLayout(self.LockInAmpGroupWidget)
        self.gridLayout_13.setSpacing(3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(5, 5, 5, 5)
        self.LockInNormalFrame = QFrame(self.LockInAmpGroupWidget)
        self.LockInNormalFrame.setObjectName(u"LockInNormalFrame")
        self.LockInNormalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LockInNormalFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.LockInNormalFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.tabLockInNormal = QTabWidget(self.LockInNormalFrame)
        self.tabLockInNormal.setObjectName(u"tabLockInNormal")
        sizePolicy.setHeightForWidth(self.tabLockInNormal.sizePolicy().hasHeightForWidth())
        self.tabLockInNormal.setSizePolicy(sizePolicy)
        self.TimeConstantNormal = QWidget()
        self.TimeConstantNormal.setObjectName(u"TimeConstantNormal")
        self.TimeNormaSlider = QScrollBar(self.TimeConstantNormal)
        self.TimeNormaSlider.setObjectName(u"TimeNormaSlider")
        self.TimeNormaSlider.setGeometry(QRect(0, 0, 20, 142))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TimeNormaSlider.sizePolicy().hasHeightForWidth())
        self.TimeNormaSlider.setSizePolicy(sizePolicy3)
        self.TimeNormaSlider.setBaseSize(QSize(20, 142))
        self.TimeNormaSlider.setOrientation(Qt.Orientation.Vertical)
        self.TimeNormalGrid = QWidget(self.TimeConstantNormal)
        self.TimeNormalGrid.setObjectName(u"TimeNormalGrid")
        self.TimeNormalGrid.setGeometry(QRect(26, 0, 185, 142))
        sizePolicy.setHeightForWidth(self.TimeNormalGrid.sizePolicy().hasHeightForWidth())
        self.TimeNormalGrid.setSizePolicy(sizePolicy)
        self.TimeNormalGrid.setBaseSize(QSize(185, 142))
        self.gridLayout_8 = QGridLayout(self.TimeNormalGrid)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.TimeNormal2 = QRadioButton(self.TimeNormalGrid)
        self.TimeNormal2.setObjectName(u"TimeNormal2")
        self.TimeNormal2.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormal2, 2, 0, 1, 1)

        self.TimeNormalx100 = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalx100.setObjectName(u"TimeNormalx100")
        self.TimeNormalx100.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalx100, 1, 1, 1, 1)

        self.TimeNormalks = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalks.setObjectName(u"TimeNormalks")
        self.TimeNormalks.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalks, 0, 2, 1, 1)

        self.TimeNormalms = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalms.setObjectName(u"TimeNormalms")
        self.TimeNormalms.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalms, 2, 2, 1, 1)

        self.TimeNormalx10 = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalx10.setObjectName(u"TimeNormalx10")
        self.TimeNormalx10.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalx10, 2, 1, 1, 1)

        self.TimeNormals = QRadioButton(self.TimeNormalGrid)
        self.TimeNormals.setObjectName(u"TimeNormals")
        self.TimeNormals.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormals, 1, 2, 1, 1)

        self.TimeNormalx1 = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalx1.setObjectName(u"TimeNormalx1")
        self.TimeNormalx1.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalx1, 3, 1, 1, 1)

        self.TimeNormalmicros = QRadioButton(self.TimeNormalGrid)
        self.TimeNormalmicros.setObjectName(u"TimeNormalmicros")
        self.TimeNormalmicros.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormalmicros, 3, 2, 1, 1)

        self.TimeNormal1 = QRadioButton(self.TimeNormalGrid)
        self.TimeNormal1.setObjectName(u"TimeNormal1")
        self.TimeNormal1.setAutoExclusive(False)

        self.gridLayout_8.addWidget(self.TimeNormal1, 3, 0, 1, 1)

        self.tabLockInNormal.addTab(self.TimeConstantNormal, "")
        self.SensitivityNormal = QWidget()
        self.SensitivityNormal.setObjectName(u"SensitivityNormal")
        self.SensNormalSlider = QScrollBar(self.SensitivityNormal)
        self.SensNormalSlider.setObjectName(u"SensNormalSlider")
        self.SensNormalSlider.setGeometry(QRect(0, 0, 20, 142))
        sizePolicy3.setHeightForWidth(self.SensNormalSlider.sizePolicy().hasHeightForWidth())
        self.SensNormalSlider.setSizePolicy(sizePolicy3)
        self.SensNormalSlider.setBaseSize(QSize(20, 142))
        self.SensNormalSlider.setOrientation(Qt.Orientation.Vertical)
        self.SensNormalGrid = QWidget(self.SensitivityNormal)
        self.SensNormalGrid.setObjectName(u"SensNormalGrid")
        self.SensNormalGrid.setGeometry(QRect(26, 0, 185, 142))
        sizePolicy.setHeightForWidth(self.SensNormalGrid.sizePolicy().hasHeightForWidth())
        self.SensNormalGrid.setSizePolicy(sizePolicy)
        self.SensNormalGrid.setBaseSize(QSize(185, 142))
        self.gridLayout_9 = QGridLayout(self.SensNormalGrid)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.SensNormal3 = QRadioButton(self.SensNormalGrid)
        self.SensNormal3.setObjectName(u"SensNormal3")
        self.SensNormal3.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormal3, 2, 0, 1, 1)

        self.SensNormalx100 = QRadioButton(self.SensNormalGrid)
        self.SensNormalx100.setObjectName(u"SensNormalx100")
        self.SensNormalx100.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalx100, 1, 1, 1, 1)

        self.SensNormalV = QRadioButton(self.SensNormalGrid)
        self.SensNormalV.setObjectName(u"SensNormalV")
        self.SensNormalV.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalV, 0, 2, 1, 1)

        self.SensNormalmicroV = QRadioButton(self.SensNormalGrid)
        self.SensNormalmicroV.setObjectName(u"SensNormalmicroV")
        self.SensNormalmicroV.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalmicroV, 2, 2, 1, 1)

        self.SensNormalx10 = QRadioButton(self.SensNormalGrid)
        self.SensNormalx10.setObjectName(u"SensNormalx10")
        self.SensNormalx10.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalx10, 2, 1, 1, 1)

        self.SensNormalmV = QRadioButton(self.SensNormalGrid)
        self.SensNormalmV.setObjectName(u"SensNormalmV")
        self.SensNormalmV.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalmV, 1, 2, 1, 1)

        self.SensNormalx1 = QRadioButton(self.SensNormalGrid)
        self.SensNormalx1.setObjectName(u"SensNormalx1")
        self.SensNormalx1.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalx1, 3, 1, 1, 1)

        self.SensNormalnV = QRadioButton(self.SensNormalGrid)
        self.SensNormalnV.setObjectName(u"SensNormalnV")
        self.SensNormalnV.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormalnV, 3, 2, 1, 1)

        self.SensNormal1 = QRadioButton(self.SensNormalGrid)
        self.SensNormal1.setObjectName(u"SensNormal1")
        self.SensNormal1.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormal1, 3, 0, 1, 1)

        self.SensNormal5 = QRadioButton(self.SensNormalGrid)
        self.SensNormal5.setObjectName(u"SensNormal5")
        self.SensNormal5.setAutoExclusive(False)

        self.gridLayout_9.addWidget(self.SensNormal5, 1, 0, 1, 1)

        self.tabLockInNormal.addTab(self.SensitivityNormal, "")
        self.FrequencyGeneratorNormal = QWidget()
        self.FrequencyGeneratorNormal.setObjectName(u"FrequencyGeneratorNormal")
        self.ExternalFreqGenNormal = QCheckBox(self.FrequencyGeneratorNormal)
        self.ExternalFreqGenNormal.setObjectName(u"ExternalFreqGenNormal")
        self.ExternalFreqGenNormal.setGeometry(QRect(0, 0, 227, 22))
        sizePolicy2.setHeightForWidth(self.ExternalFreqGenNormal.sizePolicy().hasHeightForWidth())
        self.ExternalFreqGenNormal.setSizePolicy(sizePolicy2)
        self.ExternalFreqGenNormal.setBaseSize(QSize(227, 22))
        self.ExternalFreqGenNormal.setChecked(True)
        self.LockInNormalFreqGenSettings = QWidget(self.FrequencyGeneratorNormal)
        self.LockInNormalFreqGenSettings.setObjectName(u"LockInNormalFreqGenSettings")
        self.LockInNormalFreqGenSettings.setGeometry(QRect(0, 22, 227, 136))
        sizePolicy.setHeightForWidth(self.LockInNormalFreqGenSettings.sizePolicy().hasHeightForWidth())
        self.LockInNormalFreqGenSettings.setSizePolicy(sizePolicy)
        self.LockInNormalFreqGenSettings.setBaseSize(QSize(227, 136))
        self.LockInNormalFreqGenAmpFreqFrame = QWidget(self.LockInNormalFreqGenSettings)
        self.LockInNormalFreqGenAmpFreqFrame.setObjectName(u"LockInNormalFreqGenAmpFreqFrame")
        self.LockInNormalFreqGenAmpFreqFrame.setGeometry(QRect(0, 0, 231, 121))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.LockInNormalFreqGenAmpFreqFrame.sizePolicy().hasHeightForWidth())
        self.LockInNormalFreqGenAmpFreqFrame.setSizePolicy(sizePolicy4)
        self.gridLayout_10 = QGridLayout(self.LockInNormalFreqGenAmpFreqFrame)
        self.gridLayout_10.setSpacing(3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(5, 5, 5, 5)
        self.LockInNormalFreqGenAmpFrame = QGroupBox(self.LockInNormalFreqGenAmpFreqFrame)
        self.LockInNormalFreqGenAmpFrame.setObjectName(u"LockInNormalFreqGenAmpFrame")
        self.LockInNormalFreqGenAmpFrame.setEnabled(True)
        self.gridLayout_14 = QGridLayout(self.LockInNormalFreqGenAmpFrame)
        self.gridLayout_14.setSpacing(3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(5, 5, 5, 5)
        self.LockInNormalFreqGenAmplitude = QDoubleSpinBox(self.LockInNormalFreqGenAmpFrame)
        self.LockInNormalFreqGenAmplitude.setObjectName(u"LockInNormalFreqGenAmplitude")
        sizePolicy2.setHeightForWidth(self.LockInNormalFreqGenAmplitude.sizePolicy().hasHeightForWidth())
        self.LockInNormalFreqGenAmplitude.setSizePolicy(sizePolicy2)
        self.LockInNormalFreqGenAmplitude.setDecimals(3)
        self.LockInNormalFreqGenAmplitude.setMinimum(0.006000000000000)
        self.LockInNormalFreqGenAmplitude.setMaximum(10.000000000000000)
        self.LockInNormalFreqGenAmplitude.setSingleStep(0.002000000000000)
        self.LockInNormalFreqGenAmplitude.setValue(0.006000000000000)

        self.gridLayout_14.addWidget(self.LockInNormalFreqGenAmplitude, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.LockInNormalFreqGenAmpFrame, 0, 0, 1, 1)

        self.LockInNormalFreqGenFreqFrame = QGroupBox(self.LockInNormalFreqGenAmpFreqFrame)
        self.LockInNormalFreqGenFreqFrame.setObjectName(u"LockInNormalFreqGenFreqFrame")
        self.LockInNormalFreqGenFreqFrame.setEnabled(False)
        self.gridLayout_15 = QGridLayout(self.LockInNormalFreqGenFreqFrame)
        self.gridLayout_15.setSpacing(3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(5, 5, 5, 5)
        self.LockInNormalFreqGenFrequency = QDoubleSpinBox(self.LockInNormalFreqGenFreqFrame)
        self.LockInNormalFreqGenFrequency.setObjectName(u"LockInNormalFreqGenFrequency")
        self.LockInNormalFreqGenFrequency.setDecimals(2)
        self.LockInNormalFreqGenFrequency.setMaximum(9999.989999999999782)
        self.LockInNormalFreqGenFrequency.setSingleStep(0.002000000000000)
        self.LockInNormalFreqGenFrequency.setValue(800.000000000000000)

        self.gridLayout_15.addWidget(self.LockInNormalFreqGenFrequency, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.LockInNormalFreqGenFreqFrame, 1, 0, 1, 1)

        self.tabLockInNormal.addTab(self.FrequencyGeneratorNormal, "")

        self.gridLayout_2.addWidget(self.tabLockInNormal, 3, 0, 1, 1)

        self.labelLockInNormal = QLabel(self.LockInNormalFrame)
        self.labelLockInNormal.setObjectName(u"labelLockInNormal")
        sizePolicy1.setHeightForWidth(self.labelLockInNormal.sizePolicy().hasHeightForWidth())
        self.labelLockInNormal.setSizePolicy(sizePolicy1)
        self.labelLockInNormal.setMinimumSize(QSize(50, 22))
        self.labelLockInNormal.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.labelLockInNormal, 0, 0, 1, 1)

        self.SNLockInNormalFrame = QFrame(self.LockInNormalFrame)
        self.SNLockInNormalFrame.setObjectName(u"SNLockInNormalFrame")
        sizePolicy1.setHeightForWidth(self.SNLockInNormalFrame.sizePolicy().hasHeightForWidth())
        self.SNLockInNormalFrame.setSizePolicy(sizePolicy1)
        self.SNLockInNormalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SNLockInNormalFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.SNLockInNormalFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labSNLockInNormal = QLabel(self.SNLockInNormalFrame)
        self.labSNLockInNormal.setObjectName(u"labSNLockInNormal")

        self.gridLayout.addWidget(self.labSNLockInNormal, 0, 0, 1, 1)

        self.SNLockInNormal = QLineEdit(self.SNLockInNormalFrame)
        self.SNLockInNormal.setObjectName(u"SNLockInNormal")
        sizePolicy1.setHeightForWidth(self.SNLockInNormal.sizePolicy().hasHeightForWidth())
        self.SNLockInNormal.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.SNLockInNormal, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.SNLockInNormalFrame, 1, 0, 1, 1)

        self.ConnectLockInNormal = QPushButton(self.LockInNormalFrame)
        self.ConnectLockInNormal.setObjectName(u"ConnectLockInNormal")
        sizePolicy2.setHeightForWidth(self.ConnectLockInNormal.sizePolicy().hasHeightForWidth())
        self.ConnectLockInNormal.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.ConnectLockInNormal, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.LockInNormalFrame, 0, 0, 1, 1)

        self.LockInShearFrame = QFrame(self.LockInAmpGroupWidget)
        self.LockInShearFrame.setObjectName(u"LockInShearFrame")
        self.LockInShearFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LockInShearFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.LockInShearFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.labLockInShear = QLabel(self.LockInShearFrame)
        self.labLockInShear.setObjectName(u"labLockInShear")
        sizePolicy1.setHeightForWidth(self.labLockInShear.sizePolicy().hasHeightForWidth())
        self.labLockInShear.setSizePolicy(sizePolicy1)
        self.labLockInShear.setMinimumSize(QSize(50, 22))
        self.labLockInShear.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.labLockInShear, 0, 0, 1, 1)

        self.tabLockInShear = QTabWidget(self.LockInShearFrame)
        self.tabLockInShear.setObjectName(u"tabLockInShear")
        sizePolicy.setHeightForWidth(self.tabLockInShear.sizePolicy().hasHeightForWidth())
        self.tabLockInShear.setSizePolicy(sizePolicy)
        self.TimeConstantShear = QWidget()
        self.TimeConstantShear.setObjectName(u"TimeConstantShear")
        self.TimeShearSlider = QScrollBar(self.TimeConstantShear)
        self.TimeShearSlider.setObjectName(u"TimeShearSlider")
        self.TimeShearSlider.setGeometry(QRect(0, 0, 20, 142))
        sizePolicy3.setHeightForWidth(self.TimeShearSlider.sizePolicy().hasHeightForWidth())
        self.TimeShearSlider.setSizePolicy(sizePolicy3)
        self.TimeShearSlider.setBaseSize(QSize(20, 142))
        self.TimeShearSlider.setOrientation(Qt.Orientation.Vertical)
        self.TimeShearGrid = QWidget(self.TimeConstantShear)
        self.TimeShearGrid.setObjectName(u"TimeShearGrid")
        self.TimeShearGrid.setGeometry(QRect(26, 0, 185, 142))
        sizePolicy.setHeightForWidth(self.TimeShearGrid.sizePolicy().hasHeightForWidth())
        self.TimeShearGrid.setSizePolicy(sizePolicy)
        self.TimeShearGrid.setBaseSize(QSize(185, 142))
        self.gridLayout_6 = QGridLayout(self.TimeShearGrid)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.TimeShear2 = QRadioButton(self.TimeShearGrid)
        self.TimeShear2.setObjectName(u"TimeShear2")
        self.TimeShear2.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShear2, 2, 0, 1, 1)

        self.TimeShearx100 = QRadioButton(self.TimeShearGrid)
        self.TimeShearx100.setObjectName(u"TimeShearx100")
        self.TimeShearx100.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearx100, 1, 1, 1, 1)

        self.TimeShearks = QRadioButton(self.TimeShearGrid)
        self.TimeShearks.setObjectName(u"TimeShearks")
        self.TimeShearks.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearks, 0, 2, 1, 1)

        self.TimeShearms = QRadioButton(self.TimeShearGrid)
        self.TimeShearms.setObjectName(u"TimeShearms")
        self.TimeShearms.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearms, 2, 2, 1, 1)

        self.TimeShearx10 = QRadioButton(self.TimeShearGrid)
        self.TimeShearx10.setObjectName(u"TimeShearx10")
        self.TimeShearx10.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearx10, 2, 1, 1, 1)

        self.TimeShears = QRadioButton(self.TimeShearGrid)
        self.TimeShears.setObjectName(u"TimeShears")
        self.TimeShears.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShears, 1, 2, 1, 1)

        self.TimeShearx1 = QRadioButton(self.TimeShearGrid)
        self.TimeShearx1.setObjectName(u"TimeShearx1")
        self.TimeShearx1.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearx1, 3, 1, 1, 1)

        self.TimeShearmicros = QRadioButton(self.TimeShearGrid)
        self.TimeShearmicros.setObjectName(u"TimeShearmicros")
        self.TimeShearmicros.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShearmicros, 3, 2, 1, 1)

        self.TimeShear1 = QRadioButton(self.TimeShearGrid)
        self.TimeShear1.setObjectName(u"TimeShear1")
        self.TimeShear1.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.TimeShear1, 3, 0, 1, 1)

        self.tabLockInShear.addTab(self.TimeConstantShear, "")
        self.SensitivityShear = QWidget()
        self.SensitivityShear.setObjectName(u"SensitivityShear")
        self.SensShearSlider = QScrollBar(self.SensitivityShear)
        self.SensShearSlider.setObjectName(u"SensShearSlider")
        self.SensShearSlider.setGeometry(QRect(0, 0, 20, 142))
        sizePolicy3.setHeightForWidth(self.SensShearSlider.sizePolicy().hasHeightForWidth())
        self.SensShearSlider.setSizePolicy(sizePolicy3)
        self.SensShearSlider.setBaseSize(QSize(20, 142))
        self.SensShearSlider.setOrientation(Qt.Orientation.Vertical)
        self.SensShearGrid = QWidget(self.SensitivityShear)
        self.SensShearGrid.setObjectName(u"SensShearGrid")
        self.SensShearGrid.setGeometry(QRect(26, 0, 185, 121))
        sizePolicy.setHeightForWidth(self.SensShearGrid.sizePolicy().hasHeightForWidth())
        self.SensShearGrid.setSizePolicy(sizePolicy)
        self.SensShearGrid.setBaseSize(QSize(185, 142))
        self.gridLayout_7 = QGridLayout(self.SensShearGrid)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.SensShear3 = QRadioButton(self.SensShearGrid)
        self.SensShear3.setObjectName(u"SensShear3")
        self.SensShear3.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShear3, 2, 0, 1, 1)

        self.SensShearx100 = QRadioButton(self.SensShearGrid)
        self.SensShearx100.setObjectName(u"SensShearx100")
        self.SensShearx100.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearx100, 1, 1, 1, 1)

        self.SensShearV = QRadioButton(self.SensShearGrid)
        self.SensShearV.setObjectName(u"SensShearV")
        self.SensShearV.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearV, 0, 2, 1, 1)

        self.SensShearmicroV = QRadioButton(self.SensShearGrid)
        self.SensShearmicroV.setObjectName(u"SensShearmicroV")
        self.SensShearmicroV.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearmicroV, 2, 2, 1, 1)

        self.SensShearx10 = QRadioButton(self.SensShearGrid)
        self.SensShearx10.setObjectName(u"SensShearx10")
        self.SensShearx10.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearx10, 2, 1, 1, 1)

        self.SensShearmV = QRadioButton(self.SensShearGrid)
        self.SensShearmV.setObjectName(u"SensShearmV")
        self.SensShearmV.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearmV, 1, 2, 1, 1)

        self.SensShearx1 = QRadioButton(self.SensShearGrid)
        self.SensShearx1.setObjectName(u"SensShearx1")
        self.SensShearx1.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearx1, 3, 1, 1, 1)

        self.SensShearnV = QRadioButton(self.SensShearGrid)
        self.SensShearnV.setObjectName(u"SensShearnV")
        self.SensShearnV.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShearnV, 3, 2, 1, 1)

        self.SensShear1 = QRadioButton(self.SensShearGrid)
        self.SensShear1.setObjectName(u"SensShear1")
        self.SensShear1.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShear1, 3, 0, 1, 1)

        self.SensShear5 = QRadioButton(self.SensShearGrid)
        self.SensShear5.setObjectName(u"SensShear5")
        self.SensShear5.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.SensShear5, 1, 0, 1, 1)

        self.tabLockInShear.addTab(self.SensitivityShear, "")
        self.FrequencyGeneratorShear = QWidget()
        self.FrequencyGeneratorShear.setObjectName(u"FrequencyGeneratorShear")
        self.ExternalFreqGenShear = QCheckBox(self.FrequencyGeneratorShear)
        self.ExternalFreqGenShear.setObjectName(u"ExternalFreqGenShear")
        self.ExternalFreqGenShear.setGeometry(QRect(0, 0, 211, 22))
        sizePolicy2.setHeightForWidth(self.ExternalFreqGenShear.sizePolicy().hasHeightForWidth())
        self.ExternalFreqGenShear.setSizePolicy(sizePolicy2)
        self.ExternalFreqGenShear.setChecked(True)
        self.LockInShearFreqGenAmpFreqFrame = QWidget(self.FrequencyGeneratorShear)
        self.LockInShearFreqGenAmpFreqFrame.setObjectName(u"LockInShearFreqGenAmpFreqFrame")
        self.LockInShearFreqGenAmpFreqFrame.setGeometry(QRect(0, 22, 231, 121))
        sizePolicy.setHeightForWidth(self.LockInShearFreqGenAmpFreqFrame.sizePolicy().hasHeightForWidth())
        self.LockInShearFreqGenAmpFreqFrame.setSizePolicy(sizePolicy)
        self.gridLayout_16 = QGridLayout(self.LockInShearFreqGenAmpFreqFrame)
        self.gridLayout_16.setSpacing(3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(5, 5, 5, 5)
        self.LockInShearFreqGenAmpFrame = QGroupBox(self.LockInShearFreqGenAmpFreqFrame)
        self.LockInShearFreqGenAmpFrame.setObjectName(u"LockInShearFreqGenAmpFrame")
        self.LockInShearFreqGenAmpFrame.setEnabled(True)
        self.LockInShearFreqGenAmpFrame.setAutoFillBackground(False)
        self.LockInShearFreqGenAmpFrame.setFlat(False)
        self.gridLayout_17 = QGridLayout(self.LockInShearFreqGenAmpFrame)
        self.gridLayout_17.setSpacing(3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(5, 5, 5, 5)
        self.LockInShearFreqGenAmplitude = QDoubleSpinBox(self.LockInShearFreqGenAmpFrame)
        self.LockInShearFreqGenAmplitude.setObjectName(u"LockInShearFreqGenAmplitude")
        self.LockInShearFreqGenAmplitude.setReadOnly(False)
        self.LockInShearFreqGenAmplitude.setDecimals(3)
        self.LockInShearFreqGenAmplitude.setMinimum(0.006000000000000)
        self.LockInShearFreqGenAmplitude.setMaximum(10.000000000000000)
        self.LockInShearFreqGenAmplitude.setSingleStep(0.002000000000000)
        self.LockInShearFreqGenAmplitude.setValue(0.006000000000000)

        self.gridLayout_17.addWidget(self.LockInShearFreqGenAmplitude, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.LockInShearFreqGenAmpFrame, 0, 0, 1, 1)

        self.LockInShearFreqGenFrequencyFrame = QGroupBox(self.LockInShearFreqGenAmpFreqFrame)
        self.LockInShearFreqGenFrequencyFrame.setObjectName(u"LockInShearFreqGenFrequencyFrame")
        self.LockInShearFreqGenFrequencyFrame.setEnabled(False)
        self.gridLayout_18 = QGridLayout(self.LockInShearFreqGenFrequencyFrame)
        self.gridLayout_18.setSpacing(3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(5, 5, 5, 5)
        self.LockInShearFreqGenFrequency = QDoubleSpinBox(self.LockInShearFreqGenFrequencyFrame)
        self.LockInShearFreqGenFrequency.setObjectName(u"LockInShearFreqGenFrequency")
        self.LockInShearFreqGenFrequency.setDecimals(2)
        self.LockInShearFreqGenFrequency.setMaximum(9999.989999999999782)
        self.LockInShearFreqGenFrequency.setSingleStep(0.002000000000000)
        self.LockInShearFreqGenFrequency.setValue(452.000000000000000)

        self.gridLayout_18.addWidget(self.LockInShearFreqGenFrequency, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.LockInShearFreqGenFrequencyFrame, 1, 0, 1, 1)

        self.tabLockInShear.addTab(self.FrequencyGeneratorShear, "")

        self.gridLayout_5.addWidget(self.tabLockInShear, 3, 0, 1, 1)

        self.SNLockInShearFrame = QFrame(self.LockInShearFrame)
        self.SNLockInShearFrame.setObjectName(u"SNLockInShearFrame")
        sizePolicy1.setHeightForWidth(self.SNLockInShearFrame.sizePolicy().hasHeightForWidth())
        self.SNLockInShearFrame.setSizePolicy(sizePolicy1)
        self.SNLockInShearFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.SNLockInShearFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.SNLockInShearFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labSNLockInShear = QLabel(self.SNLockInShearFrame)
        self.labSNLockInShear.setObjectName(u"labSNLockInShear")

        self.gridLayout_3.addWidget(self.labSNLockInShear, 0, 0, 1, 1)

        self.SNLockInShear = QLineEdit(self.SNLockInShearFrame)
        self.SNLockInShear.setObjectName(u"SNLockInShear")
        sizePolicy1.setHeightForWidth(self.SNLockInShear.sizePolicy().hasHeightForWidth())
        self.SNLockInShear.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.SNLockInShear, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.SNLockInShearFrame, 1, 0, 1, 1)

        self.ConnectLockInShear = QPushButton(self.LockInShearFrame)
        self.ConnectLockInShear.setObjectName(u"ConnectLockInShear")
        sizePolicy2.setHeightForWidth(self.ConnectLockInShear.sizePolicy().hasHeightForWidth())
        self.ConnectLockInShear.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.ConnectLockInShear, 2, 0, 1, 1)


        self.gridLayout_13.addWidget(self.LockInShearFrame, 1, 0, 1, 1)


        self.HardwareWidgetGrid.addWidget(self.LockInAmpGroup, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuHardware = QMenu(self.menubar)
        self.menuHardware.setObjectName(u"menuHardware")
        self.menuSoftware = QMenu(self.menubar)
        self.menuSoftware.setObjectName(u"menuSoftware")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuHardware.menuAction())
        self.menubar.addAction(self.menuSoftware.menuAction())

        self.retranslateUi(MainWindow)

        self.tabZStageFrame.setCurrentIndex(0)
        self.tabLockInNormal.setCurrentIndex(0)
        self.tabLockInShear.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelFreqGen.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Frequency Generator</span></p></body></html>", None))
        self.FreqGenChan1Box.setTitle(QCoreApplication.translate("MainWindow", u"Normal (Channel 1)", None))
        self.labFreqGenChan1AmpUnit.setText(QCoreApplication.translate("MainWindow", u"Amplitude Unit", None))
        self.FreqGeqChan1Vpp.setText(QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.FreqGeqChan1Vrms.setText(QCoreApplication.translate("MainWindow", u"Vrms", None))
        self.FreqGeqChan1dBm.setText(QCoreApplication.translate("MainWindow", u"dBm", None))
        self.labFreqGenChan1Waveform.setText(QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.FreqGeqChan1Ramp.setText(QCoreApplication.translate("MainWindow", u"Ramp", None))
        self.FreqGeqChan1Sine.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.FreqGeqChan1Square.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.FreqGeqChan1Pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.FreqGenChan1Output.setText(QCoreApplication.translate("MainWindow", u"Output Signal", None))
        self.labFreqGenChan1Amplitude.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.labFreqGenChan1Frequency.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.ConnectFreqGen.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labVISAFreqGen.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>VISA: </p></body></html>", None))
        self.FreqGenChan2Box.setTitle(QCoreApplication.translate("MainWindow", u"Shear (Channel 2)", None))
        self.FreqGenChan2Output.setText(QCoreApplication.translate("MainWindow", u"Output Signal", None))
        self.labFreqGenChan2Waveform.setText(QCoreApplication.translate("MainWindow", u"Waveform", None))
        self.FreqGenChan2Ramp.setText(QCoreApplication.translate("MainWindow", u"Ramp", None))
        self.FreqGeqChan2Sine.setText(QCoreApplication.translate("MainWindow", u"Sine", None))
        self.FreqGenChan2Sqaure.setText(QCoreApplication.translate("MainWindow", u"Square", None))
        self.FreqGenChan2Pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.labFreqGenChan2Frequency.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.labFreqGenChan2Amplitude.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.labFreqGenChan2AmpUnit.setText(QCoreApplication.translate("MainWindow", u"Amplitude Unit", None))
        self.FreqGeqChan2Vpp.setText(QCoreApplication.translate("MainWindow", u"Vpp", None))
        self.FreqGeqChan2Vrms.setText(QCoreApplication.translate("MainWindow", u"Vrms", None))
        self.FreqGeqChan2dBm.setText(QCoreApplication.translate("MainWindow", u"dBm", None))
        self.labPortZStage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Port: </p></body></html>", None))
        self.ConnectZStage.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labelZStage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Pi\u00ebzo Z-Stage Controller</span></p></body></html>", None))
        self.ZStageVButton.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.tabZStageFrame.setTabText(self.tabZStageFrame.indexOf(self.ZStageVolt), QCoreApplication.translate("MainWindow", u"Position", None))
        self.labZStageStepV.setText(QCoreApplication.translate("MainWindow", u"Step Voltage", None))
        self.labZStageMaxV.setText(QCoreApplication.translate("MainWindow", u"Max Voltage", None))
        self.labZStageMinV.setText(QCoreApplication.translate("MainWindow", u"Min Voltage", None))
        self.ZStageCalibrateButton.setText(QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.tabZStageFrame.setTabText(self.tabZStageFrame.indexOf(self.ZStageCalibrate), QCoreApplication.translate("MainWindow", u"Calibrate", None))
        self.labelHeightGauge.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Height Gauge</span></p></body></html>", None))
        self.ConnecHeightGauge.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labHeightGaugePort.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Port: </p></body></html>", None))
        self.HeightGaugeTare.setText(QCoreApplication.translate("MainWindow", u"Tare", None))
        self.HeightGaugeMeasure.setText(QCoreApplication.translate("MainWindow", u"Measure", None))
        self.HeightGaugeResult.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.TimeNormal2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.TimeNormalx100.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.TimeNormalks.setText(QCoreApplication.translate("MainWindow", u"ks", None))
        self.TimeNormalms.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.TimeNormalx10.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.TimeNormals.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.TimeNormalx1.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.TimeNormalmicros.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.TimeNormal1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tabLockInNormal.setTabText(self.tabLockInNormal.indexOf(self.TimeConstantNormal), QCoreApplication.translate("MainWindow", u"Time Constant", None))
        self.SensNormal3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.SensNormalx100.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.SensNormalV.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.SensNormalmicroV.setText(QCoreApplication.translate("MainWindow", u"\u00b5V", None))
        self.SensNormalx10.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.SensNormalmV.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.SensNormalx1.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.SensNormalnV.setText(QCoreApplication.translate("MainWindow", u"nV", None))
        self.SensNormal1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.SensNormal5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tabLockInNormal.setTabText(self.tabLockInNormal.indexOf(self.SensitivityNormal), QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.ExternalFreqGenNormal.setText(QCoreApplication.translate("MainWindow", u"External Frequency Generator", None))
        self.LockInNormalFreqGenAmpFrame.setTitle(QCoreApplication.translate("MainWindow", u"Amplitude (V)", None))
        self.LockInNormalFreqGenFreqFrame.setTitle(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.tabLockInNormal.setTabText(self.tabLockInNormal.indexOf(self.FrequencyGeneratorNormal), QCoreApplication.translate("MainWindow", u"Frequency Generator", None))
        self.labelLockInNormal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Lock-In Amplifier - Normal</span></p></body></html>", None))
        self.labSNLockInNormal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>S/N:</p></body></html>", None))
        self.ConnectLockInNormal.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.labLockInShear.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Lock-In Amplifier - Shear</span></p></body></html>", None))
        self.TimeShear2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.TimeShearx100.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.TimeShearks.setText(QCoreApplication.translate("MainWindow", u"ks", None))
        self.TimeShearms.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.TimeShearx10.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.TimeShears.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.TimeShearx1.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.TimeShearmicros.setText(QCoreApplication.translate("MainWindow", u"\u00b5s", None))
        self.TimeShear1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.tabLockInShear.setTabText(self.tabLockInShear.indexOf(self.TimeConstantShear), QCoreApplication.translate("MainWindow", u"Time Constant", None))
        self.SensShear3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.SensShearx100.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.SensShearV.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.SensShearmicroV.setText(QCoreApplication.translate("MainWindow", u"\u00b5V", None))
        self.SensShearx10.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.SensShearmV.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.SensShearx1.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.SensShearnV.setText(QCoreApplication.translate("MainWindow", u"nV", None))
        self.SensShear1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.SensShear5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tabLockInShear.setTabText(self.tabLockInShear.indexOf(self.SensitivityShear), QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.ExternalFreqGenShear.setText(QCoreApplication.translate("MainWindow", u"External Frequency Generator", None))
        self.LockInShearFreqGenAmpFrame.setTitle(QCoreApplication.translate("MainWindow", u"Amplitude (V)", None))
        self.LockInShearFreqGenFrequencyFrame.setTitle(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.tabLockInShear.setTabText(self.tabLockInShear.indexOf(self.FrequencyGeneratorShear), QCoreApplication.translate("MainWindow", u"Frequency Generator", None))
        self.labSNLockInShear.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>S/N:</p></body></html>", None))
        self.ConnectLockInShear.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.menuHardware.setTitle(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.menuSoftware.setTitle(QCoreApplication.translate("MainWindow", u"Software", None))
    # retranslateUi

