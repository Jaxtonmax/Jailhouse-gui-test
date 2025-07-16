# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'except_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ExceptWidget(object):
    def setupUi(self, ExceptWidget):
        if not ExceptWidget.objectName():
            ExceptWidget.setObjectName(u"ExceptWidget")
        ExceptWidget.resize(482, 396)
        self.verticalLayout = QVBoxLayout(ExceptWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(ExceptWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_copy = QPushButton(self.frame)
        self.btn_copy.setObjectName(u"btn_copy")

        self.horizontalLayout.addWidget(self.btn_copy)


        self.verticalLayout.addWidget(self.frame)

        self.textbrowser = QTextBrowser(ExceptWidget)
        self.textbrowser.setObjectName(u"textbrowser")
        self.textbrowser.setFrameShape(QFrame.NoFrame)

        self.verticalLayout.addWidget(self.textbrowser)

        self.frame_2 = QFrame(ExceptWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_ignore = QPushButton(self.frame_2)
        self.btn_ignore.setObjectName(u"btn_ignore")

        self.horizontalLayout_2.addWidget(self.btn_ignore)

        self.btn_terminate = QPushButton(self.frame_2)
        self.btn_terminate.setObjectName(u"btn_terminate")

        self.horizontalLayout_2.addWidget(self.btn_terminate)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(ExceptWidget)

        QMetaObject.connectSlotsByName(ExceptWidget)
    # setupUi

    def retranslateUi(self, ExceptWidget):
        ExceptWidget.setWindowTitle(QCoreApplication.translate("ExceptWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("ExceptWidget", u"\u7a0b\u5e8f\u6267\u884c\u5f02\u5e38", None))
        self.btn_copy.setText(QCoreApplication.translate("ExceptWidget", u"\u590d\u5236", None))
        self.btn_ignore.setText(QCoreApplication.translate("ExceptWidget", u"\u5ffd\u7565", None))
        self.btn_terminate.setText(QCoreApplication.translate("ExceptWidget", u"\u7ec8\u6b62", None))
    # retranslateUi

