# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mem_map_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MemMapItem(object):
    def setupUi(self, MemMapItem):
        if not MemMapItem.objectName():
            MemMapItem.setObjectName(u"MemMapItem")
        MemMapItem.resize(779, 63)
        self.horizontalLayout_3 = QHBoxLayout(MemMapItem)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(MemMapItem)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_main)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineedit_comment = QLineEdit(self.frame_title)
        self.lineedit_comment.setObjectName(u"lineedit_comment")

        self.horizontalLayout_2.addWidget(self.lineedit_comment)

        self.combobox_type = QComboBox(self.frame_title)
        self.combobox_type.setObjectName(u"combobox_type")

        self.horizontalLayout_2.addWidget(self.combobox_type)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_configs = QFrame(self.frame_main)
        self.frame_configs.setObjectName(u"frame_configs")
        self.frame_configs.setFrameShape(QFrame.NoFrame)
        self.frame_configs.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_configs)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_phys = QFrame(self.frame_configs)
        self.frame_phys.setObjectName(u"frame_phys")
        self.frame_phys.setFrameShape(QFrame.NoFrame)
        self.frame_phys.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_phys)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_phys = QLabel(self.frame_phys)
        self.label_phys.setObjectName(u"label_phys")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phys.sizePolicy().hasHeightForWidth())
        self.label_phys.setSizePolicy(sizePolicy)
        self.label_phys.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_phys)

        self.lineedit_phys = QLineEdit(self.frame_phys)
        self.lineedit_phys.setObjectName(u"lineedit_phys")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineedit_phys.sizePolicy().hasHeightForWidth())
        self.lineedit_phys.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lineedit_phys)


        self.horizontalLayout.addWidget(self.frame_phys)

        self.frame_virt = QFrame(self.frame_configs)
        self.frame_virt.setObjectName(u"frame_virt")
        self.frame_virt.setFrameShape(QFrame.NoFrame)
        self.frame_virt.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_virt)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_virt = QLabel(self.frame_virt)
        self.label_virt.setObjectName(u"label_virt")
        sizePolicy.setHeightForWidth(self.label_virt.sizePolicy().hasHeightForWidth())
        self.label_virt.setSizePolicy(sizePolicy)
        self.label_virt.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_virt)

        self.lineedit_virt = QLineEdit(self.frame_virt)
        self.lineedit_virt.setObjectName(u"lineedit_virt")
        sizePolicy1.setHeightForWidth(self.lineedit_virt.sizePolicy().hasHeightForWidth())
        self.lineedit_virt.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.lineedit_virt)


        self.horizontalLayout.addWidget(self.frame_virt)

        self.frame_size = QFrame(self.frame_configs)
        self.frame_size.setObjectName(u"frame_size")
        self.frame_size.setFrameShape(QFrame.NoFrame)
        self.frame_size.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_size)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_size = QLabel(self.frame_size)
        self.label_size.setObjectName(u"label_size")
        sizePolicy.setHeightForWidth(self.label_size.sizePolicy().hasHeightForWidth())
        self.label_size.setSizePolicy(sizePolicy)
        self.label_size.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_size)

        self.lineedit_size = QLineEdit(self.frame_size)
        self.lineedit_size.setObjectName(u"lineedit_size")
        sizePolicy1.setHeightForWidth(self.lineedit_size.sizePolicy().hasHeightForWidth())
        self.lineedit_size.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.lineedit_size)


        self.horizontalLayout.addWidget(self.frame_size)


        self.verticalLayout_2.addWidget(self.frame_configs)


        self.horizontalLayout_3.addWidget(self.frame_main)

        self.frame = QFrame(MemMapItem)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_remove = QPushButton(self.frame)
        self.btn_remove.setObjectName(u"btn_remove")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_remove.sizePolicy().hasHeightForWidth())
        self.btn_remove.setSizePolicy(sizePolicy2)
        self.btn_remove.setFlat(True)

        self.verticalLayout.addWidget(self.btn_remove)


        self.horizontalLayout_3.addWidget(self.frame)


        self.retranslateUi(MemMapItem)

        QMetaObject.connectSlotsByName(MemMapItem)
    # setupUi

    def retranslateUi(self, MemMapItem):
        MemMapItem.setWindowTitle(QCoreApplication.translate("MemMapItem", u"Form", None))
        self.lineedit_comment.setPlaceholderText(QCoreApplication.translate("MemMapItem", u"\u63cf\u8ff0\u4fe1\u606f", None))
        self.label_phys.setText(QCoreApplication.translate("MemMapItem", u"\u7269\u7406\u5730\u5740", None))
        self.label_virt.setText(QCoreApplication.translate("MemMapItem", u"\u865a\u62df\u5730\u5740", None))
        self.label_size.setText(QCoreApplication.translate("MemMapItem", u"\u5927\u5c0f", None))
        self.btn_remove.setText("")
    # retranslateUi

