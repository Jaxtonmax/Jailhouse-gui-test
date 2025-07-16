# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pci_cap_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PCICapWidget(object):
    def setupUi(self, PCICapWidget):
        if not PCICapWidget.objectName():
            PCICapWidget.setObjectName(u"PCICapWidget")
        PCICapWidget.resize(442, 42)
        self.verticalLayout = QVBoxLayout(PCICapWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(PCICapWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(11, 5, -1, 5)
        self.label_id_or_name = QLabel(self.frame)
        self.label_id_or_name.setObjectName(u"label_id_or_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id_or_name.sizePolicy().hasHeightForWidth())
        self.label_id_or_name.setSizePolicy(sizePolicy)
        self.label_id_or_name.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.label_id_or_name)

        self.label_start = QLabel(self.frame)
        self.label_start.setObjectName(u"label_start")

        self.horizontalLayout.addWidget(self.label_start)

        self.lineedit_start = QLineEdit(self.frame)
        self.lineedit_start.setObjectName(u"lineedit_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_start.sizePolicy().hasHeightForWidth())
        self.lineedit_start.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineedit_start)

        self.label_len = QLabel(self.frame)
        self.label_len.setObjectName(u"label_len")

        self.horizontalLayout.addWidget(self.label_len)

        self.lineedit_len = QLineEdit(self.frame)
        self.lineedit_len.setObjectName(u"lineedit_len")
        sizePolicy1.setHeightForWidth(self.lineedit_len.sizePolicy().hasHeightForWidth())
        self.lineedit_len.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.lineedit_len)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(PCICapWidget)

        QMetaObject.connectSlotsByName(PCICapWidget)
    # setupUi

    def retranslateUi(self, PCICapWidget):
        PCICapWidget.setWindowTitle(QCoreApplication.translate("PCICapWidget", u"Form", None))
        self.label_id_or_name.setText(QCoreApplication.translate("PCICapWidget", u"#id", None))
        self.label_start.setText(QCoreApplication.translate("PCICapWidget", u"start", None))
        self.label_len.setText(QCoreApplication.translate("PCICapWidget", u"len", None))
    # retranslateUi

