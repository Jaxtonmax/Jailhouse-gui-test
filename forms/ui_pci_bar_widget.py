# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pci_bar_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PCIBarWidget(object):
    def setupUi(self, PCIBarWidget):
        if not PCIBarWidget.objectName():
            PCIBarWidget.setObjectName(u"PCIBarWidget")
        PCIBarWidget.resize(439, 47)
        self.verticalLayout = QVBoxLayout(PCIBarWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(PCIBarWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.label_addr = QLabel(self.frame)
        self.label_addr.setObjectName(u"label_addr")

        self.horizontalLayout.addWidget(self.label_addr)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_size = QLabel(self.frame)
        self.label_size.setObjectName(u"label_size")

        self.horizontalLayout.addWidget(self.label_size)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_mask = QLabel(self.frame)
        self.label_mask.setObjectName(u"label_mask")

        self.horizontalLayout.addWidget(self.label_mask)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.label_type = QLabel(self.frame)
        self.label_type.setObjectName(u"label_type")

        self.horizontalLayout.addWidget(self.label_type)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(PCIBarWidget)

        QMetaObject.connectSlotsByName(PCIBarWidget)
    # setupUi

    def retranslateUi(self, PCIBarWidget):
        PCIBarWidget.setWindowTitle(QCoreApplication.translate("PCIBarWidget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("PCIBarWidget", u"\u5730\u5740", None))
        self.label_addr.setText(QCoreApplication.translate("PCIBarWidget", u"#addr", None))
        self.label_4.setText(QCoreApplication.translate("PCIBarWidget", u"\u5927\u5c0f", None))
        self.label_size.setText(QCoreApplication.translate("PCIBarWidget", u"#size", None))
        self.label_6.setText(QCoreApplication.translate("PCIBarWidget", u"mask", None))
        self.label_mask.setText(QCoreApplication.translate("PCIBarWidget", u"#mask", None))
        self.label_8.setText(QCoreApplication.translate("PCIBarWidget", u"\u7c7b\u578b", None))
        self.label_type.setText(QCoreApplication.translate("PCIBarWidget", u"#type", None))
    # retranslateUi

