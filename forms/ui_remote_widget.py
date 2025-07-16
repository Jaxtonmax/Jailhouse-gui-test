# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RemoteWidget(object):
    def setupUi(self, RemoteWidget):
        if not RemoteWidget.objectName():
            RemoteWidget.setObjectName(u"RemoteWidget")
        RemoteWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(RemoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(RemoteWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineedit_addr = QLineEdit(self.frame)
        self.lineedit_addr.setObjectName(u"lineedit_addr")

        self.horizontalLayout.addWidget(self.lineedit_addr)

        self.btn_connect = QPushButton(self.frame)
        self.btn_connect.setObjectName(u"btn_connect")

        self.horizontalLayout.addWidget(self.btn_connect)


        self.verticalLayout.addWidget(self.frame)

        self.tabWidget = QTabWidget(RemoteWidget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(RemoteWidget)

        self.tabWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(RemoteWidget)
    # setupUi

    def retranslateUi(self, RemoteWidget):
        RemoteWidget.setWindowTitle(QCoreApplication.translate("RemoteWidget", u"Form", None))
        self.lineedit_addr.setText(QCoreApplication.translate("RemoteWidget", u"tcp://127.0.0.1:4240", None))
        self.btn_connect.setText(QCoreApplication.translate("RemoteWidget", u"\u8fde\u63a5", None))
    # retranslateUi

