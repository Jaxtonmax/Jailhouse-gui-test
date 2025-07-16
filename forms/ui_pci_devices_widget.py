# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pci_devices_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PCIDevicesWidget(object):
    def setupUi(self, PCIDevicesWidget):
        if not PCIDevicesWidget.objectName():
            PCIDevicesWidget.setObjectName(u"PCIDevicesWidget")
        PCIDevicesWidget.resize(1002, 622)
        self.verticalLayout_6 = QVBoxLayout(PCIDevicesWidget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(PCIDevicesWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setFrameShape(QFrame.NoFrame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 1002, 622))
        self.scrollarea_content.setAutoFillBackground(True)
        self.verticalLayout_2 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_pci_device = QFrame(self.frame_left)
        self.frame_pci_device.setObjectName(u"frame_pci_device")
        self.frame_pci_device.setFrameShape(QFrame.NoFrame)
        self.frame_pci_device.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_pci_device)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_pci_device_title = QFrame(self.frame_pci_device)
        self.frame_pci_device_title.setObjectName(u"frame_pci_device_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_pci_device_title.sizePolicy().hasHeightForWidth())
        self.frame_pci_device_title.setSizePolicy(sizePolicy)
        self.frame_pci_device_title.setFrameShape(QFrame.NoFrame)
        self.frame_pci_device_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_pci_device_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_pci_device = QLabel(self.frame_pci_device_title)
        self.label_pci_device.setObjectName(u"label_pci_device")

        self.horizontalLayout_3.addWidget(self.label_pci_device)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_update = QPushButton(self.frame_pci_device_title)
        self.btn_update.setObjectName(u"btn_update")

        self.horizontalLayout_3.addWidget(self.btn_update)


        self.verticalLayout.addWidget(self.frame_pci_device_title)

        self.frame_content = QFrame(self.frame_pci_device)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listwidget_pci_devices = QListWidget(self.frame_content)
        self.listwidget_pci_devices.setObjectName(u"listwidget_pci_devices")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listwidget_pci_devices.sizePolicy().hasHeightForWidth())
        self.listwidget_pci_devices.setSizePolicy(sizePolicy1)
        self.listwidget_pci_devices.setAlternatingRowColors(True)

        self.verticalLayout_3.addWidget(self.listwidget_pci_devices)


        self.verticalLayout.addWidget(self.frame_content)


        self.verticalLayout_4.addWidget(self.frame_pci_device)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        sizePolicy1.setHeightForWidth(self.frame_right.sizePolicy().hasHeightForWidth())
        self.frame_right.setSizePolicy(sizePolicy1)
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_right)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_pcidevice_info = QFrame(self.frame_right)
        self.frame_pcidevice_info.setObjectName(u"frame_pcidevice_info")
        self.frame_pcidevice_info.setFrameShape(QFrame.NoFrame)
        self.frame_pcidevice_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_pcidevice_info)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_pcidevice_info_title = QFrame(self.frame_pcidevice_info)
        self.frame_pcidevice_info_title.setObjectName(u"frame_pcidevice_info_title")
        sizePolicy.setHeightForWidth(self.frame_pcidevice_info_title.sizePolicy().hasHeightForWidth())
        self.frame_pcidevice_info_title.setSizePolicy(sizePolicy)
        self.frame_pcidevice_info_title.setFrameShape(QFrame.NoFrame)
        self.frame_pcidevice_info_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_pcidevice_info_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_pcidevice_info_title)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_7.addWidget(self.frame_pcidevice_info_title)

        self.frame_pcidevice_info_content = QFrame(self.frame_pcidevice_info)
        self.frame_pcidevice_info_content.setObjectName(u"frame_pcidevice_info_content")
        self.frame_pcidevice_info_content.setFrameShape(QFrame.NoFrame)
        self.frame_pcidevice_info_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_pcidevice_info_content)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_bus_info_title = QFrame(self.frame_pcidevice_info_content)
        self.frame_bus_info_title.setObjectName(u"frame_bus_info_title")
        sizePolicy.setHeightForWidth(self.frame_bus_info_title.sizePolicy().hasHeightForWidth())
        self.frame_bus_info_title.setSizePolicy(sizePolicy)
        self.frame_bus_info_title.setFrameShape(QFrame.NoFrame)
        self.frame_bus_info_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_bus_info_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_bus_info_tag = QLabel(self.frame_bus_info_title)
        self.label_bus_info_tag.setObjectName(u"label_bus_info_tag")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_bus_info_tag.sizePolicy().hasHeightForWidth())
        self.label_bus_info_tag.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_bus_info_tag)

        self.label_bus_info = QLabel(self.frame_bus_info_title)
        self.label_bus_info.setObjectName(u"label_bus_info")

        self.horizontalLayout_4.addWidget(self.label_bus_info)


        self.verticalLayout_8.addWidget(self.frame_bus_info_title)

        self.frame_bus_info = QFrame(self.frame_pcidevice_info_content)
        self.frame_bus_info.setObjectName(u"frame_bus_info")
        self.frame_bus_info.setFrameShape(QFrame.NoFrame)
        self.frame_bus_info.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_bus_info)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_bus_info)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineedit_bus = QLineEdit(self.frame_bus_info)
        self.lineedit_bus.setObjectName(u"lineedit_bus")

        self.gridLayout.addWidget(self.lineedit_bus, 1, 1, 1, 1)

        self.lineedit_device = QLineEdit(self.frame_bus_info)
        self.lineedit_device.setObjectName(u"lineedit_device")

        self.gridLayout.addWidget(self.lineedit_device, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_bus_info)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_bus_info)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_bus_info)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.lineedit_domain = QLineEdit(self.frame_bus_info)
        self.lineedit_domain.setObjectName(u"lineedit_domain")

        self.gridLayout.addWidget(self.lineedit_domain, 0, 1, 1, 1)

        self.lineedit_func = QLineEdit(self.frame_bus_info)
        self.lineedit_func.setObjectName(u"lineedit_func")

        self.gridLayout.addWidget(self.lineedit_func, 3, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_bus_info)

        self.frame_caps_title = QFrame(self.frame_pcidevice_info_content)
        self.frame_caps_title.setObjectName(u"frame_caps_title")
        self.frame_caps_title.setFrameShape(QFrame.NoFrame)
        self.frame_caps_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_caps_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.label_caps_tag = QLabel(self.frame_caps_title)
        self.label_caps_tag.setObjectName(u"label_caps_tag")
        sizePolicy2.setHeightForWidth(self.label_caps_tag.sizePolicy().hasHeightForWidth())
        self.label_caps_tag.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_caps_tag)

        self.label_caps = QLabel(self.frame_caps_title)
        self.label_caps.setObjectName(u"label_caps")

        self.horizontalLayout_5.addWidget(self.label_caps)


        self.verticalLayout_8.addWidget(self.frame_caps_title)

        self.tablewidget_caps = QTableWidget(self.frame_pcidevice_info_content)
        if (self.tablewidget_caps.columnCount() < 4):
            self.tablewidget_caps.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablewidget_caps.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablewidget_caps.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablewidget_caps.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablewidget_caps.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablewidget_caps.setObjectName(u"tablewidget_caps")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tablewidget_caps.sizePolicy().hasHeightForWidth())
        self.tablewidget_caps.setSizePolicy(sizePolicy3)
        self.tablewidget_caps.setAutoScroll(False)
        self.tablewidget_caps.setAlternatingRowColors(True)

        self.verticalLayout_8.addWidget(self.tablewidget_caps)

        self.frame_bars_title = QFrame(self.frame_pcidevice_info_content)
        self.frame_bars_title.setObjectName(u"frame_bars_title")
        self.horizontalLayout_6 = QHBoxLayout(self.frame_bars_title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.label_bars_tag = QLabel(self.frame_bars_title)
        self.label_bars_tag.setObjectName(u"label_bars_tag")
        sizePolicy2.setHeightForWidth(self.label_bars_tag.sizePolicy().hasHeightForWidth())
        self.label_bars_tag.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_bars_tag)

        self.label_bars = QLabel(self.frame_bars_title)
        self.label_bars.setObjectName(u"label_bars")

        self.horizontalLayout_6.addWidget(self.label_bars)


        self.verticalLayout_8.addWidget(self.frame_bars_title)

        self.tablewidget_bars = QTableWidget(self.frame_pcidevice_info_content)
        if (self.tablewidget_bars.columnCount() < 4):
            self.tablewidget_bars.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablewidget_bars.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablewidget_bars.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablewidget_bars.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablewidget_bars.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tablewidget_bars.setObjectName(u"tablewidget_bars")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tablewidget_bars.sizePolicy().hasHeightForWidth())
        self.tablewidget_bars.setSizePolicy(sizePolicy4)
        self.tablewidget_bars.setAutoScroll(False)
        self.tablewidget_bars.setAlternatingRowColors(True)

        self.verticalLayout_8.addWidget(self.tablewidget_bars)


        self.verticalLayout_7.addWidget(self.frame_pcidevice_info_content)


        self.verticalLayout_5.addWidget(self.frame_pcidevice_info)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_right)


        self.verticalLayout_2.addWidget(self.frame_main)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.verticalLayout_6.addWidget(self.scrollarea)


        self.retranslateUi(PCIDevicesWidget)

        QMetaObject.connectSlotsByName(PCIDevicesWidget)
    # setupUi

    def retranslateUi(self, PCIDevicesWidget):
        PCIDevicesWidget.setWindowTitle(QCoreApplication.translate("PCIDevicesWidget", u"Form", None))
        self.label_pci_device.setText(QCoreApplication.translate("PCIDevicesWidget", u"PC\u8bbe\u5907\u5217\u8868", None))
        self.btn_update.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u4ece\u8fdc\u7a0b\u66f4\u65b0", None))
        self.label.setText(QCoreApplication.translate("PCIDevicesWidget", u"PCI\u8bbe\u5907\u4fe1\u606f", None))
        self.label_bus_info_tag.setText("")
        self.label_bus_info.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u603b\u7ebf\u4fe1\u606f(BDF)", None))
        self.label_5.setText(QCoreApplication.translate("PCIDevicesWidget", u"device", None))
        self.label_3.setText(QCoreApplication.translate("PCIDevicesWidget", u"bus", None))
        self.label_4.setText(QCoreApplication.translate("PCIDevicesWidget", u"domain", None))
        self.label_6.setText(QCoreApplication.translate("PCIDevicesWidget", u"function", None))
        self.label_caps_tag.setText("")
        self.label_caps.setText(QCoreApplication.translate("PCIDevicesWidget", u"Capabilities", None))
        ___qtablewidgetitem = self.tablewidget_caps.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PCIDevicesWidget", u"ID", None));
        ___qtablewidgetitem1 = self.tablewidget_caps.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tablewidget_caps.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u504f\u79fb", None));
        ___qtablewidgetitem3 = self.tablewidget_caps.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u5927\u5c0f", None));
        self.label_bars_tag.setText("")
        self.label_bars.setText(QCoreApplication.translate("PCIDevicesWidget", u"Bars", None))
        ___qtablewidgetitem4 = self.tablewidget_bars.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u5730\u5740", None));
        ___qtablewidgetitem5 = self.tablewidget_bars.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u5927\u5c0f", None));
        ___qtablewidgetitem6 = self.tablewidget_bars.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("PCIDevicesWidget", u"mask", None));
        ___qtablewidgetitem7 = self.tablewidget_bars.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("PCIDevicesWidget", u"\u7c7b\u578b", None));
    # retranslateUi

