# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_info.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageInfoWidget(object):
    def setupUi(self, ImageInfoWidget):
        if not ImageInfoWidget.objectName():
            ImageInfoWidget.setObjectName(u"ImageInfoWidget")
        ImageInfoWidget.resize(400, 93)
        self.verticalLayout = QVBoxLayout(ImageInfoWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(ImageInfoWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkbox_enable = QCheckBox(self.frame_2)
        self.checkbox_enable.setObjectName(u"checkbox_enable")

        self.horizontalLayout.addWidget(self.checkbox_enable)

        self.lineedit_name = QLineEdit(self.frame_2)
        self.lineedit_name.setObjectName(u"lineedit_name")

        self.horizontalLayout.addWidget(self.lineedit_name)

        self.btn_remove = QPushButton(self.frame_2)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_remove)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.lineedit_filename = QLineEdit(self.frame_3)
        self.lineedit_filename.setObjectName(u"lineedit_filename")

        self.gridLayout.addWidget(self.lineedit_filename, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineedit_load_addr = QLineEdit(self.frame_3)
        self.lineedit_load_addr.setObjectName(u"lineedit_load_addr")

        self.gridLayout.addWidget(self.lineedit_load_addr, 0, 1, 1, 1)

        self.btn_file = QPushButton(self.frame_3)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setFlat(True)

        self.gridLayout.addWidget(self.btn_file, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(ImageInfoWidget)

        QMetaObject.connectSlotsByName(ImageInfoWidget)
    # setupUi

    def retranslateUi(self, ImageInfoWidget):
        ImageInfoWidget.setWindowTitle(QCoreApplication.translate("ImageInfoWidget", u"Form", None))
        self.checkbox_enable.setText(QCoreApplication.translate("ImageInfoWidget", u"\u9009\u62e9", None))
        self.lineedit_name.setPlaceholderText(QCoreApplication.translate("ImageInfoWidget", u"name", None))
        self.btn_remove.setText("")
        self.label_2.setText(QCoreApplication.translate("ImageInfoWidget", u"\u955c\u50cf\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("ImageInfoWidget", u"\u52a0\u8f7d\u5730\u5740", None))
        self.btn_file.setText("")
    # retranslateUi

