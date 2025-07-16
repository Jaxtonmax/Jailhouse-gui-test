# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vm_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VMConfigWidget(object):
    def setupUi(self, VMConfigWidget):
        if not VMConfigWidget.objectName():
            VMConfigWidget.setObjectName(u"VMConfigWidget")
        VMConfigWidget.resize(971, 840)
        self.verticalLayout = QVBoxLayout(VMConfigWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_submenu = QFrame(VMConfigWidget)
        self.frame_submenu.setObjectName(u"frame_submenu")
        self.frame_submenu.setFrameShape(QFrame.NoFrame)
        self.frame_submenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_submenu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_rootcell = QPushButton(self.frame_submenu)
        self.btn_rootcell.setObjectName(u"btn_rootcell")
        self.btn_rootcell.setCheckable(True)
        self.btn_rootcell.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_rootcell)

        self.btn_ivshmem = QPushButton(self.frame_submenu)
        self.btn_ivshmem.setObjectName(u"btn_ivshmem")
        self.btn_ivshmem.setCheckable(True)
        self.btn_ivshmem.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_ivshmem)

        self.btn_pci_device = QPushButton(self.frame_submenu)
        self.btn_pci_device.setObjectName(u"btn_pci_device")
        self.btn_pci_device.setCheckable(True)
        self.btn_pci_device.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_pci_device)

        self.btn_guestcells = QPushButton(self.frame_submenu)
        self.btn_guestcells.setObjectName(u"btn_guestcells")
        self.btn_guestcells.setCheckable(True)
        self.btn_guestcells.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_guestcells)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_submenu)

        self.stacked_widget = QStackedWidget(VMConfigWidget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked_widget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stacked_widget)


        self.retranslateUi(VMConfigWidget)

        QMetaObject.connectSlotsByName(VMConfigWidget)
    # setupUi

    def retranslateUi(self, VMConfigWidget):
        VMConfigWidget.setWindowTitle(QCoreApplication.translate("VMConfigWidget", u"Form", None))
        self.btn_rootcell.setText(QCoreApplication.translate("VMConfigWidget", u"RootCell", None))
        self.btn_ivshmem.setText(QCoreApplication.translate("VMConfigWidget", u"\u6838\u95f4\u901a\u4fe1", None))
        self.btn_pci_device.setText(QCoreApplication.translate("VMConfigWidget", u"PCI\u8bbe\u5907", None))
        self.btn_guestcells.setText(QCoreApplication.translate("VMConfigWidget", u"\u865a\u62df\u673a", None))
    # retranslateUi

