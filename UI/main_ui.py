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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QRadioButton,
    QScrollBar, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.actionLock_In_Amplifiers = QAction(MainWindow)
        self.actionLock_In_Amplifiers.setObjectName(u"actionLock_In_Amplifiers")
        self.actionLock_In_Amplifiers_2 = QAction(MainWindow)
        self.actionLock_In_Amplifiers_2.setObjectName(u"actionLock_In_Amplifiers_2")
        self.actionFunction_Generator = QAction(MainWindow)
        self.actionFunction_Generator.setObjectName(u"actionFunction_Generator")
        self.actionHardware_2 = QAction(MainWindow)
        self.actionHardware_2.setObjectName(u"actionHardware_2")
        self.actionMeasurements = QAction(MainWindow)
        self.actionMeasurements.setObjectName(u"actionMeasurements")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widgetHardware = QWidget(self.centralwidget)
        self.widgetHardware.setObjectName(u"widgetHardware")
        self.widgetHardware.setEnabled(True)
        self.widgetHardware.setGeometry(QRect(0, 0, 800, 546))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetHardware.sizePolicy().hasHeightForWidth())
        self.widgetHardware.setSizePolicy(sizePolicy)
        self.widgetHardware.setMinimumSize(QSize(300, 300))
        self.widgetHardware.setMaximumSize(QSize(16777215, 16777215))
        self.widget = QWidget(self.widgetHardware)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 801, 541))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left = QWidget(self.widget)
        self.Left.setObjectName(u"Left")
        self.Left.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.Left.sizePolicy().hasHeightForWidth())
        self.Left.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget = QWidget(self.Left)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 351, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 289, 22))
        self.label_12.setTextFormat(Qt.TextFormat.AutoText)
        self.tabWidgetNormal = QTabWidget(self.frame_3)
        self.tabWidgetNormal.setObjectName(u"tabWidgetNormal")
        self.tabWidgetNormal.setGeometry(QRect(0, 44, 341, 211))
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.layoutWidget_5 = QWidget(self.tab_7)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 0, 331, 181))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar_5 = QScrollBar(self.layoutWidget_5)
        self.verticalScrollBar_5.setObjectName(u"verticalScrollBar_5")
        self.verticalScrollBar_5.setMinimumSize(QSize(20, 0))
        self.verticalScrollBar_5.setMaximum(19)
        self.verticalScrollBar_5.setPageStep(1)
        self.verticalScrollBar_5.setSliderPosition(0)
        self.verticalScrollBar_5.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBar_5.setInvertedAppearance(False)

        self.horizontalLayout_7.addWidget(self.verticalScrollBar_5)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.radioButton_40 = QRadioButton(self.layoutWidget_5)
        self.radioButton_40.setObjectName(u"radioButton_40")
        self.radioButton_40.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_40, 0, 2, 1, 1)

        self.radioButton_41 = QRadioButton(self.layoutWidget_5)
        self.radioButton_41.setObjectName(u"radioButton_41")
        self.radioButton_41.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_41, 3, 0, 1, 1)

        self.radioButton_42 = QRadioButton(self.layoutWidget_5)
        self.radioButton_42.setObjectName(u"radioButton_42")
        self.radioButton_42.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_42, 3, 2, 1, 1)

        self.radioButton_43 = QRadioButton(self.layoutWidget_5)
        self.radioButton_43.setObjectName(u"radioButton_43")
        self.radioButton_43.setChecked(True)
        self.radioButton_43.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_43, 2, 2, 1, 1)

        self.radioButton_44 = QRadioButton(self.layoutWidget_5)
        self.radioButton_44.setObjectName(u"radioButton_44")
        self.radioButton_44.setChecked(True)
        self.radioButton_44.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_44, 2, 0, 1, 1)

        self.radioButton_45 = QRadioButton(self.layoutWidget_5)
        self.radioButton_45.setObjectName(u"radioButton_45")
        self.radioButton_45.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_45, 1, 1, 1, 1)

        self.radioButton_46 = QRadioButton(self.layoutWidget_5)
        self.radioButton_46.setObjectName(u"radioButton_46")
        self.radioButton_46.setChecked(True)
        self.radioButton_46.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_46, 2, 1, 1, 1)

        self.radioButton_47 = QRadioButton(self.layoutWidget_5)
        self.radioButton_47.setObjectName(u"radioButton_47")
        self.radioButton_47.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_47, 3, 1, 1, 1)

        self.radioButton_48 = QRadioButton(self.layoutWidget_5)
        self.radioButton_48.setObjectName(u"radioButton_48")
        self.radioButton_48.setAutoExclusive(False)

        self.gridLayout_5.addWidget(self.radioButton_48, 1, 2, 1, 1)

        self.gridLayout_5.setColumnMinimumWidth(0, 30)
        self.gridLayout_5.setRowMinimumHeight(0, 20)

        self.horizontalLayout_7.addLayout(self.gridLayout_5)

        self.tabWidgetNormal.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.layoutWidget_6 = QWidget(self.tab_8)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 0, 331, 181))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar_6 = QScrollBar(self.layoutWidget_6)
        self.verticalScrollBar_6.setObjectName(u"verticalScrollBar_6")
        self.verticalScrollBar_6.setMinimumSize(QSize(20, 0))
        self.verticalScrollBar_6.setMaximum(26)
        self.verticalScrollBar_6.setPageStep(1)
        self.verticalScrollBar_6.setSliderPosition(0)
        self.verticalScrollBar_6.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBar_6.setInvertedAppearance(False)

        self.horizontalLayout_8.addWidget(self.verticalScrollBar_6)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.radioButton_49 = QRadioButton(self.layoutWidget_6)
        self.radioButton_49.setObjectName(u"radioButton_49")
        self.radioButton_49.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_49, 0, 2, 1, 1)

        self.radioButton_50 = QRadioButton(self.layoutWidget_6)
        self.radioButton_50.setObjectName(u"radioButton_50")
        self.radioButton_50.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_50, 3, 0, 1, 1)

        self.radioButton_51 = QRadioButton(self.layoutWidget_6)
        self.radioButton_51.setObjectName(u"radioButton_51")
        self.radioButton_51.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_51, 3, 2, 1, 1)

        self.radioButton_52 = QRadioButton(self.layoutWidget_6)
        self.radioButton_52.setObjectName(u"radioButton_52")
        self.radioButton_52.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_52, 2, 2, 1, 1)

        self.radioButton_53 = QRadioButton(self.layoutWidget_6)
        self.radioButton_53.setObjectName(u"radioButton_53")
        self.radioButton_53.setChecked(True)
        self.radioButton_53.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_53, 2, 0, 1, 1)

        self.radioButton_54 = QRadioButton(self.layoutWidget_6)
        self.radioButton_54.setObjectName(u"radioButton_54")
        self.radioButton_54.setChecked(True)
        self.radioButton_54.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_54, 1, 1, 1, 1)

        self.radioButton_55 = QRadioButton(self.layoutWidget_6)
        self.radioButton_55.setObjectName(u"radioButton_55")
        self.radioButton_55.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_55, 2, 1, 1, 1)

        self.radioButton_56 = QRadioButton(self.layoutWidget_6)
        self.radioButton_56.setObjectName(u"radioButton_56")
        self.radioButton_56.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_56, 3, 1, 1, 1)

        self.radioButton_57 = QRadioButton(self.layoutWidget_6)
        self.radioButton_57.setObjectName(u"radioButton_57")
        self.radioButton_57.setChecked(True)
        self.radioButton_57.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_57, 1, 2, 1, 1)

        self.radioButton_58 = QRadioButton(self.layoutWidget_6)
        self.radioButton_58.setObjectName(u"radioButton_58")
        self.radioButton_58.setAutoExclusive(False)

        self.gridLayout_6.addWidget(self.radioButton_58, 1, 0, 1, 1)

        self.gridLayout_6.setColumnMinimumWidth(0, 30)
        self.gridLayout_6.setRowMinimumHeight(0, 20)

        self.horizontalLayout_8.addLayout(self.gridLayout_6)

        self.tabWidgetNormal.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.extRefWaveNormal = QCheckBox(self.tab_9)
        self.extRefWaveNormal.setObjectName(u"extRefWaveNormal")
        self.extRefWaveNormal.setGeometry(QRect(0, 0, 331, 24))
        self.extRefWaveNormal.setChecked(True)
        self.label_13 = QLabel(self.tab_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 30, 100, 16))
        self.ampNormal = QDoubleSpinBox(self.tab_9)
        self.ampNormal.setObjectName(u"ampNormal")
        self.ampNormal.setGeometry(QRect(0, 50, 100, 23))
        self.ampNormal.setDecimals(3)
        self.ampNormal.setMinimum(0.004000000000000)
        self.ampNormal.setMaximum(10.000000000000000)
        self.ampNormal.setSingleStep(0.002000000000000)
        self.ampNormal.setValue(0.004000000000000)
        self.freqNormal = QDoubleSpinBox(self.tab_9)
        self.freqNormal.setObjectName(u"freqNormal")
        self.freqNormal.setGeometry(QRect(0, 100, 100, 23))
        self.freqNormal.setDecimals(3)
        self.freqNormal.setMinimum(0.001000000000000)
        self.freqNormal.setMaximum(3000.000000000000000)
        self.freqNormal.setValue(450.000000000000000)
        self.label_14 = QLabel(self.tab_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 80, 100, 16))
        self.label_15 = QLabel(self.tab_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 130, 100, 16))
        self.phaNormal = QDoubleSpinBox(self.tab_9)
        self.phaNormal.setObjectName(u"phaNormal")
        self.phaNormal.setGeometry(QRect(0, 150, 100, 23))
        self.phaNormal.setDecimals(2)
        self.phaNormal.setMinimum(-180.000000000000000)
        self.phaNormal.setMaximum(179.990000000000009)
        self.phaNormal.setSingleStep(0.010000000000000)
        self.tabWidgetNormal.addTab(self.tab_9, "")
        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(1, 22, 49, 22))
        self.SNlockinNormal = QLineEdit(self.frame_3)
        self.SNlockinNormal.setObjectName(u"SNlockinNormal")
        self.SNlockinNormal.setGeometry(QRect(26, 22, 81, 22))

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.verticalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 289, 22))
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.tabWidgetShear = QTabWidget(self.frame_2)
        self.tabWidgetShear.setObjectName(u"tabWidgetShear")
        self.tabWidgetShear.setGeometry(QRect(0, 44, 341, 211))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 331, 181))
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar = QScrollBar(self.widget1)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setMinimumSize(QSize(20, 0))
        self.verticalScrollBar.setMaximum(19)
        self.verticalScrollBar.setPageStep(1)
        self.verticalScrollBar.setSliderPosition(0)
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)

        self.horizontalLayout_3.addWidget(self.verticalScrollBar)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.radioButton_10 = QRadioButton(self.widget1)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_10, 0, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.widget1)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_5, 3, 2, 1, 1)

        self.radioButton_12 = QRadioButton(self.widget1)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setChecked(True)
        self.radioButton_12.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_12, 2, 2, 1, 1)

        self.radioButton_13 = QRadioButton(self.widget1)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setChecked(True)
        self.radioButton_13.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_13, 2, 0, 1, 1)

        self.radioButton_8 = QRadioButton(self.widget1)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_8, 1, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.widget1)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setChecked(True)
        self.radioButton_7.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_7, 2, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget1)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_6, 3, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.widget1)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setAutoExclusive(False)

        self.gridLayout.addWidget(self.radioButton_11, 1, 2, 1, 1)

        self.gridLayout.setColumnMinimumWidth(0, 30)
        self.gridLayout.setRowMinimumHeight(0, 20)

        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.tabWidgetShear.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget2 = QWidget(self.tab_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 331, 181))
        self.horizontalLayout_4 = QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar_2 = QScrollBar(self.widget2)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setMinimumSize(QSize(20, 0))
        self.verticalScrollBar_2.setMaximum(26)
        self.verticalScrollBar_2.setPageStep(1)
        self.verticalScrollBar_2.setSliderPosition(0)
        self.verticalScrollBar_2.setOrientation(Qt.Orientation.Vertical)
        self.verticalScrollBar_2.setInvertedAppearance(False)

        self.horizontalLayout_4.addWidget(self.verticalScrollBar_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton_14 = QRadioButton(self.widget2)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_14, 0, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.radioButton_9 = QRadioButton(self.widget2)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_9, 3, 2, 1, 1)

        self.radioButton_15 = QRadioButton(self.widget2)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_15, 2, 2, 1, 1)

        self.radioButton_16 = QRadioButton(self.widget2)
        self.radioButton_16.setObjectName(u"radioButton_16")
        self.radioButton_16.setChecked(True)
        self.radioButton_16.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_16, 2, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.widget2)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setChecked(True)
        self.radioButton_17.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_17, 1, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.widget2)
        self.radioButton_18.setObjectName(u"radioButton_18")
        self.radioButton_18.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_18, 2, 1, 1, 1)

        self.radioButton_19 = QRadioButton(self.widget2)
        self.radioButton_19.setObjectName(u"radioButton_19")
        self.radioButton_19.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_19, 3, 1, 1, 1)

        self.radioButton_20 = QRadioButton(self.widget2)
        self.radioButton_20.setObjectName(u"radioButton_20")
        self.radioButton_20.setChecked(True)
        self.radioButton_20.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_20, 1, 2, 1, 1)

        self.radioButton_21 = QRadioButton(self.widget2)
        self.radioButton_21.setObjectName(u"radioButton_21")
        self.radioButton_21.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton_21, 1, 0, 1, 1)

        self.gridLayout_2.setColumnMinimumWidth(0, 30)
        self.gridLayout_2.setRowMinimumHeight(0, 20)

        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidgetShear.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.extRefWaveShear = QCheckBox(self.tab_3)
        self.extRefWaveShear.setObjectName(u"extRefWaveShear")
        self.extRefWaveShear.setGeometry(QRect(0, 0, 331, 24))
        self.extRefWaveShear.setChecked(True)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 30, 100, 16))
        self.ampShear = QDoubleSpinBox(self.tab_3)
        self.ampShear.setObjectName(u"ampShear")
        self.ampShear.setGeometry(QRect(0, 50, 100, 23))
        self.ampShear.setDecimals(3)
        self.ampShear.setMinimum(0.004000000000000)
        self.ampShear.setMaximum(10.000000000000000)
        self.ampShear.setSingleStep(0.002000000000000)
        self.ampShear.setValue(0.004000000000000)
        self.freqShear = QDoubleSpinBox(self.tab_3)
        self.freqShear.setObjectName(u"freqShear")
        self.freqShear.setGeometry(QRect(0, 100, 100, 23))
        self.freqShear.setDecimals(3)
        self.freqShear.setMinimum(0.001000000000000)
        self.freqShear.setMaximum(3000.000000000000000)
        self.freqShear.setValue(450.000000000000000)
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 80, 100, 16))
        self.label_6 = QLabel(self.tab_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 130, 100, 16))
        self.phaShear = QDoubleSpinBox(self.tab_3)
        self.phaShear.setObjectName(u"phaShear")
        self.phaShear.setGeometry(QRect(0, 150, 100, 23))
        self.phaShear.setDecimals(2)
        self.phaShear.setMinimum(-180.000000000000000)
        self.phaShear.setMaximum(179.990000000000009)
        self.phaShear.setSingleStep(0.010000000000000)
        self.tabWidgetShear.addTab(self.tab_3, "")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(1, 22, 49, 22))
        self.SNlockinShear = QLineEdit(self.frame_2)
        self.SNlockinShear.setObjectName(u"SNlockinShear")
        self.SNlockinShear.setGeometry(QRect(26, 22, 81, 22))

        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.Left)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuHardware_2 = QMenu(self.menubar)
        self.menuHardware_2.setObjectName(u"menuHardware_2")
        self.menuMeasurements = QMenu(self.menubar)
        self.menuMeasurements.setObjectName(u"menuMeasurements")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHardware_2.menuAction())
        self.menubar.addAction(self.menuMeasurements.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidgetNormal.setCurrentIndex(2)
        self.tabWidgetShear.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.actionLock_In_Amplifiers.setText(QCoreApplication.translate("MainWindow", u"Lokc-In Amplifiers", None))
        self.actionLock_In_Amplifiers.setIconText(QCoreApplication.translate("MainWindow", u"Lock-In Amplifiers", None))
#if QT_CONFIG(tooltip)
        self.actionLock_In_Amplifiers.setToolTip(QCoreApplication.translate("MainWindow", u"Lock-In Amplifiers", None))
#endif // QT_CONFIG(tooltip)
        self.actionLock_In_Amplifiers_2.setText(QCoreApplication.translate("MainWindow", u"Lock-In Amplifiers", None))
        self.actionFunction_Generator.setText(QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.actionHardware_2.setText(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.actionMeasurements.setText(QCoreApplication.translate("MainWindow", u"Measurements", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Lock-In Amplifer - Normal Mode</span></p></body></html>", None))
        self.radioButton_40.setText(QCoreApplication.translate("MainWindow", u"ks", None))
        self.radioButton_41.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_42.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.radioButton_43.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.radioButton_44.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_45.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.radioButton_46.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.radioButton_47.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.radioButton_48.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.tabWidgetNormal.setTabText(self.tabWidgetNormal.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Time Constant", None))
        self.radioButton_49.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_50.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_51.setText(QCoreApplication.translate("MainWindow", u"nV", None))
        self.radioButton_52.setText(QCoreApplication.translate("MainWindow", u"\u00b5V", None))
        self.radioButton_53.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_54.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.radioButton_55.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.radioButton_56.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.radioButton_57.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.radioButton_58.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tabWidgetNormal.setTabText(self.tabWidgetNormal.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.extRefWaveNormal.setText(QCoreApplication.translate("MainWindow", u"External Reference Wave", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Amplitude (V)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Phase (DEG)", None))
        self.tabWidgetNormal.setTabText(self.tabWidgetNormal.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"S/N:", None))
        self.SNlockinNormal.setText(QCoreApplication.translate("MainWindow", u"A9JSTXTQA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Lock-In Amplifer - Shear Mode</span></p></body></html>", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"ks", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.radioButton_13.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.tabWidgetShear.setTabText(self.tabWidgetShear.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Time Constant", None))
        self.radioButton_14.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"nV", None))
        self.radioButton_15.setText(QCoreApplication.translate("MainWindow", u"\u00b5V", None))
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tabWidgetShear.setTabText(self.tabWidgetShear.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.extRefWaveShear.setText(QCoreApplication.translate("MainWindow", u"External Reference Wave", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amplitude (V)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frequency (Hz)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Phase (DEG)", None))
        self.tabWidgetShear.setTabText(self.tabWidgetShear.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"S/N:", None))
        self.SNlockinShear.setText(QCoreApplication.translate("MainWindow", u"A9TQAG5OA", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuHardware_2.setTitle(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.menuMeasurements.setTitle(QCoreApplication.translate("MainWindow", u"Measurements", None))
    # retranslateUi

