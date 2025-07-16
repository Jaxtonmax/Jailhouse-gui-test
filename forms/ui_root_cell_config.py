# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'root_cell_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_root(object):
    def setupUi(self, Form_root):
        if not Form_root.objectName():
            Form_root.setObjectName(u"Form_root")
        Form_root.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form_root)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 7, 7)
        self.frame_2 = QFrame(Form_root)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Form_root)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_stop = QPushButton(self.frame)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.pushButton_start = QPushButton(self.frame)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form_root)

        QMetaObject.connectSlotsByName(Form_root)
    # setupUi

    def retranslateUi(self, Form_root):
        Form_root.setWindowTitle(QCoreApplication.translate("Form_root", u"Form", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form_root", u"\u9500\u6bc1", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form_root", u"\u542f\u52a8", None))
    # retranslateUi

