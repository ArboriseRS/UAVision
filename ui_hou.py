# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'houfang_ui(1)(1)_lENRrq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(624, 294)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_28 = QLabel(Dialog)
        self.label_28.setObjectName(u"label_28")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(24, 0))
        self.label_28.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout_3.addWidget(self.label_28)

        self.label_22 = QLabel(Dialog)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setStyleSheet(u"font: 11pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_3.addWidget(self.label_22)

        self.label_23 = QLabel(Dialog)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setStyleSheet(u"font:  11pt \"Microsoft YaHei UI\";")

        self.horizontalLayout_3.addWidget(self.label_23)

        self.horizontalLayout_3.setStretch(1, 336)
        self.horizontalLayout_3.setStretch(2, 206)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_y1 = QLineEdit(Dialog)
        self.lineEdit_y1.setObjectName(u"lineEdit_y1")

        self.gridLayout.addWidget(self.lineEdit_y1, 0, 10, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.lineEdit_y4 = QLineEdit(Dialog)
        self.lineEdit_y4.setObjectName(u"lineEdit_y4")

        self.gridLayout.addWidget(self.lineEdit_y4, 3, 10, 1, 1)

        self.lineEdit_X1 = QLineEdit(Dialog)
        self.lineEdit_X1.setObjectName(u"lineEdit_X1")

        self.gridLayout.addWidget(self.lineEdit_X1, 0, 2, 1, 1)

        self.label_15 = QLabel(Dialog)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 0, 9, 1, 1)

        self.lineEdit_X2 = QLineEdit(Dialog)
        self.lineEdit_X2.setObjectName(u"lineEdit_X2")

        self.gridLayout.addWidget(self.lineEdit_X2, 1, 2, 1, 1)

        self.lineEdit_Z2 = QLineEdit(Dialog)
        self.lineEdit_Z2.setObjectName(u"lineEdit_Z2")

        self.gridLayout.addWidget(self.lineEdit_Z2, 1, 6, 1, 1)

        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 1, 9, 1, 1)

        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 2, 3, 1, 1)

        self.lineEdit_y2 = QLineEdit(Dialog)
        self.lineEdit_y2.setObjectName(u"lineEdit_y2")

        self.gridLayout.addWidget(self.lineEdit_y2, 1, 10, 1, 1)

        self.lineEdit_y3 = QLineEdit(Dialog)
        self.lineEdit_y3.setObjectName(u"lineEdit_y3")

        self.gridLayout.addWidget(self.lineEdit_y3, 2, 10, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.lineEdit_Z1 = QLineEdit(Dialog)
        self.lineEdit_Z1.setObjectName(u"lineEdit_Z1")

        self.gridLayout.addWidget(self.lineEdit_Z1, 0, 6, 1, 1)

        self.label_18 = QLabel(Dialog)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 9, 1, 1)

        self.lineEdit_x1 = QLineEdit(Dialog)
        self.lineEdit_x1.setObjectName(u"lineEdit_x1")

        self.gridLayout.addWidget(self.lineEdit_x1, 0, 8, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 0, 5, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 7, 1, 1)

        self.lineEdit_x2 = QLineEdit(Dialog)
        self.lineEdit_x2.setObjectName(u"lineEdit_x2")

        self.gridLayout.addWidget(self.lineEdit_x2, 1, 8, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)

        self.lineEdit_X4 = QLineEdit(Dialog)
        self.lineEdit_X4.setObjectName(u"lineEdit_X4")

        self.gridLayout.addWidget(self.lineEdit_X4, 3, 2, 1, 1)

        self.label_12 = QLabel(Dialog)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 1, 3, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)

        self.lineEdit_Z3 = QLineEdit(Dialog)
        self.lineEdit_Z3.setObjectName(u"lineEdit_Z3")

        self.gridLayout.addWidget(self.lineEdit_Z3, 2, 6, 1, 1)

        self.lineEdit_Y4 = QLineEdit(Dialog)
        self.lineEdit_Y4.setObjectName(u"lineEdit_Y4")

        self.gridLayout.addWidget(self.lineEdit_Y4, 3, 4, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 7, 1, 1)

        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 3, 5, 1, 1)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 7, 1, 1)

        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 5, 1, 1)

        self.lineEdit_Y1 = QLineEdit(Dialog)
        self.lineEdit_Y1.setObjectName(u"lineEdit_Y1")

        self.gridLayout.addWidget(self.lineEdit_Y1, 0, 4, 1, 1)

        self.label_17 = QLabel(Dialog)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 2, 9, 1, 1)

        self.lineEdit_x4 = QLineEdit(Dialog)
        self.lineEdit_x4.setObjectName(u"lineEdit_x4")

        self.gridLayout.addWidget(self.lineEdit_x4, 3, 8, 1, 1)

        self.lineEdit_Y3 = QLineEdit(Dialog)
        self.lineEdit_Y3.setObjectName(u"lineEdit_Y3")

        self.gridLayout.addWidget(self.lineEdit_Y3, 2, 4, 1, 1)

        self.lineEdit_x3 = QLineEdit(Dialog)
        self.lineEdit_x3.setObjectName(u"lineEdit_x3")

        self.gridLayout.addWidget(self.lineEdit_x3, 2, 8, 1, 1)

        self.label_14 = QLabel(Dialog)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 3, 3, 1, 1)

        self.lineEdit_Z4 = QLineEdit(Dialog)
        self.lineEdit_Z4.setObjectName(u"lineEdit_Z4")

        self.gridLayout.addWidget(self.lineEdit_Z4, 3, 6, 1, 1)

        self.label_11 = QLabel(Dialog)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 1, 5, 1, 1)

        self.lineEdit_X3 = QLineEdit(Dialog)
        self.lineEdit_X3.setObjectName(u"lineEdit_X3")

        self.gridLayout.addWidget(self.lineEdit_X3, 2, 2, 1, 1)

        self.lineEdit_Y2 = QLineEdit(Dialog)
        self.lineEdit_Y2.setObjectName(u"lineEdit_Y2")

        self.gridLayout.addWidget(self.lineEdit_Y2, 1, 4, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")

        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_26 = QLabel(Dialog)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_27 = QLabel(Dialog)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_21 = QLabel(Dialog)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 9pt \"Microsoft YaHei UI\";")

        self.horizontalLayout.addWidget(self.label_21)

        self.lineEdit_f = QLineEdit(Dialog)
        self.lineEdit_f.setObjectName(u"lineEdit_f")

        self.horizontalLayout.addWidget(self.lineEdit_f)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_load_houfang = QPushButton(Dialog)
        self.pushButton_load_houfang.setObjectName(u"pushButton_load_houfang")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_load_houfang.sizePolicy().hasHeightForWidth())
        self.pushButton_load_houfang.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_load_houfang)

        self.pushButton_run = QPushButton(Dialog)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy2.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_run)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_28.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"> \u5730\u9762\u70b9\u5750\u6807(X,Y,Z)</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u50cf\u70b9\u5750\u6807(x,y)</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"X 4", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"y 1", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"y 2", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Y 3", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"X 1", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"y 4", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"X 2", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Z 1", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"x 1", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"X 3", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Y 2", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"x 3", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"x 4", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Z 4", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"x 2", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Z 3", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"y 3", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Y 4", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Z 2", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Y 1", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"\u70b9\u2460", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"\u70b9\u2461", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"\u70b9\u2462", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"\u70b9\u2463", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u6444\u50cf\u673a\u4e3b\u8ddd f", None))
        self.pushButton_load_houfang.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u6587\u4ef6", None))
        self.pushButton_run.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi

