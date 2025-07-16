# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rootcell_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RootCellWidget(object):
    def setupUi(self, RootCellWidget):
        if not RootCellWidget.objectName():
            RootCellWidget.setObjectName(u"RootCellWidget")
        RootCellWidget.resize(916, 749)
        self.verticalLayout_11 = QVBoxLayout(RootCellWidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(RootCellWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setFrameShape(QFrame.NoFrame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 916, 749))
        self.verticalLayout_3 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_system = QFrame(self.frame_right)
        self.frame_system.setObjectName(u"frame_system")
        self.frame_system.setFrameShape(QFrame.NoFrame)
        self.frame_system.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_system)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_system_title = QFrame(self.frame_system)
        self.frame_system_title.setObjectName(u"frame_system_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_system_title.sizePolicy().hasHeightForWidth())
        self.frame_system_title.setSizePolicy(sizePolicy)
        self.frame_system_title.setFrameShape(QFrame.NoFrame)
        self.frame_system_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_system_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_9 = QLabel(self.frame_system_title)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout.addWidget(self.frame_system_title)

        self.frame_system_content = QFrame(self.frame_system)
        self.frame_system_content.setObjectName(u"frame_system_content")
        self.frame_system_content.setFrameShape(QFrame.NoFrame)
        self.frame_system_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_system_content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_name = QFrame(self.frame_system_content)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_name)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label)

        self.lineedit_name = QLineEdit(self.frame_name)
        self.lineedit_name.setObjectName(u"lineedit_name")
        sizePolicy.setHeightForWidth(self.lineedit_name.sizePolicy().hasHeightForWidth())
        self.lineedit_name.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.lineedit_name)


        self.verticalLayout_5.addWidget(self.frame_name)

        self.label_10 = QLabel(self.frame_system_content)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.frame_ram = QFrame(self.frame_system_content)
        self.frame_ram.setObjectName(u"frame_ram")
        self.frame_ram.setFrameShape(QFrame.NoFrame)
        self.frame_ram.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_ram)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_5.addWidget(self.frame_ram)


        self.verticalLayout.addWidget(self.frame_system_content)


        self.verticalLayout_2.addWidget(self.frame_system)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_right)

        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_left)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_hyp = QFrame(self.frame_left)
        self.frame_hyp.setObjectName(u"frame_hyp")
        self.frame_hyp.setFrameShape(QFrame.NoFrame)
        self.frame_hyp.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_hyp)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_hyp_title = QFrame(self.frame_hyp)
        self.frame_hyp_title.setObjectName(u"frame_hyp_title")
        sizePolicy.setHeightForWidth(self.frame_hyp_title.sizePolicy().hasHeightForWidth())
        self.frame_hyp_title.setSizePolicy(sizePolicy)
        self.frame_hyp_title.setFrameShape(QFrame.NoFrame)
        self.frame_hyp_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_hyp_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_hyp_title)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.frame_hyp_title)

        self.frame_hyp_content = QFrame(self.frame_hyp)
        self.frame_hyp_content.setObjectName(u"frame_hyp_content")
        self.frame_hyp_content.setFrameShape(QFrame.NoFrame)
        self.frame_hyp_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_hyp_content)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_hyp_items = QFrame(self.frame_hyp_content)
        self.frame_hyp_items.setObjectName(u"frame_hyp_items")
        self.frame_hyp_items.setFrameShape(QFrame.NoFrame)
        self.frame_hyp_items.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_hyp_items)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_hyp_base = QLabel(self.frame_hyp_items)
        self.label_hyp_base.setObjectName(u"label_hyp_base")
        sizePolicy1.setHeightForWidth(self.label_hyp_base.sizePolicy().hasHeightForWidth())
        self.label_hyp_base.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_hyp_base, 1, 0, 1, 1)

        self.label_debug_terminal = QLabel(self.frame_hyp_items)
        self.label_debug_terminal.setObjectName(u"label_debug_terminal")
        sizePolicy1.setHeightForWidth(self.label_debug_terminal.sizePolicy().hasHeightForWidth())
        self.label_debug_terminal.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_debug_terminal, 0, 0, 1, 1)

        self.label_hyp_size = QLabel(self.frame_hyp_items)
        self.label_hyp_size.setObjectName(u"label_hyp_size")
        sizePolicy1.setHeightForWidth(self.label_hyp_size.sizePolicy().hasHeightForWidth())
        self.label_hyp_size.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.label_hyp_size, 2, 0, 1, 1)

        self.lineedit_hyp_addr = QLineEdit(self.frame_hyp_items)
        self.lineedit_hyp_addr.setObjectName(u"lineedit_hyp_addr")
        sizePolicy.setHeightForWidth(self.lineedit_hyp_addr.sizePolicy().hasHeightForWidth())
        self.lineedit_hyp_addr.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineedit_hyp_addr, 1, 1, 1, 1)

        self.lineedit_hyp_size = QLineEdit(self.frame_hyp_items)
        self.lineedit_hyp_size.setObjectName(u"lineedit_hyp_size")
        sizePolicy.setHeightForWidth(self.lineedit_hyp_size.sizePolicy().hasHeightForWidth())
        self.lineedit_hyp_size.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.lineedit_hyp_size, 2, 1, 1, 1)

        self.combobox_debug_console = QComboBox(self.frame_hyp_items)
        self.combobox_debug_console.setObjectName(u"combobox_debug_console")

        self.gridLayout_2.addWidget(self.combobox_debug_console, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_hyp_items)


        self.verticalLayout_6.addWidget(self.frame_hyp_content)


        self.verticalLayout_10.addWidget(self.frame_hyp)

        self.frame_pci_mmconfig = QFrame(self.frame_left)
        self.frame_pci_mmconfig.setObjectName(u"frame_pci_mmconfig")
        self.frame_pci_mmconfig.setFrameShape(QFrame.NoFrame)
        self.frame_pci_mmconfig.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_pci_mmconfig)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_pci_mmconfig_title = QFrame(self.frame_pci_mmconfig)
        self.frame_pci_mmconfig_title.setObjectName(u"frame_pci_mmconfig_title")
        sizePolicy.setHeightForWidth(self.frame_pci_mmconfig_title.sizePolicy().hasHeightForWidth())
        self.frame_pci_mmconfig_title.setSizePolicy(sizePolicy)
        self.frame_pci_mmconfig_title.setFrameShape(QFrame.NoFrame)
        self.frame_pci_mmconfig_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_pci_mmconfig_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_pci_mmconfig_title)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_pci_mmconfig_title)

        self.frame_pci_mmconfig_content = QFrame(self.frame_pci_mmconfig)
        self.frame_pci_mmconfig_content.setObjectName(u"frame_pci_mmconfig_content")
        self.frame_pci_mmconfig_content.setFrameShape(QFrame.NoFrame)
        self.frame_pci_mmconfig_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_pci_mmconfig_content)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_3 = QFrame(self.frame_pci_mmconfig_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_pci_mmconfig_bus_count = QLabel(self.frame_3)
        self.label_pci_mmconfig_bus_count.setObjectName(u"label_pci_mmconfig_bus_count")
        sizePolicy1.setHeightForWidth(self.label_pci_mmconfig_bus_count.sizePolicy().hasHeightForWidth())
        self.label_pci_mmconfig_bus_count.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_pci_mmconfig_bus_count, 2, 0, 1, 1)

        self.label_pci_mmconfig_domain = QLabel(self.frame_3)
        self.label_pci_mmconfig_domain.setObjectName(u"label_pci_mmconfig_domain")
        sizePolicy1.setHeightForWidth(self.label_pci_mmconfig_domain.sizePolicy().hasHeightForWidth())
        self.label_pci_mmconfig_domain.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_pci_mmconfig_domain, 3, 0, 1, 1)

        self.lineedit_pci_mmconfig_domain = QLineEdit(self.frame_3)
        self.lineedit_pci_mmconfig_domain.setObjectName(u"lineedit_pci_mmconfig_domain")
        sizePolicy.setHeightForWidth(self.lineedit_pci_mmconfig_domain.sizePolicy().hasHeightForWidth())
        self.lineedit_pci_mmconfig_domain.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineedit_pci_mmconfig_domain, 3, 1, 1, 1)

        self.label_pci_mmconfig_base = QLabel(self.frame_3)
        self.label_pci_mmconfig_base.setObjectName(u"label_pci_mmconfig_base")
        sizePolicy1.setHeightForWidth(self.label_pci_mmconfig_base.sizePolicy().hasHeightForWidth())
        self.label_pci_mmconfig_base.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_pci_mmconfig_base, 0, 0, 1, 1)

        self.lineedit_pci_mmconfig_count = QLineEdit(self.frame_3)
        self.lineedit_pci_mmconfig_count.setObjectName(u"lineedit_pci_mmconfig_count")
        sizePolicy.setHeightForWidth(self.lineedit_pci_mmconfig_count.sizePolicy().hasHeightForWidth())
        self.lineedit_pci_mmconfig_count.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineedit_pci_mmconfig_count, 2, 1, 1, 1)

        self.lineedit_pci_mmconfig_addr = QLineEdit(self.frame_3)
        self.lineedit_pci_mmconfig_addr.setObjectName(u"lineedit_pci_mmconfig_addr")
        sizePolicy.setHeightForWidth(self.lineedit_pci_mmconfig_addr.sizePolicy().hasHeightForWidth())
        self.lineedit_pci_mmconfig_addr.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineedit_pci_mmconfig_addr, 0, 1, 1, 1)

        self.label_pci_mmconfig_vpci = QLabel(self.frame_3)
        self.label_pci_mmconfig_vpci.setObjectName(u"label_pci_mmconfig_vpci")
        sizePolicy1.setHeightForWidth(self.label_pci_mmconfig_vpci.sizePolicy().hasHeightForWidth())
        self.label_pci_mmconfig_vpci.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_pci_mmconfig_vpci, 4, 0, 1, 1)

        self.lineedit_vpci_irq_base = QLineEdit(self.frame_3)
        self.lineedit_vpci_irq_base.setObjectName(u"lineedit_vpci_irq_base")
        sizePolicy.setHeightForWidth(self.lineedit_vpci_irq_base.sizePolicy().hasHeightForWidth())
        self.lineedit_vpci_irq_base.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lineedit_vpci_irq_base, 4, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_3)


        self.verticalLayout_8.addWidget(self.frame_pci_mmconfig_content)


        self.verticalLayout_10.addWidget(self.frame_pci_mmconfig)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_left)


        self.verticalLayout_3.addWidget(self.frame_main)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.verticalLayout_11.addWidget(self.scrollarea)


        self.retranslateUi(RootCellWidget)

        QMetaObject.connectSlotsByName(RootCellWidget)
    # setupUi

    def retranslateUi(self, RootCellWidget):
        RootCellWidget.setWindowTitle(QCoreApplication.translate("RootCellWidget", u"Form", None))
        self.label_9.setText(QCoreApplication.translate("RootCellWidget", u"\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("RootCellWidget", u"\u540d\u79f0", None))
        self.label_10.setText(QCoreApplication.translate("RootCellWidget", u"\u5185\u5b58", None))
        self.label_6.setText(QCoreApplication.translate("RootCellWidget", u"Hypervisor", None))
        self.label_hyp_base.setText(QCoreApplication.translate("RootCellWidget", u"Hypervisor\u56fa\u4ef6\u8d77\u59cb\u5730\u5740", None))
        self.label_debug_terminal.setText(QCoreApplication.translate("RootCellWidget", u"\u8c03\u8bd5\u7ec8\u7aef", None))
        self.label_hyp_size.setText(QCoreApplication.translate("RootCellWidget", u"Hypervisor\u56fa\u4ef6\u5927\u5c0f", None))
        self.label_2.setText(QCoreApplication.translate("RootCellWidget", u"PCI MMConfig", None))
        self.label_pci_mmconfig_bus_count.setText(QCoreApplication.translate("RootCellWidget", u"\u603b\u7ebf\u6570\u91cf", None))
        self.label_pci_mmconfig_domain.setText(QCoreApplication.translate("RootCellWidget", u"domain", None))
        self.label_pci_mmconfig_base.setText(QCoreApplication.translate("RootCellWidget", u"\u57fa\u5730\u5740", None))
        self.label_pci_mmconfig_vpci.setText(QCoreApplication.translate("RootCellWidget", u"VPCI\u8d77\u59cbIRQ", None))
    # retranslateUi

