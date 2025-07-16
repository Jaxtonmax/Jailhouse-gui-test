# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_title.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LogTitleWidget(object):
    def setupUi(self, LogTitleWidget):
        if not LogTitleWidget.objectName():
            LogTitleWidget.setObjectName(u"LogTitleWidget")
        LogTitleWidget.resize(538, 40)
        self.horizontalLayout = QHBoxLayout(LogTitleWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LogTitleWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.combobox_level = QComboBox(self.frame)
        self.combobox_level.setObjectName(u"combobox_level")
        self.combobox_level.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_2.addWidget(self.combobox_level)

        self.btn_clean = QToolButton(self.frame)
        self.btn_clean.setObjectName(u"btn_clean")

        self.horizontalLayout_2.addWidget(self.btn_clean)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(LogTitleWidget)

        QMetaObject.connectSlotsByName(LogTitleWidget)
    # setupUi

    def retranslateUi(self, LogTitleWidget):
        LogTitleWidget.setWindowTitle(QCoreApplication.translate("LogTitleWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("LogTitleWidget", u"\u65e5\u5fd7", None))
        self.btn_clean.setText("")
    # retranslateUi

