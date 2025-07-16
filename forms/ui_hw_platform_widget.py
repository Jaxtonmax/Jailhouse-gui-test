# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hw_platform_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_HwPlatformWidget(object):
    def setupUi(self, HwPlatformWidget):
        if not HwPlatformWidget.objectName():
            HwPlatformWidget.setObjectName(u"HwPlatformWidget")
        HwPlatformWidget.resize(833, 590)
        self.verticalLayout = QVBoxLayout(HwPlatformWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_submenu = QFrame(HwPlatformWidget)
        self.frame_submenu.setObjectName(u"frame_submenu")
        self.frame_submenu.setFrameShape(QFrame.NoFrame)
        self.frame_submenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_submenu)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cpu = QPushButton(self.frame_submenu)
        self.btn_cpu.setObjectName(u"btn_cpu")
        self.btn_cpu.setCheckable(True)
        self.btn_cpu.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_cpu)

        self.btn_board = QPushButton(self.frame_submenu)
        self.btn_board.setObjectName(u"btn_board")
        self.btn_board.setCheckable(True)
        self.btn_board.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.btn_board)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_submenu)

        self.stacked_widget = QStackedWidget(HwPlatformWidget)
        self.stacked_widget.setObjectName(u"stacked_widget")

        self.verticalLayout.addWidget(self.stacked_widget)


        self.retranslateUi(HwPlatformWidget)

        QMetaObject.connectSlotsByName(HwPlatformWidget)
    # setupUi

    def retranslateUi(self, HwPlatformWidget):
        HwPlatformWidget.setWindowTitle(QCoreApplication.translate("HwPlatformWidget", u"Form", None))
        self.btn_cpu.setText(QCoreApplication.translate("HwPlatformWidget", u"CPU", None))
        self.btn_board.setText(QCoreApplication.translate("HwPlatformWidget", u"Board", None))
    # retranslateUi

