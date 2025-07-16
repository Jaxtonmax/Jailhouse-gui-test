# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vm_state_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VMStateItemWidget(object):
    def setupUi(self, VMStateItemWidget):
        if not VMStateItemWidget.objectName():
            VMStateItemWidget.setObjectName(u"VMStateItemWidget")
        VMStateItemWidget.resize(378, 50)
        self.verticalLayout = QVBoxLayout(VMStateItemWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(VMStateItemWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout.addWidget(self.label_name)

        self.label_state = QLabel(self.frame)
        self.label_state.setObjectName(u"label_state")

        self.horizontalLayout.addWidget(self.label_state)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(VMStateItemWidget)

        QMetaObject.connectSlotsByName(VMStateItemWidget)
    # setupUi

    def retranslateUi(self, VMStateItemWidget):
        VMStateItemWidget.setWindowTitle(QCoreApplication.translate("VMStateItemWidget", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("VMStateItemWidget", u"#name", None))
        self.label_state.setText(QCoreApplication.translate("VMStateItemWidget", u"#state", None))
    # retranslateUi

