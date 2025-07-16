# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pci_device_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PCIDeviceWidget(object):
    def setupUi(self, PCIDeviceWidget):
        if not PCIDeviceWidget.objectName():
            PCIDeviceWidget.setObjectName(u"PCIDeviceWidget")
        PCIDeviceWidget.resize(629, 713)
        self.verticalLayout = QVBoxLayout(PCIDeviceWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(PCIDeviceWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 607, 691))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_title = QFrame(self.scrollAreaWidgetContents)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy1)
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_title)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.label_name = QLabel(self.frame_title)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_name)

        self.label_path = QLabel(self.frame_title)
        self.label_path.setObjectName(u"label_path")

        self.verticalLayout_3.addWidget(self.label_path)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_infos = QFrame(self.scrollAreaWidgetContents)
        self.frame_infos.setObjectName(u"frame_infos")
        sizePolicy1.setHeightForWidth(self.frame_infos.sizePolicy().hasHeightForWidth())
        self.frame_infos.setSizePolicy(sizePolicy1)
        self.frame_infos.setFrameShape(QFrame.NoFrame)
        self.frame_infos.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_infos)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_bus = QLabel(self.frame_infos)
        self.label_bus.setObjectName(u"label_bus")

        self.gridLayout.addWidget(self.label_bus, 1, 0, 1, 1)

        self.label_device = QLabel(self.frame_infos)
        self.label_device.setObjectName(u"label_device")

        self.gridLayout.addWidget(self.label_device, 2, 0, 1, 1)

        self.label_func = QLabel(self.frame_infos)
        self.label_func.setObjectName(u"label_func")

        self.gridLayout.addWidget(self.label_func, 3, 0, 1, 1)

        self.label_func_value = QLabel(self.frame_infos)
        self.label_func_value.setObjectName(u"label_func_value")

        self.gridLayout.addWidget(self.label_func_value, 3, 1, 1, 1)

        self.label_domain = QLabel(self.frame_infos)
        self.label_domain.setObjectName(u"label_domain")

        self.gridLayout.addWidget(self.label_domain, 0, 0, 1, 1)

        self.label_device_value = QLabel(self.frame_infos)
        self.label_device_value.setObjectName(u"label_device_value")

        self.gridLayout.addWidget(self.label_device_value, 2, 1, 1, 1)

        self.label_domain_value = QLabel(self.frame_infos)
        self.label_domain_value.setObjectName(u"label_domain_value")

        self.gridLayout.addWidget(self.label_domain_value, 0, 1, 1, 1)

        self.label_bus_value = QLabel(self.frame_infos)
        self.label_bus_value.setObjectName(u"label_bus_value")

        self.gridLayout.addWidget(self.label_bus_value, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_infos)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.frame_caps = QFrame(self.scrollAreaWidgetContents)
        self.frame_caps.setObjectName(u"frame_caps")
        self.frame_caps.setFrameShape(QFrame.NoFrame)
        self.frame_caps.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_caps)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_bars = QFrame(self.scrollAreaWidgetContents)
        self.frame_bars.setObjectName(u"frame_bars")
        self.frame_bars.setFrameShape(QFrame.NoFrame)
        self.frame_bars.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_bars)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(PCIDeviceWidget)

        QMetaObject.connectSlotsByName(PCIDeviceWidget)
    # setupUi

    def retranslateUi(self, PCIDeviceWidget):
        PCIDeviceWidget.setWindowTitle(QCoreApplication.translate("PCIDeviceWidget", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("PCIDeviceWidget", u"USB controller: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1", None))
        self.label_path.setText(QCoreApplication.translate("PCIDeviceWidget", u"#path", None))
        self.label_bus.setText(QCoreApplication.translate("PCIDeviceWidget", u"bus", None))
        self.label_device.setText(QCoreApplication.translate("PCIDeviceWidget", u"device", None))
        self.label_func.setText(QCoreApplication.translate("PCIDeviceWidget", u"function", None))
        self.label_func_value.setText(QCoreApplication.translate("PCIDeviceWidget", u"#function", None))
        self.label_domain.setText(QCoreApplication.translate("PCIDeviceWidget", u"domain", None))
        self.label_device_value.setText(QCoreApplication.translate("PCIDeviceWidget", u"#device", None))
        self.label_domain_value.setText(QCoreApplication.translate("PCIDeviceWidget", u"#domain", None))
        self.label_bus_value.setText(QCoreApplication.translate("PCIDeviceWidget", u"#bus", None))
        self.label.setText(QCoreApplication.translate("PCIDeviceWidget", u"Capabilities", None))
        self.label_2.setText(QCoreApplication.translate("PCIDeviceWidget", u"Bars", None))
    # retranslateUi

