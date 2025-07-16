# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HomePageWidget(object):
    def setupUi(self, HomePageWidget):
        if not HomePageWidget.objectName():
            HomePageWidget.setObjectName(u"HomePageWidget")
        HomePageWidget.resize(615, 511)
        self.verticalLayout = QVBoxLayout(HomePageWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(HomePageWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 14, -1, -1)
        self.frame_new = QFrame(self.frame_main)
        self.frame_new.setObjectName(u"frame_new")
        self.frame_new.setFrameShape(QFrame.NoFrame)
        self.frame_new.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_new)
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_new1 = QFrame(self.frame_new)
        self.frame_new1.setObjectName(u"frame_new1")
        self.frame_new1.setFrameShape(QFrame.NoFrame)
        self.frame_new1.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_new1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_home_icon = QLabel(self.frame_new1)
        self.label_home_icon.setObjectName(u"label_home_icon")
        self.label_home_icon.setMinimumSize(QSize(25, 25))
        self.label_home_icon.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.label_home_icon)

        self.label_home = QLabel(self.frame_new1)
        self.label_home.setObjectName(u"label_home")

        self.horizontalLayout_2.addWidget(self.label_home)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_new1)

        self.frame_new2 = QFrame(self.frame_new)
        self.frame_new2.setObjectName(u"frame_new2")
        self.frame_new2.setFrameShape(QFrame.NoFrame)
        self.frame_new2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_new2)
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new = QPushButton(self.frame_new2)
        self.btn_new.setObjectName(u"btn_new")

        self.horizontalLayout.addWidget(self.btn_new)

        self.btn_open = QPushButton(self.frame_new2)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout.addWidget(self.btn_open)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_new2)


        self.verticalLayout_2.addWidget(self.frame_new)

        self.frame_open = QFrame(self.frame_main)
        self.frame_open.setObjectName(u"frame_open")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_open.sizePolicy().hasHeightForWidth())
        self.frame_open.setSizePolicy(sizePolicy)
        self.frame_open.setFrameShape(QFrame.NoFrame)
        self.frame_open.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_open)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(HomePageWidget)

        QMetaObject.connectSlotsByName(HomePageWidget)
    # setupUi

    def retranslateUi(self, HomePageWidget):
        HomePageWidget.setWindowTitle(QCoreApplication.translate("HomePageWidget", u"Form", None))
        self.label_home_icon.setText("")
        self.label_home.setText(QCoreApplication.translate("HomePageWidget", u"\u9996\u9875", None))
        self.btn_new.setText(QCoreApplication.translate("HomePageWidget", u"\u65b0\u5efa\u914d\u7f6e", None))
        self.btn_open.setText(QCoreApplication.translate("HomePageWidget", u"\u6253\u5f00\u914d\u7f6e", None))
    # retranslateUi

