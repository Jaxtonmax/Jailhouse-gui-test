# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tip_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TipWidget(object):
    def setupUi(self, TipWidget):
        if not TipWidget.objectName():
            TipWidget.setObjectName(u"TipWidget")
        TipWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(TipWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(TipWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_main)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_icon = QLabel(self.frame_title)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_icon)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout.addWidget(self.label_title)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_content = QFrame(self.frame_main)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.textbrowser = QTextBrowser(self.frame_content)
        self.textbrowser.setObjectName(u"textbrowser")
        self.textbrowser.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_3.addWidget(self.textbrowser)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(TipWidget)

        QMetaObject.connectSlotsByName(TipWidget)
    # setupUi

    def retranslateUi(self, TipWidget):
        TipWidget.setWindowTitle(QCoreApplication.translate("TipWidget", u"Form", None))
        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("TipWidget", u"\u63d0\u793a", None))
    # retranslateUi

