# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_0624_SbIZju.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(240, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFont(font)
        self.topLogo.setStyleSheet(u"background-image: url(:/images/images/images/icon.png);")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(60, 0, 160, 51))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"font: 700 16pt \"Microsoft YaHei UI\";")
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/images/images/images/12.png);\n"
"\n"
"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/images/images/images/11.png);\n"
"\n"
"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font2)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/images/images/images/13.png);\n"
"\n"
"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font2)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/images/images/images/14.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_fun1 = QPushButton(self.topMenu)
        self.btn_fun1.setObjectName(u"btn_fun1")
        sizePolicy.setHeightForWidth(self.btn_fun1.sizePolicy().hasHeightForWidth())
        self.btn_fun1.setSizePolicy(sizePolicy)
        self.btn_fun1.setMinimumSize(QSize(0, 45))
        self.btn_fun1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_fun1.setStyleSheet(u"background-image: url(:/images/images/images/10.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_fun1)

        self.btn_jingdu = QPushButton(self.topMenu)
        self.btn_jingdu.setObjectName(u"btn_jingdu")
        self.btn_jingdu.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_jingdu.sizePolicy().hasHeightForWidth())
        self.btn_jingdu.setSizePolicy(sizePolicy)
        self.btn_jingdu.setMinimumSize(QSize(0, 45))
        self.btn_jingdu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jingdu.setStyleSheet(u"background-image: url(:/images/images/images/15.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_jingdu)

        self.btn_help = QPushButton(self.topMenu)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QSize(0, 45))
        self.btn_help.setFont(font2)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_help.setStyleSheet(u"background-image: url(:/images/images/images/16.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"")

        self.verticalLayout_8.addWidget(self.btn_help)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font2)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(255,255,255);\n"
"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.extraLeftBox.sizePolicy().hasHeightForWidth())
        self.extraLeftBox.setSizePolicy(sizePolicy1)
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setSizeIncrement(QSize(0, 0))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 0, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/images/26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_query_path = QPushButton(self.extraTopMenu)
        self.pushButton_query_path.setObjectName(u"pushButton_query_path")
        sizePolicy.setHeightForWidth(self.pushButton_query_path.sizePolicy().hasHeightForWidth())
        self.pushButton_query_path.setSizePolicy(sizePolicy)
        self.pushButton_query_path.setMinimumSize(QSize(0, 45))
        self.pushButton_query_path.setFont(font2)
        self.pushButton_query_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_query_path.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_query_path.setStyleSheet(u"background-image:url(:/images/images/images/2.png);\n"
"\n"
"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.pushButton_query_path)

        self.pushButton_map_path = QPushButton(self.extraTopMenu)
        self.pushButton_map_path.setObjectName(u"pushButton_map_path")
        sizePolicy.setHeightForWidth(self.pushButton_map_path.sizePolicy().hasHeightForWidth())
        self.pushButton_map_path.setSizePolicy(sizePolicy)
        self.pushButton_map_path.setMinimumSize(QSize(0, 45))
        self.pushButton_map_path.setFont(font2)
        self.pushButton_map_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_map_path.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_map_path.setStyleSheet(u"background-image:url(:/images/images/images/6.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.pushButton_map_path)

        self.pushButton_output_dir = QPushButton(self.extraTopMenu)
        self.pushButton_output_dir.setObjectName(u"pushButton_output_dir")
        sizePolicy.setHeightForWidth(self.pushButton_output_dir.sizePolicy().hasHeightForWidth())
        self.pushButton_output_dir.setSizePolicy(sizePolicy)
        self.pushButton_output_dir.setMinimumSize(QSize(0, 45))
        self.pushButton_output_dir.setFont(font2)
        self.pushButton_output_dir.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_output_dir.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_output_dir.setStyleSheet(u"background-image:url(:/images/images/images/1.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.pushButton_output_dir)

        self.checkBox_display = QCheckBox(self.extraTopMenu)
        self.checkBox_display.setObjectName(u"checkBox_display")
        sizePolicy.setHeightForWidth(self.checkBox_display.sizePolicy().hasHeightForWidth())
        self.checkBox_display.setSizePolicy(sizePolicy)
        self.checkBox_display.setMinimumSize(QSize(0, 45))
        self.checkBox_display.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkBox_display.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color :rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.checkBox_display, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_show_keypoints = QCheckBox(self.extraTopMenu)
        self.checkBox_show_keypoints.setObjectName(u"checkBox_show_keypoints")
        sizePolicy.setHeightForWidth(self.checkBox_show_keypoints.sizePolicy().hasHeightForWidth())
        self.checkBox_show_keypoints.setSizePolicy(sizePolicy)
        self.checkBox_show_keypoints.setMinimumSize(QSize(0, 45))
        self.checkBox_show_keypoints.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.checkBox_show_keypoints, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_jiaozheng = QCheckBox(self.extraTopMenu)
        self.checkBox_jiaozheng.setObjectName(u"checkBox_jiaozheng")
        sizePolicy.setHeightForWidth(self.checkBox_jiaozheng.sizePolicy().hasHeightForWidth())
        self.checkBox_jiaozheng.setSizePolicy(sizePolicy)
        self.checkBox_jiaozheng.setMinimumSize(QSize(0, 45))
        self.checkBox_jiaozheng.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.checkBox_jiaozheng, 0, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_WRITE_RESULT = QCheckBox(self.extraTopMenu)
        self.checkBox_WRITE_RESULT.setObjectName(u"checkBox_WRITE_RESULT")
        sizePolicy.setHeightForWidth(self.checkBox_WRITE_RESULT.sizePolicy().hasHeightForWidth())
        self.checkBox_WRITE_RESULT.setSizePolicy(sizePolicy)
        self.checkBox_WRITE_RESULT.setMinimumSize(QSize(0, 45))
        self.checkBox_WRITE_RESULT.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.checkBox_WRITE_RESULT, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_feature_type = QComboBox(self.extraTopMenu)
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.addItem("")
        self.comboBox_feature_type.setObjectName(u"comboBox_feature_type")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_feature_type.sizePolicy().hasHeightForWidth())
        self.comboBox_feature_type.setSizePolicy(sizePolicy2)
        self.comboBox_feature_type.setFont(font2)
        self.comboBox_feature_type.setAutoFillBackground(False)
        self.comboBox_feature_type.setStyleSheet(u"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);\n"
"color: rgb(112, 112, 112);")
        self.comboBox_feature_type.setIconSize(QSize(16, 16))
        self.comboBox_feature_type.setFrame(True)

        self.verticalLayout_11.addWidget(self.comboBox_feature_type)

        self.run_button = QPushButton(self.extraTopMenu)
        self.run_button.setObjectName(u"run_button")
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setMinimumSize(QSize(0, 45))
        self.run_button.setFont(font2)
        self.run_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.run_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.run_button.setStyleSheet(u"background-image:url(:/images/images/images/8.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.run_button)

        self.pushButton_stop = QPushButton(self.extraTopMenu)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QSize(0, 45))
        self.pushButton_stop.setFont(font2)
        self.pushButton_stop.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_stop.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_stop.setStyleSheet(u"background-image:url(:/images/images/images/5.png);\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_11.addWidget(self.pushButton_stop)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 700 14pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/images/20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/images/19.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/images/21.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/images/images/images/22.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_36 = QVBoxLayout(self.page_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_34.addWidget(self.label_13)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_run_pipei_2 = QPushButton(self.page_2)
        self.pushButton_run_pipei_2.setObjectName(u"pushButton_run_pipei_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_run_pipei_2.sizePolicy().hasHeightForWidth())
        self.pushButton_run_pipei_2.setSizePolicy(sizePolicy5)
        self.pushButton_run_pipei_2.setMinimumSize(QSize(70, 30))
        self.pushButton_run_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_run_pipei_2.setIcon(icon5)

        self.horizontalLayout_22.addWidget(self.pushButton_run_pipei_2)

        self.pushButton_fanhui_pipei_2 = QPushButton(self.page_2)
        self.pushButton_fanhui_pipei_2.setObjectName(u"pushButton_fanhui_pipei_2")
        self.pushButton_fanhui_pipei_2.setMinimumSize(QSize(70, 30))
        self.pushButton_fanhui_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-chevron-double-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_fanhui_pipei_2.setIcon(icon6)

        self.horizontalLayout_22.addWidget(self.pushButton_fanhui_pipei_2)

        self.clear_pipei_2 = QPushButton(self.page_2)
        self.clear_pipei_2.setObjectName(u"clear_pipei_2")
        self.clear_pipei_2.setMinimumSize(QSize(70, 30))
        self.clear_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_pipei_2.setIcon(icon7)

        self.horizontalLayout_22.addWidget(self.clear_pipei_2)

        self.pushButton_save_pipei_2 = QPushButton(self.page_2)
        self.pushButton_save_pipei_2.setObjectName(u"pushButton_save_pipei_2")
        sizePolicy5.setHeightForWidth(self.pushButton_save_pipei_2.sizePolicy().hasHeightForWidth())
        self.pushButton_save_pipei_2.setSizePolicy(sizePolicy5)
        self.pushButton_save_pipei_2.setMinimumSize(QSize(70, 30))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.pushButton_save_pipei_2.setFont(font5)
        self.pushButton_save_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_pipei_2.setIcon(icon8)

        self.horizontalLayout_22.addWidget(self.pushButton_save_pipei_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_8)


        self.verticalLayout_34.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_load_image1_pipei_2 = QPushButton(self.page_2)
        self.pushButton_load_image1_pipei_2.setObjectName(u"pushButton_load_image1_pipei_2")
        sizePolicy2.setHeightForWidth(self.pushButton_load_image1_pipei_2.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image1_pipei_2.setSizePolicy(sizePolicy2)
        self.pushButton_load_image1_pipei_2.setMinimumSize(QSize(146, 30))
        self.pushButton_load_image1_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-image-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_load_image1_pipei_2.setIcon(icon9)

        self.horizontalLayout_23.addWidget(self.pushButton_load_image1_pipei_2)

        self.pushButton_load_image2_pipei_2 = QPushButton(self.page_2)
        self.pushButton_load_image2_pipei_2.setObjectName(u"pushButton_load_image2_pipei_2")
        sizePolicy2.setHeightForWidth(self.pushButton_load_image2_pipei_2.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image2_pipei_2.setSizePolicy(sizePolicy2)
        self.pushButton_load_image2_pipei_2.setMinimumSize(QSize(146, 30))
        self.pushButton_load_image2_pipei_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-image1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_load_image2_pipei_2.setIcon(icon10)

        self.horizontalLayout_23.addWidget(self.pushButton_load_image2_pipei_2)

        self.comboBox_feature_type_pipei_2 = QComboBox(self.page_2)
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.addItem("")
        self.comboBox_feature_type_pipei_2.setObjectName(u"comboBox_feature_type_pipei_2")
        sizePolicy2.setHeightForWidth(self.comboBox_feature_type_pipei_2.sizePolicy().hasHeightForWidth())
        self.comboBox_feature_type_pipei_2.setSizePolicy(sizePolicy2)
        self.comboBox_feature_type_pipei_2.setMinimumSize(QSize(177, 30))
        self.comboBox_feature_type_pipei_2.setMaximumSize(QSize(170, 16777215))
        self.comboBox_feature_type_pipei_2.setFont(font5)
        self.comboBox_feature_type_pipei_2.setAutoFillBackground(False)
        self.comboBox_feature_type_pipei_2.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: #00619a; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}QComboBox {\n"
"    background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"    border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    /*color: #f8f8f2; /* \u5b57\u4f53\u989c\u8272\u4e3a#f8f8f2 */\n"
"    /* padding: 5px; /* \u5185\u8fb9\u8ddd\u4e3a5px */\n"
"    /* padding-left: 10px; /* \u5de6\u4fa7\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"border: 1px solid black;\n"
"       text-align: center;  \n"
"  min-width: 8em;\n"
"     \n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"      background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QComboBox::"
                        "drop-down {\n"
"    subcontrol-origin: padding; /* \u5b50\u63a7\u4ef6\u7684\u539f\u70b9\u76f8\u5bf9\u4e8e\u5185\u8fb9\u8ddd */\n"
"    subcontrol-position: top right; /* \u5b50\u63a7\u4ef6\u7684\u4f4d\u7f6e\u5728\u53f3\u4e0a\u89d2 */\n"
"    width: 25px; /* \u4e0b\u62c9\u6309\u94ae\u7684\u5bbd\u5ea6\u4e3a25px */\n"
"    border-left-width: 0px; /* \u5de6\u4fa7\u8fb9\u6846\u5bbd\u5ea6\u4e3a3px */\n"
"    /*border-left-color: #00619a; /* \u5de6\u4fa7\u8fb9\u6846\u989c\u8272\u4e3a#6272a4 */\n"
"   /* border-left-style: solid; /* \u5de6\u4fa7\u8fb9\u6846\u6837\u5f0f\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 3px; /* \u53f3\u4e0a\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    border-bottom-right-radius: 3px; /* \u53f3\u4e0b\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png); /* \u4e0b\u62c9\u6309\u94ae\u7684\u80cc\u666f\u56fe\u7247 */\n"
"    background-position: center; /* \u80cc\u666f\u56fe\u7247\u5c45\u4e2d */\n"
"    background-repeat:"
                        " no-repeat; /* \u80cc\u666f\u56fe\u7247\u4e0d\u91cd\u590d */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0,0,0); /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a#ff79c6 */\n"
"    background-color:#ffffff; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    padding: 10px; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"    selection-background-color: #6272a4; /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    border:#00619a;\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.comboBox_feature_type_pipei_2.setIconSize(QSize(16, 16))
        self.comboBox_feature_type_pipei_2.setFrame(True)

        self.horizontalLayout_23.addWidget(self.comboBox_feature_type_pipei_2)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)
        self.label_14.setMinimumSize(QSize(150, 30))
        self.label_14.setStyleSheet(u"QLabel {\n"
"background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"\n"
"    border-top-left-radius: 10px; \n"
"    border-bottom-left-radius: 10px; \n"
"    border-top-right-radius: 0px; \n"
"    border-bottom-right-radius: 0px; \n"
"    border: 1px solid black;\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"}\n"
"/*QLabel:hover{ */\n"
"\n"
"   /*background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"/*} */")

        self.horizontalLayout_24.addWidget(self.label_14)

        self.lineEdit_pipei_2 = QLineEdit(self.page_2)
        self.lineEdit_pipei_2.setObjectName(u"lineEdit_pipei_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_pipei_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_pipei_2.setSizePolicy(sizePolicy5)
        self.lineEdit_pipei_2.setMinimumSize(QSize(75, 30))
        self.lineEdit_pipei_2.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_pipei_2.setStyleSheet(u"QLineEdit:hover{\n"
"   background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QLineEdit{    \n"
"  background: #00619a;\n"
"  color:#F0F0F0;\n"
"  border:none;\n"
" border-top-left-radius: 0px; \n"
"    border-bottom-left-radius: 0px; \n"
"    border-top-right-radius:10px; \n"
"    border-bottom-right-radius: 10px; \n"
"font-size: 11pt\n"
"}")

        self.horizontalLayout_24.addWidget(self.lineEdit_pipei_2)

        self.horizontalSpacer_9 = QSpacerItem(600, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)


        self.verticalLayout_34.addLayout(self.horizontalLayout_23)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_pipei_left_2 = QLabel(self.page_2)
        self.label_pipei_left_2.setObjectName(u"label_pipei_left_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_pipei_left_2.sizePolicy().hasHeightForWidth())
        self.label_pipei_left_2.setSizePolicy(sizePolicy6)
        self.label_pipei_left_2.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.horizontalLayout_25.addWidget(self.label_pipei_left_2)

        self.label_pipei_right_2 = QLabel(self.page_2)
        self.label_pipei_right_2.setObjectName(u"label_pipei_right_2")
        sizePolicy6.setHeightForWidth(self.label_pipei_right_2.sizePolicy().hasHeightForWidth())
        self.label_pipei_right_2.setSizePolicy(sizePolicy6)
        self.label_pipei_right_2.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.horizontalLayout_25.addWidget(self.label_pipei_right_2)


        self.verticalLayout_35.addLayout(self.horizontalLayout_25)

        self.label_pipei_result_2 = QLabel(self.page_2)
        self.label_pipei_result_2.setObjectName(u"label_pipei_result_2")
        sizePolicy6.setHeightForWidth(self.label_pipei_result_2.sizePolicy().hasHeightForWidth())
        self.label_pipei_result_2.setSizePolicy(sizePolicy6)
        self.label_pipei_result_2.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.verticalLayout_35.addWidget(self.label_pipei_result_2)

        self.label_pipei_zhuangtai_2 = QLabel(self.page_2)
        self.label_pipei_zhuangtai_2.setObjectName(u"label_pipei_zhuangtai_2")
        self.label_pipei_zhuangtai_2.setStyleSheet(u"")

        self.verticalLayout_35.addWidget(self.label_pipei_zhuangtai_2)


        self.verticalLayout_34.addLayout(self.verticalLayout_35)


        self.verticalLayout_36.addLayout(self.verticalLayout_34)

        self.stackedWidget.addWidget(self.page_2)
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout_31 = QVBoxLayout(self.widgets)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.frame_div_content_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_clear_result = QPushButton(self.frame_div_content_1)
        self.btn_clear_result.setObjectName(u"btn_clear_result")
        sizePolicy5.setHeightForWidth(self.btn_clear_result.sizePolicy().hasHeightForWidth())
        self.btn_clear_result.setSizePolicy(sizePolicy5)
        self.btn_clear_result.setMinimumSize(QSize(70, 30))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.btn_clear_result.setFont(font6)
        self.btn_clear_result.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.btn_clear_result.setIcon(icon7)
        self.btn_clear_result.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.btn_clear_result)

        self.btn_save = QPushButton(self.frame_div_content_1)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy5.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy5)
        self.btn_save.setMinimumSize(QSize(70, 30))
        self.btn_save.setFont(font5)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.btn_save.setIcon(icon8)
        self.btn_save.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.btn_save)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout_31.addWidget(self.row_1)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_result = QTableWidget(self.row_3)
        if (self.tableWidget_result.columnCount() < 5):
            self.tableWidget_result.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_result.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget_result.rowCount() < 27):
            self.tableWidget_result.setRowCount(27)
        brush = QBrush(QColor(0, 0, 0, 0))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255, 0));
        __qtablewidgetitem5.setForeground(brush);
        self.tableWidget_result.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_result.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(10, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(11, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(12, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(13, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(14, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(15, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(16, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(17, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(18, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(19, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(20, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(21, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(22, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(23, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(24, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(25, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(26, __qtablewidgetitem31)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        brush2 = QBrush(QColor(255, 255, 255, 0))
        brush2.setStyle(Qt.NoBrush)
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setBold(True)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font7);
        __qtablewidgetitem32.setBackground(brush2);
        __qtablewidgetitem32.setForeground(brush1);
        self.tableWidget_result.setItem(0, 0, __qtablewidgetitem32)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font7);
        __qtablewidgetitem33.setBackground(brush4);
        __qtablewidgetitem33.setForeground(brush3);
        self.tableWidget_result.setItem(0, 1, __qtablewidgetitem33)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font7);
        __qtablewidgetitem34.setBackground(brush5);
        self.tableWidget_result.setItem(0, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font7);
        self.tableWidget_result.setItem(0, 3, __qtablewidgetitem35)
        font8 = QFont()
        font8.setBold(True)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem36.setFont(font8);
        self.tableWidget_result.setItem(0, 4, __qtablewidgetitem36)
        self.tableWidget_result.setObjectName(u"tableWidget_result")
        sizePolicy6.setHeightForWidth(self.tableWidget_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_result.setSizePolicy(sizePolicy6)
        self.tableWidget_result.setMinimumSize(QSize(240, 0))
        palette = QPalette()
        brush6 = QBrush(QColor(221, 221, 221, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(0, 0, 0, 0))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.tableWidget_result.setPalette(palette)
        self.tableWidget_result.setStyleSheet(u"QTableWidget { color: red; }")
        self.tableWidget_result.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_result.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_result.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_result.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_result.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_result.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_result.setShowGrid(True)
        self.tableWidget_result.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_result.setSortingEnabled(False)
        self.tableWidget_result.horizontalHeader().setVisible(False)
        self.tableWidget_result.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_result.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setVisible(False)
        self.tableWidget_result.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_result.verticalHeader().setHighlightSections(False)
        self.tableWidget_result.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget_result)


        self.verticalLayout_31.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_33 = QVBoxLayout(self.page)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_32.addWidget(self.label_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_jisuan = QPushButton(self.page)
        self.pushButton_jisuan.setObjectName(u"pushButton_jisuan")
        sizePolicy5.setHeightForWidth(self.pushButton_jisuan.sizePolicy().hasHeightForWidth())
        self.pushButton_jisuan.setSizePolicy(sizePolicy5)
        self.pushButton_jisuan.setMinimumSize(QSize(0, 30))
        self.pushButton_jisuan.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-dialpad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_jisuan.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.pushButton_jisuan)

        self.pushButton_real = QPushButton(self.page)
        self.pushButton_real.setObjectName(u"pushButton_real")
        sizePolicy5.setHeightForWidth(self.pushButton_real.sizePolicy().hasHeightForWidth())
        self.pushButton_real.setSizePolicy(sizePolicy5)
        self.pushButton_real.setMinimumSize(QSize(0, 30))
        self.pushButton_real.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_real.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.pushButton_real)

        self.btn_clear_result_jingdu = QPushButton(self.page)
        self.btn_clear_result_jingdu.setObjectName(u"btn_clear_result_jingdu")
        sizePolicy5.setHeightForWidth(self.btn_clear_result_jingdu.sizePolicy().hasHeightForWidth())
        self.btn_clear_result_jingdu.setSizePolicy(sizePolicy5)
        self.btn_clear_result_jingdu.setMinimumSize(QSize(70, 30))
        self.btn_clear_result_jingdu.setFont(font6)
        self.btn_clear_result_jingdu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.btn_clear_result_jingdu.setIcon(icon7)
        self.btn_clear_result_jingdu.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.btn_clear_result_jingdu)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_32.addLayout(self.horizontalLayout_8)

        self.graphicsView = QChartView(self.page)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_32.addWidget(self.graphicsView)


        self.verticalLayout_33.addLayout(self.verticalLayout_32)

        self.stackedWidget.addWidget(self.page)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.horizontalLayout_19 = QHBoxLayout(self.new_page)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_2 = QLabel(self.new_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy7)
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.label_2.setFont(font9)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet(u"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout_19.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.verticalLayout_19.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_19)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_4 = QLabel(self.new_page)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setStyleSheet(u"font: 20pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_20.addWidget(self.label_4)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_map = QLabel(self.new_page)
        self.label_map.setObjectName(u"label_map")
        self.label_map.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(5)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_map.sizePolicy().hasHeightForWidth())
        self.label_map.setSizePolicy(sizePolicy8)
        self.label_map.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.verticalLayout_18.addWidget(self.label_map)

        self.tableWidget_view = QTableWidget(self.new_page)
        if (self.tableWidget_view.columnCount() < 1):
            self.tableWidget_view.setColumnCount(1)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_view.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        if (self.tableWidget_view.rowCount() < 7):
            self.tableWidget_view.setRowCount(7)
        brush11 = QBrush(QColor(0, 0, 0, 0))
        brush11.setStyle(Qt.NoBrush)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem38.setBackground(QColor(255, 255, 255, 0));
        __qtablewidgetitem38.setForeground(brush11);
        self.tableWidget_view.setVerticalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_view.setVerticalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_view.setVerticalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_view.setVerticalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_view.setVerticalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_view.setVerticalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_view.setVerticalHeaderItem(6, __qtablewidgetitem44)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        brush13 = QBrush(QColor(255, 255, 255, 0))
        brush13.setStyle(Qt.NoBrush)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem45.setFont(font7);
        __qtablewidgetitem45.setBackground(brush13);
        __qtablewidgetitem45.setForeground(brush12);
        self.tableWidget_view.setItem(0, 0, __qtablewidgetitem45)
        self.tableWidget_view.setObjectName(u"tableWidget_view")
        sizePolicy3.setHeightForWidth(self.tableWidget_view.sizePolicy().hasHeightForWidth())
        self.tableWidget_view.setSizePolicy(sizePolicy3)
        self.tableWidget_view.setMinimumSize(QSize(0, 0))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.tableWidget_view.setPalette(palette1)
        self.tableWidget_view.setStyleSheet(u"QTableWidget {\n"
"    background-color: #000000; /* \u767d\u8272\u80cc\u666f */\n"
"    border-radius: 5px; /* \u5706\u89d2 */\n"
"    border: 1px solid black; /* \u9ed1\u8272\u7ec6\u7ebf\u8fb9\u6846 */\n"
"    /* gridline-color: black;  \u79fb\u9664\u7f51\u683c\u7ebf\u989c\u8272 */\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #ffffff; /* \u767d\u8272\u80cc\u666f */\n"
"    border-color: black; /* \u8868\u683c\u9879\u8fb9\u6846\u989c\u8272 */\n"
"    /* gridline-color: black; \u79fb\u9664\u8868\u683c\u9879\u7f51\u683c\u7ebf\u989c\u8272 */\n"
"    color: black; /* \u5b57\u4f53\u989c\u8272\u9ed1\u8272 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5b57\u4f53\u4e3a\u5fae\u8f6f\u96c5\u9ed1 */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(149, 183, 193); /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.tableWidget_view.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_view.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_view.setShowGrid(True)
        self.tableWidget_view.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_view.setSortingEnabled(False)
        self.tableWidget_view.horizontalHeader().setVisible(False)
        self.tableWidget_view.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_view.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_view.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_view.verticalHeader().setVisible(False)
        self.tableWidget_view.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_view.verticalHeader().setHighlightSections(False)
        self.tableWidget_view.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_18.addWidget(self.tableWidget_view)

        self.verticalLayout_18.setStretch(0, 9)
        self.verticalLayout_18.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.verticalLayout_18)


        self.horizontalLayout_6.addLayout(self.verticalLayout_20)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.horizontalLayout_19.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.new_page)
        self.page_fun1 = QWidget()
        self.page_fun1.setObjectName(u"page_fun1")
        self.horizontalLayout_21 = QHBoxLayout(self.page_fun1)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_tiqu = QPushButton(self.page_fun1)
        self.pushButton_tiqu.setObjectName(u"pushButton_tiqu")
        self.pushButton_tiqu.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.pushButton_tiqu)

        self.pushButton_pipei = QPushButton(self.page_fun1)
        self.pushButton_pipei.setObjectName(u"pushButton_pipei")
        self.pushButton_pipei.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.pushButton_pipei)

        self.pushButton_video = QPushButton(self.page_fun1)
        self.pushButton_video.setObjectName(u"pushButton_video")
        self.pushButton_video.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.pushButton_video)

        self.pushButton = QPushButton(self.page_fun1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")

        self.verticalLayout_26.addWidget(self.pushButton)

        self.pushButton_forward = QPushButton(self.page_fun1)
        self.pushButton_forward.setObjectName(u"pushButton_forward")
        self.pushButton_forward.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.pushButton_forward)

        self.pushButton_backward = QPushButton(self.page_fun1)
        self.pushButton_backward.setObjectName(u"pushButton_backward")
        self.pushButton_backward.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 20pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_26.addWidget(self.pushButton_backward)


        self.horizontalLayout_20.addLayout(self.verticalLayout_26)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_5 = QLabel(self.page_fun1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_5)

        self.tableWidget_ = QTableWidget(self.page_fun1)
        if (self.tableWidget_.columnCount() < 2):
            self.tableWidget_.setColumnCount(2)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        if (self.tableWidget_.rowCount() < 19):
            self.tableWidget_.setRowCount(19)
        brush15 = QBrush(QColor(0, 0, 0, 0))
        brush15.setStyle(Qt.NoBrush)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem48.setBackground(QColor(255, 255, 255, 0));
        __qtablewidgetitem48.setForeground(brush15);
        self.tableWidget_.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_.setVerticalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(6, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(7, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(9, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(10, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(11, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(12, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(13, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(14, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(15, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(16, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(17, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_.setVerticalHeaderItem(18, __qtablewidgetitem66)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        brush17 = QBrush(QColor(255, 255, 255, 0))
        brush17.setStyle(Qt.NoBrush)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem67.setFont(font7);
        __qtablewidgetitem67.setBackground(brush17);
        __qtablewidgetitem67.setForeground(brush16);
        self.tableWidget_.setItem(0, 0, __qtablewidgetitem67)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        brush19 = QBrush(QColor(255, 255, 255, 255))
        brush19.setStyle(Qt.NoBrush)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem68.setFont(font7);
        __qtablewidgetitem68.setBackground(brush19);
        __qtablewidgetitem68.setForeground(brush18);
        self.tableWidget_.setItem(0, 1, __qtablewidgetitem68)
        self.tableWidget_.setObjectName(u"tableWidget_")
        sizePolicy6.setHeightForWidth(self.tableWidget_.sizePolicy().hasHeightForWidth())
        self.tableWidget_.setSizePolicy(sizePolicy6)
        self.tableWidget_.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        brush21 = QBrush(QColor(0, 0, 0, 255))
        brush21.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush21)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush22)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.tableWidget_.setPalette(palette2)
        self.tableWidget_.setStyleSheet(u"QTableWidget { color: red; }")
        self.tableWidget_.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget_.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_.setShowGrid(True)
        self.tableWidget_.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_.setSortingEnabled(False)
        self.tableWidget_.horizontalHeader().setVisible(False)
        self.tableWidget_.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_.verticalHeader().setVisible(False)
        self.tableWidget_.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_.verticalHeader().setHighlightSections(False)
        self.tableWidget_.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_21.addWidget(self.tableWidget_)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 1)

        self.horizontalLayout_20.addLayout(self.verticalLayout_21)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)

        self.stackedWidget.addWidget(self.page_fun1)
        self.page_tiqu = QWidget()
        self.page_tiqu.setObjectName(u"page_tiqu")
        self.verticalLayout_28 = QVBoxLayout(self.page_tiqu)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_8 = QLabel(self.page_tiqu)
        self.label_8.setObjectName(u"label_8")
        sizePolicy7.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy7)
        self.label_8.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_22.addWidget(self.label_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_run_tiqu = QPushButton(self.page_tiqu)
        self.pushButton_run_tiqu.setObjectName(u"pushButton_run_tiqu")
        sizePolicy5.setHeightForWidth(self.pushButton_run_tiqu.sizePolicy().hasHeightForWidth())
        self.pushButton_run_tiqu.setSizePolicy(sizePolicy5)
        self.pushButton_run_tiqu.setMinimumSize(QSize(70, 30))
        self.pushButton_run_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_run_tiqu.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.pushButton_run_tiqu)

        self.pushButton_fanhui_tiqu = QPushButton(self.page_tiqu)
        self.pushButton_fanhui_tiqu.setObjectName(u"pushButton_fanhui_tiqu")
        sizePolicy5.setHeightForWidth(self.pushButton_fanhui_tiqu.sizePolicy().hasHeightForWidth())
        self.pushButton_fanhui_tiqu.setSizePolicy(sizePolicy5)
        self.pushButton_fanhui_tiqu.setMinimumSize(QSize(70, 30))
        self.pushButton_fanhui_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_fanhui_tiqu.setIcon(icon6)

        self.horizontalLayout_10.addWidget(self.pushButton_fanhui_tiqu)

        self.clear_tiqu = QPushButton(self.page_tiqu)
        self.clear_tiqu.setObjectName(u"clear_tiqu")
        sizePolicy5.setHeightForWidth(self.clear_tiqu.sizePolicy().hasHeightForWidth())
        self.clear_tiqu.setSizePolicy(sizePolicy5)
        self.clear_tiqu.setMinimumSize(QSize(70, 30))
        self.clear_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.clear_tiqu.setIcon(icon7)

        self.horizontalLayout_10.addWidget(self.clear_tiqu)

        self.pushButton_save_tiqu = QPushButton(self.page_tiqu)
        self.pushButton_save_tiqu.setObjectName(u"pushButton_save_tiqu")
        sizePolicy5.setHeightForWidth(self.pushButton_save_tiqu.sizePolicy().hasHeightForWidth())
        self.pushButton_save_tiqu.setSizePolicy(sizePolicy5)
        self.pushButton_save_tiqu.setMinimumSize(QSize(70, 30))
        self.pushButton_save_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_save_tiqu.setIcon(icon8)

        self.horizontalLayout_10.addWidget(self.pushButton_save_tiqu)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_load_image1_tiqu = QPushButton(self.page_tiqu)
        self.pushButton_load_image1_tiqu.setObjectName(u"pushButton_load_image1_tiqu")
        sizePolicy5.setHeightForWidth(self.pushButton_load_image1_tiqu.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image1_tiqu.setSizePolicy(sizePolicy5)
        self.pushButton_load_image1_tiqu.setMinimumSize(QSize(140, 30))
        self.pushButton_load_image1_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_load_image1_tiqu.setIcon(icon9)

        self.horizontalLayout_11.addWidget(self.pushButton_load_image1_tiqu)

        self.pushButton_load_image2_tiqu = QPushButton(self.page_tiqu)
        self.pushButton_load_image2_tiqu.setObjectName(u"pushButton_load_image2_tiqu")
        sizePolicy5.setHeightForWidth(self.pushButton_load_image2_tiqu.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image2_tiqu.setSizePolicy(sizePolicy5)
        self.pushButton_load_image2_tiqu.setMinimumSize(QSize(140, 30))
        self.pushButton_load_image2_tiqu.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_load_image2_tiqu.setIcon(icon10)

        self.horizontalLayout_11.addWidget(self.pushButton_load_image2_tiqu)

        self.comboBox_feature_type_tiqu = QComboBox(self.page_tiqu)
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.addItem("")
        self.comboBox_feature_type_tiqu.setObjectName(u"comboBox_feature_type_tiqu")
        sizePolicy5.setHeightForWidth(self.comboBox_feature_type_tiqu.sizePolicy().hasHeightForWidth())
        self.comboBox_feature_type_tiqu.setSizePolicy(sizePolicy5)
        self.comboBox_feature_type_tiqu.setMinimumSize(QSize(177, 30))
        self.comboBox_feature_type_tiqu.setMaximumSize(QSize(170, 16777215))
        self.comboBox_feature_type_tiqu.setFont(font5)
        self.comboBox_feature_type_tiqu.setAutoFillBackground(False)
        self.comboBox_feature_type_tiqu.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: #00619a; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}QComboBox {\n"
"    background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"    border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    /*color: #f8f8f2; /* \u5b57\u4f53\u989c\u8272\u4e3a#f8f8f2 */\n"
"    /* padding: 5px; /* \u5185\u8fb9\u8ddd\u4e3a5px */\n"
"    /* padding-left: 10px; /* \u5de6\u4fa7\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"border: 1px solid black;\n"
"       text-align: center;  \n"
"  min-width: 8em;\n"
"     \n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"      background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QComboBox::"
                        "drop-down {\n"
"    subcontrol-origin: padding; /* \u5b50\u63a7\u4ef6\u7684\u539f\u70b9\u76f8\u5bf9\u4e8e\u5185\u8fb9\u8ddd */\n"
"    subcontrol-position: top right; /* \u5b50\u63a7\u4ef6\u7684\u4f4d\u7f6e\u5728\u53f3\u4e0a\u89d2 */\n"
"    width: 25px; /* \u4e0b\u62c9\u6309\u94ae\u7684\u5bbd\u5ea6\u4e3a25px */\n"
"    border-left-width: 0px; /* \u5de6\u4fa7\u8fb9\u6846\u5bbd\u5ea6\u4e3a3px */\n"
"    /*border-left-color: #00619a; /* \u5de6\u4fa7\u8fb9\u6846\u989c\u8272\u4e3a#6272a4 */\n"
"   /* border-left-style: solid; /* \u5de6\u4fa7\u8fb9\u6846\u6837\u5f0f\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 3px; /* \u53f3\u4e0a\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    border-bottom-right-radius: 3px; /* \u53f3\u4e0b\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png); /* \u4e0b\u62c9\u6309\u94ae\u7684\u80cc\u666f\u56fe\u7247 */\n"
"    background-position: center; /* \u80cc\u666f\u56fe\u7247\u5c45\u4e2d */\n"
"    background-repeat:"
                        " no-repeat; /* \u80cc\u666f\u56fe\u7247\u4e0d\u91cd\u590d */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0,0,0); /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a#ff79c6 */\n"
"    background-color:#ffffff; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    padding: 10px; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"    selection-background-color: #6272a4; /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    border:#00619a;\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.comboBox_feature_type_tiqu.setIconSize(QSize(16, 16))
        self.comboBox_feature_type_tiqu.setFrame(True)

        self.horizontalLayout_11.addWidget(self.comboBox_feature_type_tiqu)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.page_tiqu)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setMinimumSize(QSize(150, 30))
        self.label_6.setStyleSheet(u"QLabel {\n"
"background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"\n"
"    border-top-left-radius: 10px; \n"
"    border-bottom-left-radius: 10px; \n"
"    border-top-right-radius: 0px; \n"
"    border-bottom-right-radius: 0px; \n"
"    border: 1px solid black;\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"}\n"
"/*QLabel:hover{ */\n"
"\n"
"   /*background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"/*} */")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.lineEdit_tiqu = QLineEdit(self.page_tiqu)
        self.lineEdit_tiqu.setObjectName(u"lineEdit_tiqu")
        sizePolicy5.setHeightForWidth(self.lineEdit_tiqu.sizePolicy().hasHeightForWidth())
        self.lineEdit_tiqu.setSizePolicy(sizePolicy5)
        self.lineEdit_tiqu.setMinimumSize(QSize(75, 30))
        self.lineEdit_tiqu.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_tiqu.setStyleSheet(u"QLineEdit:hover{\n"
"   background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QLineEdit{    \n"
"  background: #00619a;\n"
"  color:#F0F0F0;\n"
"  border:none;\n"
" border-top-left-radius: 0px; \n"
"    border-bottom-left-radius: 0px; \n"
"    border-top-right-radius:10px; \n"
"    border-bottom-right-radius: 10px; \n"
"font-size: 11pt\n"
"}")

        self.horizontalLayout_9.addWidget(self.lineEdit_tiqu)

        self.horizontalSpacer_2 = QSpacerItem(600, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 4)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_22.addLayout(self.horizontalLayout_11)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_tiqu_left = QLabel(self.page_tiqu)
        self.label_tiqu_left.setObjectName(u"label_tiqu_left")
        sizePolicy6.setHeightForWidth(self.label_tiqu_left.sizePolicy().hasHeightForWidth())
        self.label_tiqu_left.setSizePolicy(sizePolicy6)
        self.label_tiqu_left.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.horizontalLayout_13.addWidget(self.label_tiqu_left)

        self.label_tiqu_right = QLabel(self.page_tiqu)
        self.label_tiqu_right.setObjectName(u"label_tiqu_right")
        sizePolicy6.setHeightForWidth(self.label_tiqu_right.sizePolicy().hasHeightForWidth())
        self.label_tiqu_right.setSizePolicy(sizePolicy6)
        self.label_tiqu_right.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.horizontalLayout_13.addWidget(self.label_tiqu_right)


        self.verticalLayout_23.addLayout(self.horizontalLayout_13)

        self.label_tiqu_result = QLabel(self.page_tiqu)
        self.label_tiqu_result.setObjectName(u"label_tiqu_result")
        sizePolicy6.setHeightForWidth(self.label_tiqu_result.sizePolicy().hasHeightForWidth())
        self.label_tiqu_result.setSizePolicy(sizePolicy6)
        self.label_tiqu_result.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.verticalLayout_23.addWidget(self.label_tiqu_result)

        self.label_tiqu_zhuangtai = QLabel(self.page_tiqu)
        self.label_tiqu_zhuangtai.setObjectName(u"label_tiqu_zhuangtai")

        self.verticalLayout_23.addWidget(self.label_tiqu_zhuangtai)


        self.verticalLayout_22.addLayout(self.verticalLayout_23)


        self.verticalLayout_28.addLayout(self.verticalLayout_22)

        self.stackedWidget.addWidget(self.page_tiqu)
        self.page_video = QWidget()
        self.page_video.setObjectName(u"page_video")
        self.verticalLayout_30 = QVBoxLayout(self.page_video)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_12 = QLabel(self.page_video)
        self.label_12.setObjectName(u"label_12")
        sizePolicy7.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy7)
        self.label_12.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_29.addWidget(self.label_12)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_video_run = QPushButton(self.page_video)
        self.pushButton_video_run.setObjectName(u"pushButton_video_run")
        sizePolicy5.setHeightForWidth(self.pushButton_video_run.sizePolicy().hasHeightForWidth())
        self.pushButton_video_run.setSizePolicy(sizePolicy5)
        self.pushButton_video_run.setMinimumSize(QSize(110, 30))
        self.pushButton_video_run.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/images/images/images/17.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_video_run.setIcon(icon13)

        self.horizontalLayout_18.addWidget(self.pushButton_video_run)

        self.btn_exit = QPushButton(self.page_video)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy5.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy5)
        self.btn_exit.setMinimumSize(QSize(110, 30))
        self.btn_exit.setFont(font5)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/images/images/images/18.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon14)

        self.horizontalLayout_18.addWidget(self.btn_exit)

        self.clear_shipin = QPushButton(self.page_video)
        self.clear_shipin.setObjectName(u"clear_shipin")
        sizePolicy5.setHeightForWidth(self.clear_shipin.sizePolicy().hasHeightForWidth())
        self.clear_shipin.setSizePolicy(sizePolicy5)
        self.clear_shipin.setMinimumSize(QSize(70, 30))
        self.clear_shipin.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.clear_shipin.setIcon(icon7)

        self.horizontalLayout_18.addWidget(self.clear_shipin)

        self.pushButton_fanhui_video = QPushButton(self.page_video)
        self.pushButton_fanhui_video.setObjectName(u"pushButton_fanhui_video")
        sizePolicy5.setHeightForWidth(self.pushButton_fanhui_video.sizePolicy().hasHeightForWidth())
        self.pushButton_fanhui_video.setSizePolicy(sizePolicy5)
        self.pushButton_fanhui_video.setMinimumSize(QSize(70, 30))
        self.pushButton_fanhui_video.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_fanhui_video.setIcon(icon6)

        self.horizontalLayout_18.addWidget(self.pushButton_fanhui_video)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_6)


        self.verticalLayout_29.addLayout(self.horizontalLayout_18)

        self.label_video = QLabel(self.page_video)
        self.label_video.setObjectName(u"label_video")
        sizePolicy6.setHeightForWidth(self.label_video.sizePolicy().hasHeightForWidth())
        self.label_video.setSizePolicy(sizePolicy6)
        self.label_video.setMinimumSize(QSize(881, 338))
        self.label_video.setStyleSheet(u"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */\n"
"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;")

        self.verticalLayout_29.addWidget(self.label_video)


        self.verticalLayout_30.addLayout(self.verticalLayout_29)

        self.label_video_zhuangtai = QLabel(self.page_video)
        self.label_video_zhuangtai.setObjectName(u"label_video_zhuangtai")
        sizePolicy3.setHeightForWidth(self.label_video_zhuangtai.sizePolicy().hasHeightForWidth())
        self.label_video_zhuangtai.setSizePolicy(sizePolicy3)
        self.label_video_zhuangtai.setStyleSheet(u"")

        self.verticalLayout_30.addWidget(self.label_video_zhuangtai)

        self.stackedWidget.addWidget(self.page_video)
        self.page_pipei = QWidget()
        self.page_pipei.setObjectName(u"page_pipei")
        self.verticalLayout_27 = QVBoxLayout(self.page_pipei)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_7 = QLabel(self.page_pipei)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")

        self.verticalLayout_25.addWidget(self.label_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_run_pipei = QPushButton(self.page_pipei)
        self.pushButton_run_pipei.setObjectName(u"pushButton_run_pipei")
        sizePolicy5.setHeightForWidth(self.pushButton_run_pipei.sizePolicy().hasHeightForWidth())
        self.pushButton_run_pipei.setSizePolicy(sizePolicy5)
        self.pushButton_run_pipei.setMinimumSize(QSize(70, 30))
        self.pushButton_run_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_run_pipei.setIcon(icon5)

        self.horizontalLayout_15.addWidget(self.pushButton_run_pipei)

        self.pushButton_fanhui_pipei = QPushButton(self.page_pipei)
        self.pushButton_fanhui_pipei.setObjectName(u"pushButton_fanhui_pipei")
        self.pushButton_fanhui_pipei.setMinimumSize(QSize(70, 30))
        self.pushButton_fanhui_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_fanhui_pipei.setIcon(icon6)

        self.horizontalLayout_15.addWidget(self.pushButton_fanhui_pipei)

        self.clear_pipei = QPushButton(self.page_pipei)
        self.clear_pipei.setObjectName(u"clear_pipei")
        self.clear_pipei.setMinimumSize(QSize(70, 30))
        self.clear_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.clear_pipei.setIcon(icon7)

        self.horizontalLayout_15.addWidget(self.clear_pipei)

        self.pushButton_save_pipei = QPushButton(self.page_pipei)
        self.pushButton_save_pipei.setObjectName(u"pushButton_save_pipei")
        sizePolicy5.setHeightForWidth(self.pushButton_save_pipei.sizePolicy().hasHeightForWidth())
        self.pushButton_save_pipei.setSizePolicy(sizePolicy5)
        self.pushButton_save_pipei.setMinimumSize(QSize(70, 30))
        self.pushButton_save_pipei.setFont(font5)
        self.pushButton_save_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_save_pipei.setIcon(icon8)

        self.horizontalLayout_15.addWidget(self.pushButton_save_pipei)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_5)


        self.verticalLayout_25.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_load_image1_pipei = QPushButton(self.page_pipei)
        self.pushButton_load_image1_pipei.setObjectName(u"pushButton_load_image1_pipei")
        sizePolicy2.setHeightForWidth(self.pushButton_load_image1_pipei.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image1_pipei.setSizePolicy(sizePolicy2)
        self.pushButton_load_image1_pipei.setMinimumSize(QSize(146, 30))
        self.pushButton_load_image1_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_load_image1_pipei.setIcon(icon9)

        self.horizontalLayout_16.addWidget(self.pushButton_load_image1_pipei)

        self.pushButton_load_image2_pipei = QPushButton(self.page_pipei)
        self.pushButton_load_image2_pipei.setObjectName(u"pushButton_load_image2_pipei")
        sizePolicy2.setHeightForWidth(self.pushButton_load_image2_pipei.sizePolicy().hasHeightForWidth())
        self.pushButton_load_image2_pipei.setSizePolicy(sizePolicy2)
        self.pushButton_load_image2_pipei.setMinimumSize(QSize(146, 30))
        self.pushButton_load_image2_pipei.setStyleSheet(u"QPushButton {\n"
"    background-color: #00619a; /* \u6df1\u84dd\u8272\u80cc\u666f */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border-radius: 10px;      /* \u5706\u89d2 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    padding: 5px 10px;;       /* \u5185\u8fb9\u8ddd */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    \n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1E2A77; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.pushButton_load_image2_pipei.setIcon(icon10)

        self.horizontalLayout_16.addWidget(self.pushButton_load_image2_pipei)

        self.comboBox_feature_type_pipei = QComboBox(self.page_pipei)
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.addItem("")
        self.comboBox_feature_type_pipei.setObjectName(u"comboBox_feature_type_pipei")
        sizePolicy2.setHeightForWidth(self.comboBox_feature_type_pipei.sizePolicy().hasHeightForWidth())
        self.comboBox_feature_type_pipei.setSizePolicy(sizePolicy2)
        self.comboBox_feature_type_pipei.setMinimumSize(QSize(177, 30))
        self.comboBox_feature_type_pipei.setMaximumSize(QSize(170, 16777215))
        self.comboBox_feature_type_pipei.setFont(font5)
        self.comboBox_feature_type_pipei.setAutoFillBackground(False)
        self.comboBox_feature_type_pipei.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color: #00619a; /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}QComboBox {\n"
"    background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"    border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"    /*color: #f8f8f2; /* \u5b57\u4f53\u989c\u8272\u4e3a#f8f8f2 */\n"
"    /* padding: 5px; /* \u5185\u8fb9\u8ddd\u4e3a5px */\n"
"    /* padding-left: 10px; /* \u5de6\u4fa7\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"border: 1px solid black;\n"
"       text-align: center;  \n"
"  min-width: 8em;\n"
"     \n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"      background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QComboBox::"
                        "drop-down {\n"
"    subcontrol-origin: padding; /* \u5b50\u63a7\u4ef6\u7684\u539f\u70b9\u76f8\u5bf9\u4e8e\u5185\u8fb9\u8ddd */\n"
"    subcontrol-position: top right; /* \u5b50\u63a7\u4ef6\u7684\u4f4d\u7f6e\u5728\u53f3\u4e0a\u89d2 */\n"
"    width: 25px; /* \u4e0b\u62c9\u6309\u94ae\u7684\u5bbd\u5ea6\u4e3a25px */\n"
"    border-left-width: 0px; /* \u5de6\u4fa7\u8fb9\u6846\u5bbd\u5ea6\u4e3a3px */\n"
"    /*border-left-color: #00619a; /* \u5de6\u4fa7\u8fb9\u6846\u989c\u8272\u4e3a#6272a4 */\n"
"   /* border-left-style: solid; /* \u5de6\u4fa7\u8fb9\u6846\u6837\u5f0f\u4e3a\u5b9e\u7ebf */\n"
"    border-top-right-radius: 3px; /* \u53f3\u4e0a\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    border-bottom-right-radius: 3px; /* \u53f3\u4e0b\u89d2\u5706\u89d2\u534a\u5f84\u4e3a3px */\n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png); /* \u4e0b\u62c9\u6309\u94ae\u7684\u80cc\u666f\u56fe\u7247 */\n"
"    background-position: center; /* \u80cc\u666f\u56fe\u7247\u5c45\u4e2d */\n"
"    background-repeat:"
                        " no-repeat; /* \u80cc\u666f\u56fe\u7247\u4e0d\u91cd\u590d */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0,0,0); /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5b57\u4f53\u989c\u8272\u4e3a#ff79c6 */\n"
"    background-color:#ffffff; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    padding: 10px; /* \u4e0b\u62c9\u5217\u8868\u9879\u7684\u5185\u8fb9\u8ddd\u4e3a10px */\n"
"    selection-background-color: #6272a4; /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272\u4e3a#6272a4 */\n"
"    border:#00619a;\n"
"    border: 1px solid black;\n"
"}\n"
"")
        self.comboBox_feature_type_pipei.setIconSize(QSize(16, 16))
        self.comboBox_feature_type_pipei.setFrame(True)

        self.horizontalLayout_16.addWidget(self.comboBox_feature_type_pipei)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_9 = QLabel(self.page_pipei)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)
        self.label_9.setMinimumSize(QSize(150, 30))
        self.label_9.setStyleSheet(u"QLabel {\n"
"background-color: #00619a; /* \u80cc\u666f\u989c\u8272\u4e3a\u6df1\u84dd\u8272 */\n"
"\n"
"    border-top-left-radius: 10px; \n"
"    border-bottom-left-radius: 10px; \n"
"    border-top-right-radius: 0px; \n"
"    border-bottom-right-radius: 0px; \n"
"    border: 1px solid black;\n"
"    color: #F0F0F0;           /* \u6d45\u8272\u5b57\u4f53 */\n"
"    border: none;             /* \u65e0\u8fb9\u6846 */\n"
"    font-size: 11pt;         /* 11\u53f7\u5b57\u4f53 */\n"
"    font-family: 'Microsoft YaHei'; /* \u5fae\u8f6f\u96c5\u9ed1\u5b57\u4f53 */\n"
"}\n"
"/*QLabel:hover{ */\n"
"\n"
"   /*background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"/*} */")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.lineEdit_pipei = QLineEdit(self.page_pipei)
        self.lineEdit_pipei.setObjectName(u"lineEdit_pipei")
        sizePolicy5.setHeightForWidth(self.lineEdit_pipei.sizePolicy().hasHeightForWidth())
        self.lineEdit_pipei.setSizePolicy(sizePolicy5)
        self.lineEdit_pipei.setMinimumSize(QSize(75, 30))
        self.lineEdit_pipei.setMaximumSize(QSize(75, 16777215))
        self.lineEdit_pipei.setStyleSheet(u"QLineEdit:hover{\n"
"   background-color: #59a5f5; /* \u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"QLineEdit{    \n"
"  background: #00619a;\n"
"  color:#F0F0F0;\n"
"  border:none;\n"
" border-top-left-radius: 0px; \n"
"    border-bottom-left-radius: 0px; \n"
"    border-top-right-radius:10px; \n"
"    border-bottom-right-radius: 10px; \n"
"font-size: 11pt\n"
"}")

        self.horizontalLayout_14.addWidget(self.lineEdit_pipei)

        self.horizontalSpacer_4 = QSpacerItem(600, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_14)


        self.verticalLayout_25.addLayout(self.horizontalLayout_16)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_pipei_left = QLabel(self.page_pipei)
        self.label_pipei_left.setObjectName(u"label_pipei_left")
        sizePolicy6.setHeightForWidth(self.label_pipei_left.sizePolicy().hasHeightForWidth())
        self.label_pipei_left.setSizePolicy(sizePolicy6)
        self.label_pipei_left.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.horizontalLayout_17.addWidget(self.label_pipei_left)

        self.label_pipei_right = QLabel(self.page_pipei)
        self.label_pipei_right.setObjectName(u"label_pipei_right")
        sizePolicy6.setHeightForWidth(self.label_pipei_right.sizePolicy().hasHeightForWidth())
        self.label_pipei_right.setSizePolicy(sizePolicy6)
        self.label_pipei_right.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.horizontalLayout_17.addWidget(self.label_pipei_right)


        self.verticalLayout_24.addLayout(self.horizontalLayout_17)

        self.label_pipei_result = QLabel(self.page_pipei)
        self.label_pipei_result.setObjectName(u"label_pipei_result")
        sizePolicy6.setHeightForWidth(self.label_pipei_result.sizePolicy().hasHeightForWidth())
        self.label_pipei_result.setSizePolicy(sizePolicy6)
        self.label_pipei_result.setStyleSheet(u"border: 1.5px solid rgb(56,56,56);\n"
"background-color: white;\n"
"border-radius: 10px; /* \u8fb9\u6846\u5706\u89d2\u534a\u5f84\u4e3a10px */")

        self.verticalLayout_24.addWidget(self.label_pipei_result)

        self.label_pipei_zhuangtai = QLabel(self.page_pipei)
        self.label_pipei_zhuangtai.setObjectName(u"label_pipei_zhuangtai")
        self.label_pipei_zhuangtai.setStyleSheet(u"")

        self.verticalLayout_24.addWidget(self.label_pipei_zhuangtai)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)


        self.verticalLayout_27.addLayout(self.verticalLayout_25)

        self.stackedWidget.addWidget(self.page_pipei)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font2)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/images/images/images/23.png);\n"
"\n"
"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font2)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);background-image: url(:/images/images/images/24.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font2)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"\n"
"font: 700 11pt \"Microsoft YaHei UI\";\n"
"color: rgb(112, 112, 112);background-image: url(:/images/images/images/25.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setBold(False)
        font10.setItalic(False)
        self.creditsLabel.setFont(font10)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_17.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"UAVision", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u754c\u9762", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u4eba\u673a\u667a\u80fd\u89c6\u89c9\u5b9a\u4f4d", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u4eba\u673a\u5b9a\u4f4d\u7ed3\u679c", None))
        self.btn_fun1.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u5de5\u5177\u680f", None))
        self.btn_jingdu.setText(QCoreApplication.translate("MainWindow", u"\u5b9a\u4f4d\u7cbe\u5ea6\u53ef\u89c6\u5316\u8bc4\u4ef7", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u53c2\u6570\u8bbe\u7f6e</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.pushButton_query_path.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u65e0\u4eba\u673a\u5f71\u50cf\u5e93", None))
        self.pushButton_map_path.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u536b\u661f\u56fe\u50cf\u5e93", None))
        self.pushButton_output_dir.setText(
            QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5339\u914d\u7ed3\u679c\u8def\u5f84", None))
        self.checkBox_display.setText(
            QCoreApplication.translate("MainWindow", u"    \u663e\u793a\u5339\u914d\u8fc7\u7a0b             ", None))
        self.checkBox_show_keypoints.setText(
            QCoreApplication.translate("MainWindow", u"    \u663e\u793a\u7279\u5f81\u70b9                 ", None))
        self.checkBox_jiaozheng.setText(
            QCoreApplication.translate("MainWindow", u"    \u5c55\u793a\u5f71\u50cf\u77eb\u6b63\u7ed3\u679c     ",
                                       None))
        self.checkBox_WRITE_RESULT.setText(
            QCoreApplication.translate("MainWindow", u"    \u5bfc\u51fa\u65e0\u4eba\u673a\u5b9a\u4f4d\u7ed3\u679c ",
                                       None))
        self.comboBox_feature_type.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                             u"               \u9009\u62e9\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5",
                                                                             None))
        self.comboBox_feature_type.setItemText(1, QCoreApplication.translate("MainWindow", u"SuperPoint", None))
        self.comboBox_feature_type.setItemText(2, QCoreApplication.translate("MainWindow", u"DISK", None))
        self.comboBox_feature_type.setItemText(3, QCoreApplication.translate("MainWindow", u"ALIKED", None))
        self.comboBox_feature_type.setItemText(4, QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.comboBox_feature_type.setItemText(5, QCoreApplication.translate("MainWindow", u"DoGHardNet", None))

        self.run_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u65e0\u4eba\u673a\u9ad8\u7cbe\u5ea6\u5b9a\u4f4d", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u8fd0\u884c", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u667a\u80fd\u5f71\u50cf\u77eb\u6b63</span></p></body></html>", None))
        self.pushButton_run_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.pushButton_fanhui_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.clear_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_save_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_load_image1_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e00\u5f20\u5f71\u50cf", None))
        self.pushButton_load_image2_pipei_2.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e8c\u5f20\u5f71\u50cf", None))
        self.comboBox_feature_type_pipei_2.setItemText(0, QCoreApplication.translate("MainWindow", u"  \u9009\u62e9\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
        self.comboBox_feature_type_pipei_2.setItemText(1, QCoreApplication.translate("MainWindow", u"SuperPoint", None))
        self.comboBox_feature_type_pipei_2.setItemText(2, QCoreApplication.translate("MainWindow", u"DISK", None))
        self.comboBox_feature_type_pipei_2.setItemText(3, QCoreApplication.translate("MainWindow", u"ALIKED", None))
        self.comboBox_feature_type_pipei_2.setItemText(4, QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.comboBox_feature_type_pipei_2.setItemText(5, QCoreApplication.translate("MainWindow", u"DoGHardNet", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u8f93\u5165\u6700\u5927\u7279\u5f81\u70b9\u6570\uff1a</p></body></html>", None))
        self.label_pipei_left_2.setText("")
        self.label_pipei_right_2.setText("")
        self.label_pipei_result_2.setText("")
        self.label_pipei_zhuangtai_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u65e0\u4eba\u673a\u5b9a\u4f4d\u7ed3\u679c</span></p></body></html>", None))
        self.btn_clear_result.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        ___qtablewidgetitem = self.tableWidget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget_result.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem5 = self.tableWidget_result.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem6 = self.tableWidget_result.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem7 = self.tableWidget_result.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem8 = self.tableWidget_result.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem9 = self.tableWidget_result.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem10 = self.tableWidget_result.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem11 = self.tableWidget_result.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem12 = self.tableWidget_result.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem13 = self.tableWidget_result.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem14 = self.tableWidget_result.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem15 = self.tableWidget_result.verticalHeaderItem(10)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem16 = self.tableWidget_result.verticalHeaderItem(11)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem17 = self.tableWidget_result.verticalHeaderItem(12)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem18 = self.tableWidget_result.verticalHeaderItem(13)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem19 = self.tableWidget_result.verticalHeaderItem(14)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem20 = self.tableWidget_result.verticalHeaderItem(15)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem21 = self.tableWidget_result.verticalHeaderItem(16)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem22 = self.tableWidget_result.verticalHeaderItem(17)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem23 = self.tableWidget_result.verticalHeaderItem(18)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem24 = self.tableWidget_result.verticalHeaderItem(19)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem25 = self.tableWidget_result.verticalHeaderItem(20)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem26 = self.tableWidget_result.verticalHeaderItem(21)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem27 = self.tableWidget_result.verticalHeaderItem(22)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem28 = self.tableWidget_result.verticalHeaderItem(23)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem29 = self.tableWidget_result.verticalHeaderItem(24)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem30 = self.tableWidget_result.verticalHeaderItem(25)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem31 = self.tableWidget_result.verticalHeaderItem(26)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget_result.isSortingEnabled()
        self.tableWidget_result.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.tableWidget_result.item(0, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem33 = self.tableWidget_result.item(0, 1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u5ea6", None));
        ___qtablewidgetitem34 = self.tableWidget_result.item(0, 2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u7eac\u5ea6", None));
        ___qtablewidgetitem35 = self.tableWidget_result.item(0, 3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem36 = self.tableWidget_result.item(0, 4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.tableWidget_result.setSortingEnabled(__sortingEnabled)

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u5b9a\u4f4d\u7cbe\u5ea6\u53ef\u89c6\u5316\u8bc4\u4ef7</span></p></body></html>", None))
        self.pushButton_jisuan.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8ba1\u7b97\u7ed3\u679c", None))
        self.pushButton_real.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u771f\u5b9e\u7ed3\u679c", None))
        self.btn_clear_result_jingdu.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">\u5339\u914d\u8fc7\u7a0b</span></p></body></html>", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#000000;\">\u65e0\u4eba\u673a\u5b9a\u4f4d\u89c6\u56fe</span></p></body></html>", None))
        self.label_map.setText("")
        ___qtablewidgetitem37 = self.tableWidget_view.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem38 = self.tableWidget_view.verticalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem39 = self.tableWidget_view.verticalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem40 = self.tableWidget_view.verticalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem41 = self.tableWidget_view.verticalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem42 = self.tableWidget_view.verticalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem43 = self.tableWidget_view.verticalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem44 = self.tableWidget_view.verticalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled1 = self.tableWidget_view.isSortingEnabled()
        self.tableWidget_view.setSortingEnabled(False)
        ___qtablewidgetitem45 = self.tableWidget_view.item(0, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None));
        self.tableWidget_view.setSortingEnabled(__sortingEnabled1)

        self.pushButton_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u50cf\u7279\u5f81\u63d0\u53d6", None))
        self.pushButton_pipei.setText(QCoreApplication.translate("MainWindow", u"\u5f71\u50cf\u7279\u5f81\u5339\u914d", None))
        self.pushButton_video.setText(QCoreApplication.translate("MainWindow", u"\u6444\u50cf\u5934\u7279\u5f81\u8ddf\u8e2a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u667a\u80fd\u5f71\u50cf\u77eb\u6b63", None))
        self.pushButton_forward.setText(QCoreApplication.translate("MainWindow", u"\u524d\u65b9\u4ea4\u4f1a\u89e3\u7b97", None))
        self.pushButton_backward.setText(QCoreApplication.translate("MainWindow", u"\u540e\u65b9\u4ea4\u4f1a\u89e3\u7b97", None))
        self.label_5.setText("")
        ___qtablewidgetitem46 = self.tableWidget_.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem47 = self.tableWidget_.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem48 = self.tableWidget_.verticalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem49 = self.tableWidget_.verticalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem50 = self.tableWidget_.verticalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem51 = self.tableWidget_.verticalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem52 = self.tableWidget_.verticalHeaderItem(4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem53 = self.tableWidget_.verticalHeaderItem(5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem54 = self.tableWidget_.verticalHeaderItem(6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem55 = self.tableWidget_.verticalHeaderItem(7)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem56 = self.tableWidget_.verticalHeaderItem(8)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem57 = self.tableWidget_.verticalHeaderItem(9)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem58 = self.tableWidget_.verticalHeaderItem(10)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem59 = self.tableWidget_.verticalHeaderItem(11)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem60 = self.tableWidget_.verticalHeaderItem(12)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem61 = self.tableWidget_.verticalHeaderItem(13)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem62 = self.tableWidget_.verticalHeaderItem(14)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem63 = self.tableWidget_.verticalHeaderItem(15)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem64 = self.tableWidget_.verticalHeaderItem(16)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem65 = self.tableWidget_.verticalHeaderItem(17)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));
        ___qtablewidgetitem66 = self.tableWidget_.verticalHeaderItem(18)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled2 = self.tableWidget_.isSortingEnabled()
        self.tableWidget_.setSortingEnabled(False)
        ___qtablewidgetitem67 = self.tableWidget_.item(0, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7b97\u8fc7\u7a0b", None));
        ___qtablewidgetitem68 = self.tableWidget_.item(0, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7b97\u7ed3\u679c", None));
        self.tableWidget_.setSortingEnabled(__sortingEnabled2)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u5f71\u50cf\u7279\u5f81\u63d0\u53d6</span></p></body></html>", None))
        self.pushButton_run_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.pushButton_fanhui_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.clear_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_save_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_load_image1_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e00\u5f20\u5f71\u50cf", None))
        self.pushButton_load_image2_tiqu.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e8c\u5f20\u5f71\u50cf", None))
        self.comboBox_feature_type_tiqu.setItemText(0, QCoreApplication.translate("MainWindow", u"  \u9009\u62e9\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
        self.comboBox_feature_type_tiqu.setItemText(1, QCoreApplication.translate("MainWindow", u"SuperPoint", None))
        self.comboBox_feature_type_tiqu.setItemText(2, QCoreApplication.translate("MainWindow", u"DISK", None))
        self.comboBox_feature_type_tiqu.setItemText(3, QCoreApplication.translate("MainWindow", u"ALIKED", None))
        self.comboBox_feature_type_tiqu.setItemText(4, QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.comboBox_feature_type_tiqu.setItemText(5, QCoreApplication.translate("MainWindow", u"DoGHardNet", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"> \u8f93\u5165\u6700\u5927\u7279\u5f81\u70b9\u6570\uff1a</p></body></html>", None))
        self.label_tiqu_left.setText("")
        self.label_tiqu_right.setText("")
        self.label_tiqu_result.setText("")
        self.label_tiqu_zhuangtai.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u6444\u50cf\u5934\u7279\u5f81\u8ddf\u8e2a</span></p></body></html>", None))
        self.pushButton_video_run.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u6444\u50cf\u5934", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u6444\u50cf\u5934", None))
        self.clear_shipin.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_fanhui_video.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.label_video.setText("")
        self.label_video_zhuangtai.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u5f71\u50cf\u7279\u5f81\u5339\u914d</span></p></body></html>", None))
        self.pushButton_run_pipei.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.pushButton_fanhui_pipei.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.clear_pipei.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_save_pipei.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_load_image1_pipei.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e00\u5f20\u5f71\u50cf", None))
        self.pushButton_load_image2_pipei.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u7b2c\u4e8c\u5f20\u5f71\u50cf", None))
        self.comboBox_feature_type_pipei.setItemText(0, QCoreApplication.translate("MainWindow", u"  \u9009\u62e9\u7279\u5f81\u63d0\u53d6\u7b97\u6cd5", None))
        self.comboBox_feature_type_pipei.setItemText(1, QCoreApplication.translate("MainWindow", u"SuperPoint", None))
        self.comboBox_feature_type_pipei.setItemText(2, QCoreApplication.translate("MainWindow", u"DISK", None))
        self.comboBox_feature_type_pipei.setItemText(3, QCoreApplication.translate("MainWindow", u"ALIKED", None))
        self.comboBox_feature_type_pipei.setItemText(4, QCoreApplication.translate("MainWindow", u"SIFT", None))
        self.comboBox_feature_type_pipei.setItemText(5, QCoreApplication.translate("MainWindow", u"DoGHardNet", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u8f93\u5165\u6700\u5927\u7279\u5f81\u70b9\u6570\uff1a</p></body></html>", None))
        self.label_pipei_left.setText("")
        self.label_pipei_right.setText("")
        self.label_pipei_result.setText("")
        self.label_pipei_zhuangtai.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u610f\u89c1\u53cd\u9988", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u95ee\u5377\u8c03\u67e5", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Yinshusheng", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

