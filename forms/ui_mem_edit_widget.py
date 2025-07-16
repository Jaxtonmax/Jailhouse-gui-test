# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mem_edit_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MemEditWidget(object):
    def setupUi(self, MemEditWidget):
        if not MemEditWidget.objectName():
            MemEditWidget.setObjectName(u"MemEditWidget")
        MemEditWidget.resize(562, 46)
        self.verticalLayout = QVBoxLayout(MemEditWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 7, 0, 10)
        self.frame_title = QFrame(MemEditWidget)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_total = QLabel(self.frame_title)
        self.label_total.setObjectName(u"label_total")
        sizePolicy.setHeightForWidth(self.label_total.sizePolicy().hasHeightForWidth())
        self.label_total.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_total)

        self.label_msg = QLabel(self.frame_title)
        self.label_msg.setObjectName(u"label_msg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_msg.sizePolicy().hasHeightForWidth())
        self.label_msg.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_msg)

        self.btn_add = QPushButton(self.frame_title)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_add)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_regions = QFrame(MemEditWidget)
        self.frame_regions.setObjectName(u"frame_regions")
        self.frame_regions.setFrameShape(QFrame.NoFrame)
        self.frame_regions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_regions)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_regions)


        self.retranslateUi(MemEditWidget)

        QMetaObject.connectSlotsByName(MemEditWidget)
    # setupUi

    def retranslateUi(self, MemEditWidget):
        MemEditWidget.setWindowTitle(QCoreApplication.translate("MemEditWidget", u"Form", None))
        self.label_total.setText("")
        self.label_msg.setText("")
        self.btn_add.setText("")
    # retranslateUi

