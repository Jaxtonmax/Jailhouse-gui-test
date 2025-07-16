# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acore_runinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ACoreRunInfoWidget(object):
    def setupUi(self, ACoreRunInfoWidget):
        if not ACoreRunInfoWidget.objectName():
            ACoreRunInfoWidget.setObjectName(u"ACoreRunInfoWidget")
        ACoreRunInfoWidget.resize(500, 371)
        self.verticalLayout_2 = QVBoxLayout(ACoreRunInfoWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(ACoreRunInfoWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_msl = QFrame(self.frame_main)
        self.frame_msl.setObjectName(u"frame_msl")
        self.frame_msl.setFrameShape(QFrame.NoFrame)
        self.frame_msl.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_msl)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.lineedit_msl_path = QLineEdit(self.frame_msl)
        self.lineedit_msl_path.setObjectName(u"lineedit_msl_path")

        self.gridLayout_2.addWidget(self.lineedit_msl_path, 2, 1, 1, 1)

        self.lineedit_msl_addr = QLineEdit(self.frame_msl)
        self.lineedit_msl_addr.setObjectName(u"lineedit_msl_addr")

        self.gridLayout_2.addWidget(self.lineedit_msl_addr, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_msl)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_9 = QLabel(self.frame_msl)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label = QLabel(self.frame_msl)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.btn_select_msl = QPushButton(self.frame_msl)
        self.btn_select_msl.setObjectName(u"btn_select_msl")
        self.btn_select_msl.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_select_msl, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_msl)

        self.frame_os = QFrame(self.frame_main)
        self.frame_os.setObjectName(u"frame_os")
        self.frame_os.setFrameShape(QFrame.NoFrame)
        self.frame_os.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_os)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(7, 7, 7, 7)
        self.lineedit_os_path = QLineEdit(self.frame_os)
        self.lineedit_os_path.setObjectName(u"lineedit_os_path")

        self.gridLayout_3.addWidget(self.lineedit_os_path, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_os)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineedit_os_addr = QLineEdit(self.frame_os)
        self.lineedit_os_addr.setObjectName(u"lineedit_os_addr")

        self.gridLayout_3.addWidget(self.lineedit_os_addr, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_os)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_os)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.btn_select_os = QPushButton(self.frame_os)
        self.btn_select_os.setObjectName(u"btn_select_os")
        self.btn_select_os.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_select_os, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_os)

        self.groupbox_app = QGroupBox(self.frame_main)
        self.groupbox_app.setObjectName(u"groupbox_app")
        self.groupbox_app.setFlat(True)
        self.groupbox_app.setCheckable(True)
        self.groupbox_app.setChecked(False)
        self.gridLayout_5 = QGridLayout(self.groupbox_app)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(7, 7, 7, 7)
        self.label_6 = QLabel(self.groupbox_app)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineedit_app_path = QLineEdit(self.groupbox_app)
        self.lineedit_app_path.setObjectName(u"lineedit_app_path")

        self.gridLayout_5.addWidget(self.lineedit_app_path, 1, 1, 1, 1)

        self.label_11 = QLabel(self.groupbox_app)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.lineedit_app_addr = QLineEdit(self.groupbox_app)
        self.lineedit_app_addr.setObjectName(u"lineedit_app_addr")

        self.gridLayout_5.addWidget(self.lineedit_app_addr, 0, 1, 1, 1)

        self.btn_select_app = QPushButton(self.groupbox_app)
        self.btn_select_app.setObjectName(u"btn_select_app")
        self.btn_select_app.setFlat(True)

        self.gridLayout_5.addWidget(self.btn_select_app, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupbox_app)


        self.verticalLayout_2.addWidget(self.frame_main)


        self.retranslateUi(ACoreRunInfoWidget)

        QMetaObject.connectSlotsByName(ACoreRunInfoWidget)
    # setupUi

    def retranslateUi(self, ACoreRunInfoWidget):
        ACoreRunInfoWidget.setWindowTitle(QCoreApplication.translate("ACoreRunInfoWidget", u"Form", None))
        self.lineedit_msl_path.setText("")
        self.lineedit_msl_addr.setText("")
        self.label_4.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u52a0\u8f7d\u5730\u5740\uff1a", None))
        self.label.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"MSL", None))
        self.btn_select_msl.setText("")
        self.lineedit_os_path.setText("")
        self.label_10.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u52a0\u8f7d\u5730\u5740\uff1a", None))
        self.lineedit_os_addr.setText("")
        self.label_5.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"OS", None))
        self.btn_select_os.setText("")
        self.groupbox_app.setTitle(QCoreApplication.translate("ACoreRunInfoWidget", u"APP", None))
        self.label_6.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineedit_app_path.setText("")
        self.label_11.setText(QCoreApplication.translate("ACoreRunInfoWidget", u"\u52a0\u8f7d\u5730\u5740\uff1a", None))
        self.lineedit_app_addr.setText("")
        self.btn_select_app.setText("")
    # retranslateUi

