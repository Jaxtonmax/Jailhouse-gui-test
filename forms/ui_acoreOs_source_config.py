# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acoreOs_source_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_acoreOS(object):
    def setupUi(self, Form_acoreOS):
        if not Form_acoreOS.objectName():
            Form_acoreOS.setObjectName(u"Form_acoreOS")
        Form_acoreOS.resize(532, 489)
        self.verticalLayout = QVBoxLayout(Form_acoreOS)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_cell_name = QComboBox(Form_acoreOS)
        self.comboBox_cell_name.setObjectName(u"comboBox_cell_name")

        self.verticalLayout.addWidget(self.comboBox_cell_name)

        self.frame = QFrame(Form_acoreOS)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(7, 7, 7, 7)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineEdit_select_msl_file = QLineEdit(self.frame)
        self.lineEdit_select_msl_file.setObjectName(u"lineEdit_select_msl_file")

        self.gridLayout.addWidget(self.lineEdit_select_msl_file, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineEdit_msl_run_addr = QLineEdit(self.frame)
        self.lineEdit_msl_run_addr.setObjectName(u"lineEdit_msl_run_addr")

        self.gridLayout.addWidget(self.lineEdit_msl_run_addr, 1, 1, 1, 1)

        self.btn_select_file_1 = QToolButton(self.frame)
        self.btn_select_file_1.setObjectName(u"btn_select_file_1")

        self.gridLayout.addWidget(self.btn_select_file_1, 2, 3, 1, 1)

        self.checkBox_msl = QCheckBox(self.frame)
        self.checkBox_msl.setObjectName(u"checkBox_msl")

        self.gridLayout.addWidget(self.checkBox_msl, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form_acoreOS)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.checkBox_os = QCheckBox(self.frame_2)
        self.checkBox_os.setObjectName(u"checkBox_os")

        self.gridLayout_2.addWidget(self.checkBox_os, 0, 0, 1, 1)

        self.lineEdit_select_os_file = QLineEdit(self.frame_2)
        self.lineEdit_select_os_file.setObjectName(u"lineEdit_select_os_file")

        self.gridLayout_2.addWidget(self.lineEdit_select_os_file, 2, 1, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.lineEdit_os_run_addr = QLineEdit(self.frame_2)
        self.lineEdit_os_run_addr.setObjectName(u"lineEdit_os_run_addr")

        self.gridLayout_2.addWidget(self.lineEdit_os_run_addr, 1, 1, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.btn_select_file_2 = QToolButton(self.frame_2)
        self.btn_select_file_2.setObjectName(u"btn_select_file_2")

        self.gridLayout_2.addWidget(self.btn_select_file_2, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form_acoreOS)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(7, 7, 7, 7)
        self.checkBox_app = QCheckBox(self.frame_3)
        self.checkBox_app.setObjectName(u"checkBox_app")

        self.gridLayout_3.addWidget(self.checkBox_app, 0, 0, 1, 1)

        self.lineEdit_select_app_file = QLineEdit(self.frame_3)
        self.lineEdit_select_app_file.setObjectName(u"lineEdit_select_app_file")

        self.gridLayout_3.addWidget(self.lineEdit_select_app_file, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineEdit_app_run_addr = QLineEdit(self.frame_3)
        self.lineEdit_app_run_addr.setObjectName(u"lineEdit_app_run_addr")

        self.gridLayout_3.addWidget(self.lineEdit_app_run_addr, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.btn_select_file_3 = QToolButton(self.frame_3)
        self.btn_select_file_3.setObjectName(u"btn_select_file_3")

        self.gridLayout_3.addWidget(self.btn_select_file_3, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(Form_acoreOS)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_stop = QPushButton(self.frame_4)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.pushButton_start = QPushButton(self.frame_4)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(Form_acoreOS)

        QMetaObject.connectSlotsByName(Form_acoreOS)
    # setupUi

    def retranslateUi(self, Form_acoreOS):
        Form_acoreOS.setWindowTitle(QCoreApplication.translate("Form_acoreOS", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form_acoreOS", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineEdit_select_msl_file.setText("")
        self.label_8.setText(QCoreApplication.translate("Form_acoreOS", u"\u8fd0\u884c\u5730\u5740\uff1a", None))
        self.lineEdit_msl_run_addr.setText("")
        self.btn_select_file_1.setText(QCoreApplication.translate("Form_acoreOS", u"...", None))
        self.checkBox_msl.setText(QCoreApplication.translate("Form_acoreOS", u"MSL", None))
        self.checkBox_os.setText(QCoreApplication.translate("Form_acoreOS", u"OS", None))
        self.lineEdit_select_os_file.setText("")
        self.label_4.setText(QCoreApplication.translate("Form_acoreOS", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineEdit_os_run_addr.setText("")
        self.label_9.setText(QCoreApplication.translate("Form_acoreOS", u"\u8fd0\u884c\u5730\u5740\uff1a", None))
        self.btn_select_file_2.setText(QCoreApplication.translate("Form_acoreOS", u"...", None))
        self.checkBox_app.setText(QCoreApplication.translate("Form_acoreOS", u"APP", None))
        self.lineEdit_select_app_file.setText("")
        self.label_10.setText(QCoreApplication.translate("Form_acoreOS", u"\u8fd0\u884c\u5730\u5740\uff1a", None))
        self.lineEdit_app_run_addr.setText("")
        self.label_5.setText(QCoreApplication.translate("Form_acoreOS", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.btn_select_file_3.setText(QCoreApplication.translate("Form_acoreOS", u"...", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form_acoreOS", u"\u505c\u6b62", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form_acoreOS", u"\u542f\u52a8", None))
    # retranslateUi

