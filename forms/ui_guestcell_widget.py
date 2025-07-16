# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guestcell_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GuestCellWidget(object):
    def setupUi(self, GuestCellWidget):
        if not GuestCellWidget.objectName():
            GuestCellWidget.setObjectName(u"GuestCellWidget")
        GuestCellWidget.resize(806, 812)
        self.verticalLayout_2 = QVBoxLayout(GuestCellWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_content = QFrame(GuestCellWidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_sysattr_title = QFrame(self.frame_content)
        self.frame_sysattr_title.setObjectName(u"frame_sysattr_title")
        self.frame_sysattr_title.setFrameShape(QFrame.NoFrame)
        self.frame_sysattr_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_sysattr_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_sysattr_tag = QLabel(self.frame_sysattr_title)
        self.label_sysattr_tag.setObjectName(u"label_sysattr_tag")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sysattr_tag.sizePolicy().hasHeightForWidth())
        self.label_sysattr_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_sysattr_tag)

        self.label_sysattr = QLabel(self.frame_sysattr_title)
        self.label_sysattr.setObjectName(u"label_sysattr")

        self.horizontalLayout_4.addWidget(self.label_sysattr)


        self.verticalLayout.addWidget(self.frame_sysattr_title)

        self.frame_sys_attr = QFrame(self.frame_content)
        self.frame_sys_attr.setObjectName(u"frame_sys_attr")
        self.frame_sys_attr.setFrameShape(QFrame.NoFrame)
        self.frame_sys_attr.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_sys_attr)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_sys_attr)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_sys_attr)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.combobox_console = QComboBox(self.frame_4)
        self.combobox_console.setObjectName(u"combobox_console")

        self.horizontalLayout_11.addWidget(self.combobox_console)


        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_sys_attr)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_sys_attr)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_virtual_console = QPushButton(self.frame_2)
        self.btn_virtual_console.setObjectName(u"btn_virtual_console")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_virtual_console.sizePolicy().hasHeightForWidth())
        self.btn_virtual_console.setSizePolicy(sizePolicy1)
        self.btn_virtual_console.setLayoutDirection(Qt.LeftToRight)
        self.btn_virtual_console.setAutoFillBackground(True)
        self.btn_virtual_console.setStyleSheet(u"")
        self.btn_virtual_console.setCheckable(True)
        self.btn_virtual_console.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_virtual_console)


        self.gridLayout.addWidget(self.frame_2, 3, 1, 1, 1)

        self.linedit_name = QLineEdit(self.frame_sys_attr)
        self.linedit_name.setObjectName(u"linedit_name")

        self.gridLayout.addWidget(self.linedit_name, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_sys_attr)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_sys_attr)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label = QLabel(self.frame_sys_attr)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.frame = QFrame(self.frame_sys_attr)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.radiobtn_aarch64 = QRadioButton(self.frame)
        self.radiobtn_aarch64.setObjectName(u"radiobtn_aarch64")
        self.radiobtn_aarch64.setChecked(True)

        self.horizontalLayout.addWidget(self.radiobtn_aarch64)

        self.radiobtn_aarch32 = QRadioButton(self.frame)
        self.radiobtn_aarch32.setObjectName(u"radiobtn_aarch32")

        self.horizontalLayout.addWidget(self.radiobtn_aarch32)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_sys_attr)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_use_virt_cpuid = QPushButton(self.frame_3)
        self.btn_use_virt_cpuid.setObjectName(u"btn_use_virt_cpuid")
        sizePolicy1.setHeightForWidth(self.btn_use_virt_cpuid.sizePolicy().hasHeightForWidth())
        self.btn_use_virt_cpuid.setSizePolicy(sizePolicy1)
        self.btn_use_virt_cpuid.setLayoutDirection(Qt.LeftToRight)
        self.btn_use_virt_cpuid.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_use_virt_cpuid)


        self.gridLayout.addWidget(self.frame_3, 4, 1, 1, 1)

        self.label_reset_addr = QLabel(self.frame_sys_attr)
        self.label_reset_addr.setObjectName(u"label_reset_addr")

        self.gridLayout.addWidget(self.label_reset_addr, 5, 0, 1, 1)

        self.lineedit_reset_addr = QLineEdit(self.frame_sys_attr)
        self.lineedit_reset_addr.setObjectName(u"lineedit_reset_addr")

        self.gridLayout.addWidget(self.lineedit_reset_addr, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_sys_attr)

        self.frame_sysmem_title = QFrame(self.frame_content)
        self.frame_sysmem_title.setObjectName(u"frame_sysmem_title")
        self.frame_sysmem_title.setFrameShape(QFrame.NoFrame)
        self.frame_sysmem_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_sysmem_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_sysmem_tag = QLabel(self.frame_sysmem_title)
        self.label_sysmem_tag.setObjectName(u"label_sysmem_tag")
        sizePolicy.setHeightForWidth(self.label_sysmem_tag.sizePolicy().hasHeightForWidth())
        self.label_sysmem_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_sysmem_tag)

        self.label_system_mem = QLabel(self.frame_sysmem_title)
        self.label_system_mem.setObjectName(u"label_system_mem")

        self.horizontalLayout_5.addWidget(self.label_system_mem)


        self.verticalLayout.addWidget(self.frame_sysmem_title)

        self.frame_sys_mem = QFrame(self.frame_content)
        self.frame_sys_mem.setObjectName(u"frame_sys_mem")
        self.frame_sys_mem.setFrameShape(QFrame.NoFrame)
        self.frame_sys_mem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_sys_mem)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, 5, 5)

        self.verticalLayout.addWidget(self.frame_sys_mem)

        self.frame_cpu = QFrame(self.frame_content)
        self.frame_cpu.setObjectName(u"frame_cpu")
        self.frame_cpu.setFrameShape(QFrame.NoFrame)
        self.frame_cpu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_cpu)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_cpu_tag = QLabel(self.frame_cpu)
        self.label_cpu_tag.setObjectName(u"label_cpu_tag")
        sizePolicy.setHeightForWidth(self.label_cpu_tag.sizePolicy().hasHeightForWidth())
        self.label_cpu_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_cpu_tag)

        self.label_cpu = QLabel(self.frame_cpu)
        self.label_cpu.setObjectName(u"label_cpu")

        self.horizontalLayout_6.addWidget(self.label_cpu)


        self.verticalLayout.addWidget(self.frame_cpu)

        self.frame_cpus = QFrame(self.frame_content)
        self.frame_cpus.setObjectName(u"frame_cpus")
        self.frame_cpus.setFrameShape(QFrame.NoFrame)
        self.frame_cpus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_cpus)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(11, 5, 5, 5)

        self.verticalLayout.addWidget(self.frame_cpus)

        self.frame_memmap_title = QFrame(self.frame_content)
        self.frame_memmap_title.setObjectName(u"frame_memmap_title")
        self.frame_memmap_title.setFrameShape(QFrame.NoFrame)
        self.frame_memmap_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_memmap_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_memmap_tag = QLabel(self.frame_memmap_title)
        self.label_memmap_tag.setObjectName(u"label_memmap_tag")
        sizePolicy.setHeightForWidth(self.label_memmap_tag.sizePolicy().hasHeightForWidth())
        self.label_memmap_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.label_memmap_tag)

        self.label_memmap = QLabel(self.frame_memmap_title)
        self.label_memmap.setObjectName(u"label_memmap")

        self.horizontalLayout_7.addWidget(self.label_memmap)


        self.verticalLayout.addWidget(self.frame_memmap_title)

        self.frame_memmaps = QFrame(self.frame_content)
        self.frame_memmaps.setObjectName(u"frame_memmaps")
        self.frame_memmaps.setFrameShape(QFrame.NoFrame)
        self.frame_memmaps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_memmaps)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(11, 5, 5, 5)

        self.verticalLayout.addWidget(self.frame_memmaps)

        self.frame_comm_title = QFrame(self.frame_content)
        self.frame_comm_title.setObjectName(u"frame_comm_title")
        self.frame_comm_title.setFrameShape(QFrame.NoFrame)
        self.frame_comm_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_comm_title)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_comm_tag = QLabel(self.frame_comm_title)
        self.label_comm_tag.setObjectName(u"label_comm_tag")
        sizePolicy.setHeightForWidth(self.label_comm_tag.sizePolicy().hasHeightForWidth())
        self.label_comm_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_comm_tag)

        self.label_comm = QLabel(self.frame_comm_title)
        self.label_comm.setObjectName(u"label_comm")

        self.horizontalLayout_8.addWidget(self.label_comm)


        self.verticalLayout.addWidget(self.frame_comm_title)

        self.frame_comm = QFrame(self.frame_content)
        self.frame_comm.setObjectName(u"frame_comm")
        self.frame_comm.setFrameShape(QFrame.NoFrame)
        self.frame_comm.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_comm)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_ivshmem_virt_addr = QLabel(self.frame_comm)
        self.label_ivshmem_virt_addr.setObjectName(u"label_ivshmem_virt_addr")

        self.gridLayout_2.addWidget(self.label_ivshmem_virt_addr, 0, 0, 1, 1)

        self.lineedit_ivshmem_virt_addr = QLineEdit(self.frame_comm)
        self.lineedit_ivshmem_virt_addr.setObjectName(u"lineedit_ivshmem_virt_addr")

        self.gridLayout_2.addWidget(self.lineedit_ivshmem_virt_addr, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_comm)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineedit_comm_region = QLineEdit(self.frame_comm)
        self.lineedit_comm_region.setObjectName(u"lineedit_comm_region")

        self.gridLayout_2.addWidget(self.lineedit_comm_region, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_comm)

        self.frame_devices_title = QFrame(self.frame_content)
        self.frame_devices_title.setObjectName(u"frame_devices_title")
        self.frame_devices_title.setFrameShape(QFrame.NoFrame)
        self.frame_devices_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_devices_title)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_devices_tag = QLabel(self.frame_devices_title)
        self.label_devices_tag.setObjectName(u"label_devices_tag")
        sizePolicy.setHeightForWidth(self.label_devices_tag.sizePolicy().hasHeightForWidth())
        self.label_devices_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_devices_tag)

        self.label_devices = QLabel(self.frame_devices_title)
        self.label_devices.setObjectName(u"label_devices")

        self.horizontalLayout_9.addWidget(self.label_devices)


        self.verticalLayout.addWidget(self.frame_devices_title)

        self.frame_devices = QFrame(self.frame_content)
        self.frame_devices.setObjectName(u"frame_devices")
        self.frame_devices.setFrameShape(QFrame.NoFrame)
        self.frame_devices.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_devices)

        self.frame_pci_devices_title = QFrame(self.frame_content)
        self.frame_pci_devices_title.setObjectName(u"frame_pci_devices_title")
        self.frame_pci_devices_title.setFrameShape(QFrame.NoFrame)
        self.frame_pci_devices_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_pci_devices_title)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_pci_devices_tag = QLabel(self.frame_pci_devices_title)
        self.label_pci_devices_tag.setObjectName(u"label_pci_devices_tag")
        sizePolicy.setHeightForWidth(self.label_pci_devices_tag.sizePolicy().hasHeightForWidth())
        self.label_pci_devices_tag.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_pci_devices_tag)

        self.label_pci_devices = QLabel(self.frame_pci_devices_title)
        self.label_pci_devices.setObjectName(u"label_pci_devices")

        self.horizontalLayout_10.addWidget(self.label_pci_devices)


        self.verticalLayout.addWidget(self.frame_pci_devices_title)

        self.frame_pci_devices = QFrame(self.frame_content)
        self.frame_pci_devices.setObjectName(u"frame_pci_devices")
        self.frame_pci_devices.setFrameShape(QFrame.NoFrame)
        self.frame_pci_devices.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_pci_devices)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.retranslateUi(GuestCellWidget)

        QMetaObject.connectSlotsByName(GuestCellWidget)
    # setupUi

    def retranslateUi(self, GuestCellWidget):
        GuestCellWidget.setWindowTitle(QCoreApplication.translate("GuestCellWidget", u"Form", None))
        self.label_sysattr_tag.setText("")
        self.label_sysattr.setText(QCoreApplication.translate("GuestCellWidget", u"\u7cfb\u7edf\u5c5e\u6027", None))
        self.label_5.setText(QCoreApplication.translate("GuestCellWidget", u"\u865a\u62df\u4e32\u53e3", None))
        self.label_3.setText(QCoreApplication.translate("GuestCellWidget", u"\u540d\u79f0", None))
        self.btn_virtual_console.setText("")
        self.label_6.setText(QCoreApplication.translate("GuestCellWidget", u"\u4f7f\u7528\u865a\u62dfCPUID", None))
        self.label_4.setText(QCoreApplication.translate("GuestCellWidget", u"\u6307\u4ee4\u67b6\u6784", None))
        self.label.setText(QCoreApplication.translate("GuestCellWidget", u"\u7ec8\u7aef", None))
        self.radiobtn_aarch64.setText(QCoreApplication.translate("GuestCellWidget", u"AArch64", None))
        self.radiobtn_aarch32.setText(QCoreApplication.translate("GuestCellWidget", u"AArch32", None))
        self.btn_use_virt_cpuid.setText("")
        self.label_reset_addr.setText(QCoreApplication.translate("GuestCellWidget", u"\u542f\u52a8\u5165\u53e3\u5730\u5740", None))
        self.label_sysmem_tag.setText("")
        self.label_system_mem.setText(QCoreApplication.translate("GuestCellWidget", u"\u7cfb\u7edf\u5185\u5b58", None))
        self.label_cpu_tag.setText("")
        self.label_cpu.setText(QCoreApplication.translate("GuestCellWidget", u"CPU", None))
        self.label_memmap_tag.setText("")
        self.label_memmap.setText(QCoreApplication.translate("GuestCellWidget", u"\u5730\u5740\u7a7a\u95f4\u6620\u5c04", None))
        self.label_comm_tag.setText("")
        self.label_comm.setText(QCoreApplication.translate("GuestCellWidget", u"\u6838\u95f4\u901a\u4fe1", None))
        self.label_ivshmem_virt_addr.setText(QCoreApplication.translate("GuestCellWidget", u"ivshmem\u865a\u62df\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("GuestCellWidget", u"communication region", None))
        self.label_devices_tag.setText("")
        self.label_devices.setText(QCoreApplication.translate("GuestCellWidget", u"\u8bbe\u5907", None))
        self.label_pci_devices_tag.setText("")
        self.label_pci_devices.setText(QCoreApplication.translate("GuestCellWidget", u"PCI\u8bbe\u5907", None))
    # retranslateUi

