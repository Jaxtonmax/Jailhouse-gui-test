# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mem_region_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MemRegionItem(object):
    def setupUi(self, MemRegionItem):
        if not MemRegionItem.objectName():
            MemRegionItem.setObjectName(u"MemRegionItem")
        MemRegionItem.resize(478, 31)
        self.horizontalLayout = QHBoxLayout(MemRegionItem)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_addr = QFrame(MemRegionItem)
        self.frame_addr.setObjectName(u"frame_addr")
        self.frame_addr.setFrameShape(QFrame.NoFrame)
        self.frame_addr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_addr)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_addr = QLabel(self.frame_addr)
        self.label_addr.setObjectName(u"label_addr")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_addr.sizePolicy().hasHeightForWidth())
        self.label_addr.setSizePolicy(sizePolicy)
        self.label_addr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_addr)

        self.lineedit_addr = QLineEdit(self.frame_addr)
        self.lineedit_addr.setObjectName(u"lineedit_addr")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_addr.sizePolicy().hasHeightForWidth())
        self.lineedit_addr.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineedit_addr)


        self.horizontalLayout.addWidget(self.frame_addr)

        self.frame_size = QFrame(MemRegionItem)
        self.frame_size.setObjectName(u"frame_size")
        self.frame_size.setFrameShape(QFrame.NoFrame)
        self.frame_size.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_size)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_size = QLabel(self.frame_size)
        self.label_size.setObjectName(u"label_size")
        sizePolicy.setHeightForWidth(self.label_size.sizePolicy().hasHeightForWidth())
        self.label_size.setSizePolicy(sizePolicy)
        self.label_size.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_size)

        self.lineedit_size = QLineEdit(self.frame_size)
        self.lineedit_size.setObjectName(u"lineedit_size")
        sizePolicy1.setHeightForWidth(self.lineedit_size.sizePolicy().hasHeightForWidth())
        self.lineedit_size.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.lineedit_size)


        self.horizontalLayout.addWidget(self.frame_size)

        self.frame_btns = QFrame(MemRegionItem)
        self.frame_btns.setObjectName(u"frame_btns")
        sizePolicy.setHeightForWidth(self.frame_btns.sizePolicy().hasHeightForWidth())
        self.frame_btns.setSizePolicy(sizePolicy)
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_remove = QPushButton(self.frame_btns)
        self.btn_remove.setObjectName(u"btn_remove")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_remove.sizePolicy().hasHeightForWidth())
        self.btn_remove.setSizePolicy(sizePolicy2)
        self.btn_remove.setFlat(True)

        self.horizontalLayout_4.addWidget(self.btn_remove)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.retranslateUi(MemRegionItem)

        QMetaObject.connectSlotsByName(MemRegionItem)
    # setupUi

    def retranslateUi(self, MemRegionItem):
        MemRegionItem.setWindowTitle(QCoreApplication.translate("MemRegionItem", u"Form", None))
        self.label_addr.setText(QCoreApplication.translate("MemRegionItem", u"\u5730\u5740", None))
        self.label_size.setText(QCoreApplication.translate("MemRegionItem", u"\u5927\u5c0f", None))
        self.btn_remove.setText("")
    # retranslateUi

