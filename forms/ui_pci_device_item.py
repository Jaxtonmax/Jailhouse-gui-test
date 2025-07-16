# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pci_device_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PCIDeviceItemWidget(object):
    def setupUi(self, PCIDeviceItemWidget):
        if not PCIDeviceItemWidget.objectName():
            PCIDeviceItemWidget.setObjectName(u"PCIDeviceItemWidget")
        PCIDeviceItemWidget.resize(514, 87)
        self.verticalLayout = QVBoxLayout(PCIDeviceItemWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, -1)
        self.frame = QFrame(PCIDeviceItemWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_2.addWidget(self.label_name)

        self.label_path = QLabel(self.frame)
        self.label_path.setObjectName(u"label_path")

        self.verticalLayout_2.addWidget(self.label_path)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(PCIDeviceItemWidget)

        QMetaObject.connectSlotsByName(PCIDeviceItemWidget)
    # setupUi

    def retranslateUi(self, PCIDeviceItemWidget):
        PCIDeviceItemWidget.setWindowTitle(QCoreApplication.translate("PCIDeviceItemWidget", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("PCIDeviceItemWidget", u"USB controller: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1", None))
        self.label_path.setText(QCoreApplication.translate("PCIDeviceItemWidget", u"/sys/bus/pci/devices/0000:03:00.3", None))
    # retranslateUi

