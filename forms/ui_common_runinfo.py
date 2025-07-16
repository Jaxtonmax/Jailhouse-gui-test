# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'common_runinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CommonRunInfoWidget(object):
    def setupUi(self, CommonRunInfoWidget):
        if not CommonRunInfoWidget.objectName():
            CommonRunInfoWidget.setObjectName(u"CommonRunInfoWidget")
        CommonRunInfoWidget.resize(412, 116)
        self.verticalLayout = QVBoxLayout(CommonRunInfoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_main = QFrame(CommonRunInfoWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.frame_main)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_images_title = QFrame(self.frame)
        self.frame_images_title.setObjectName(u"frame_images_title")
        self.frame_images_title.setFrameShape(QFrame.NoFrame)
        self.frame_images_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_images_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_images_title)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_add_image = QPushButton(self.frame_images_title)
        self.btn_add_image.setObjectName(u"btn_add_image")
        self.btn_add_image.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_add_image)


        self.verticalLayout_3.addWidget(self.frame_images_title)

        self.frame_images = QFrame(self.frame)
        self.frame_images.setObjectName(u"frame_images")
        self.frame_images.setFrameShape(QFrame.NoFrame)
        self.frame_images.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_images)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(16, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_images)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_reset_addr = QFrame(self.frame_main)
        self.frame_reset_addr.setObjectName(u"frame_reset_addr")
        self.frame_reset_addr.setFrameShape(QFrame.NoFrame)
        self.frame_reset_addr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_reset_addr)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_reset_addr)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineedit_reset_addr = QLineEdit(self.frame_reset_addr)
        self.lineedit_reset_addr.setObjectName(u"lineedit_reset_addr")

        self.horizontalLayout_2.addWidget(self.lineedit_reset_addr)


        self.verticalLayout_2.addWidget(self.frame_reset_addr)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(CommonRunInfoWidget)

        QMetaObject.connectSlotsByName(CommonRunInfoWidget)
    # setupUi

    def retranslateUi(self, CommonRunInfoWidget):
        CommonRunInfoWidget.setWindowTitle(QCoreApplication.translate("CommonRunInfoWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("CommonRunInfoWidget", u"\u955c\u50cf\u6587\u4ef6", None))
        self.btn_add_image.setText("")
        self.label_2.setText(QCoreApplication.translate("CommonRunInfoWidget", u"\u542f\u52a8\u5165\u53e3\u5730\u5740", None))
    # retranslateUi

