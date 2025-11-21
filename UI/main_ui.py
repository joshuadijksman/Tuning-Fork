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
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QRadioButton, QScrollBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 289, 22))

        self.verticalLayout.addWidget(self.frame)

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
        self.tabWidgetShear.setGeometry(QRect(0, 20, 341, 241))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget1 = QWidget(self.tab)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 271, 211))
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

        self.gridLayout.addWidget(self.radioButton_10, 0, 2, 1, 1)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 3, 0, 1, 1)

        self.radioButton_5 = QRadioButton(self.widget1)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.gridLayout.addWidget(self.radioButton_5, 3, 2, 1, 1)

        self.radioButton_12 = QRadioButton(self.widget1)
        self.radioButton_12.setObjectName(u"radioButton_12")

        self.gridLayout.addWidget(self.radioButton_12, 2, 2, 1, 1)

        self.radioButton_13 = QRadioButton(self.widget1)
        self.radioButton_13.setObjectName(u"radioButton_13")

        self.gridLayout.addWidget(self.radioButton_13, 2, 0, 1, 1)

        self.radioButton_8 = QRadioButton(self.widget1)
        self.radioButton_8.setObjectName(u"radioButton_8")

        self.gridLayout.addWidget(self.radioButton_8, 1, 1, 1, 1)

        self.radioButton_7 = QRadioButton(self.widget1)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.gridLayout.addWidget(self.radioButton_7, 2, 1, 1, 1)

        self.radioButton_6 = QRadioButton(self.widget1)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.gridLayout.addWidget(self.radioButton_6, 3, 1, 1, 1)

        self.radioButton_11 = QRadioButton(self.widget1)
        self.radioButton_11.setObjectName(u"radioButton_11")

        self.gridLayout.addWidget(self.radioButton_11, 1, 2, 1, 1)

        self.gridLayout.setColumnMinimumWidth(0, 30)
        self.gridLayout.setRowMinimumHeight(0, 20)

        self.horizontalLayout_3.addLayout(self.gridLayout)

        self.tabWidgetShear.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget2 = QWidget(self.tab_2)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(0, 0, 271, 211))
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

        self.gridLayout_2.addWidget(self.radioButton_14, 0, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.widget2)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_2.addWidget(self.radioButton_3, 3, 0, 1, 1)

        self.radioButton_9 = QRadioButton(self.widget2)
        self.radioButton_9.setObjectName(u"radioButton_9")

        self.gridLayout_2.addWidget(self.radioButton_9, 3, 2, 1, 1)

        self.radioButton_15 = QRadioButton(self.widget2)
        self.radioButton_15.setObjectName(u"radioButton_15")

        self.gridLayout_2.addWidget(self.radioButton_15, 2, 2, 1, 1)

        self.radioButton_16 = QRadioButton(self.widget2)
        self.radioButton_16.setObjectName(u"radioButton_16")

        self.gridLayout_2.addWidget(self.radioButton_16, 2, 0, 1, 1)

        self.radioButton_17 = QRadioButton(self.widget2)
        self.radioButton_17.setObjectName(u"radioButton_17")
        self.radioButton_17.setAutoExclusive(True)

        self.gridLayout_2.addWidget(self.radioButton_17, 1, 1, 1, 1)

        self.radioButton_18 = QRadioButton(self.widget2)
        self.radioButton_18.setObjectName(u"radioButton_18")

        self.gridLayout_2.addWidget(self.radioButton_18, 2, 1, 1, 1)

        self.radioButton_19 = QRadioButton(self.widget2)
        self.radioButton_19.setObjectName(u"radioButton_19")

        self.gridLayout_2.addWidget(self.radioButton_19, 3, 1, 1, 1)

        self.radioButton_20 = QRadioButton(self.widget2)
        self.radioButton_20.setObjectName(u"radioButton_20")

        self.gridLayout_2.addWidget(self.radioButton_20, 1, 2, 1, 1)

        self.radioButton_21 = QRadioButton(self.widget2)
        self.radioButton_21.setObjectName(u"radioButton_21")

        self.gridLayout_2.addWidget(self.radioButton_21, 1, 0, 1, 1)

        self.gridLayout_2.setColumnMinimumWidth(0, 30)
        self.gridLayout_2.setRowMinimumHeight(0, 20)

        self.horizontalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidgetShear.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.checkBox = QCheckBox(self.tab_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(0, 0, 331, 24))
        self.checkBox.setChecked(True)
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 30, 151, 16))
        self.doubleSpinBox = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(0, 50, 84, 23))
        self.doubleSpinBox_2 = QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(0, 100, 84, 23))
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 80, 151, 16))
        self.tabWidgetShear.addTab(self.tab_3, "")

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

        self.tabWidgetShear.setCurrentIndex(1)


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
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Lock-In Amplifer - Normal Mode</span></p></body></html>", None))
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
        self.radioButton_16.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.radioButton_17.setText(QCoreApplication.translate("MainWindow", u"x100", None))
        self.radioButton_18.setText(QCoreApplication.translate("MainWindow", u"x10", None))
        self.radioButton_19.setText(QCoreApplication.translate("MainWindow", u"x1", None))
        self.radioButton_20.setText(QCoreApplication.translate("MainWindow", u"mV", None))
        self.radioButton_21.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.tabWidgetShear.setTabText(self.tabWidgetShear.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"External Reference Wave", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.tabWidgetShear.setTabText(self.tabWidgetShear.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Function Generator", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Home", None))
        self.menuHardware_2.setTitle(QCoreApplication.translate("MainWindow", u"Hardware", None))
        self.menuMeasurements.setTitle(QCoreApplication.translate("MainWindow", u"Measurements", None))
    # retranslateUi

