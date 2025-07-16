# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpuload.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CPULoadWidget(object):
    def setupUi(self, CPULoadWidget):
        if not CPULoadWidget.objectName():
            CPULoadWidget.setObjectName(u"CPULoadWidget")
        CPULoadWidget.resize(575, 362)
        self.verticalLayout = QVBoxLayout(CPULoadWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(CPULoadWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.frame_values = QFrame(self.frame_main)
        self.frame_values.setObjectName(u"frame_values")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_values.sizePolicy().hasHeightForWidth())
        self.frame_values.setSizePolicy(sizePolicy)
        self.frame_values.setFrameShape(QFrame.NoFrame)
        self.frame_values.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_values)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 7, 0, 0)
        self.label_3 = QLabel(self.frame_values)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_load = QLabel(self.frame_values)
        self.label_load.setObjectName(u"label_load")
        self.label_load.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_load)

        self.label_4 = QLabel(self.frame_values)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_count = QLabel(self.frame_values)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setMinimumSize(QSize(100, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_count)


        self.horizontalLayout.addWidget(self.frame_values)

        self.frame_chart = QFrame(self.frame_main)
        self.frame_chart.setObjectName(u"frame_chart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_chart.sizePolicy().hasHeightForWidth())
        self.frame_chart.setSizePolicy(sizePolicy1)
        self.frame_chart.setFrameShape(QFrame.NoFrame)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_chart)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame_chart)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(CPULoadWidget)

        QMetaObject.connectSlotsByName(CPULoadWidget)
    # setupUi

    def retranslateUi(self, CPULoadWidget):
        CPULoadWidget.setWindowTitle(QCoreApplication.translate("CPULoadWidget", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CPULoadWidget", u"CPU\u8d1f\u8f7d", None))
        self.label_load.setText("")
        self.label_4.setText(QCoreApplication.translate("CPULoadWidget", u"CPU\u4e2a\u6570", None))
        self.label_count.setText("")
    # retranslateUi

