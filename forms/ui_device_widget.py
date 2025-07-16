# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeviceWidget(object):
    def setupUi(self, DeviceWidget):
        if not DeviceWidget.objectName():
            DeviceWidget.setObjectName(u"DeviceWidget")
        DeviceWidget.resize(94, 29)
        self.verticalLayout = QVBoxLayout(DeviceWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.button = QPushButton(DeviceWidget)
        self.button.setObjectName(u"button")
        self.button.setCheckable(True)

        self.verticalLayout.addWidget(self.button)


        self.retranslateUi(DeviceWidget)

        QMetaObject.connectSlotsByName(DeviceWidget)
    # setupUi

    def retranslateUi(self, DeviceWidget):
        DeviceWidget.setWindowTitle(QCoreApplication.translate("DeviceWidget", u"Form", None))
        self.button.setText(QCoreApplication.translate("DeviceWidget", u"PushButton", None))
    # retranslateUi

