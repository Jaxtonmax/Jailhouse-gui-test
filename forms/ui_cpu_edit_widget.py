# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpu_edit_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CPUEditWidget(object):
    def setupUi(self, CPUEditWidget):
        if not CPUEditWidget.objectName():
            CPUEditWidget.setObjectName(u"CPUEditWidget")
        CPUEditWidget.resize(291, 90)
        self.horizontalLayout = QHBoxLayout(CPUEditWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_cpus = QFrame(CPUEditWidget)
        self.frame_cpus.setObjectName(u"frame_cpus")
        self.frame_cpus.setFrameShape(QFrame.NoFrame)
        self.frame_cpus.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_cpus)

        self.frame_ops = QFrame(CPUEditWidget)
        self.frame_ops.setObjectName(u"frame_ops")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_ops.sizePolicy().hasHeightForWidth())
        self.frame_ops.setSizePolicy(sizePolicy)
        self.frame_ops.setFrameShape(QFrame.NoFrame)
        self.frame_ops.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_ops)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_add = QToolButton(self.frame_ops)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_ops)


        self.retranslateUi(CPUEditWidget)

        QMetaObject.connectSlotsByName(CPUEditWidget)
    # setupUi

    def retranslateUi(self, CPUEditWidget):
        CPUEditWidget.setWindowTitle(QCoreApplication.translate("CPUEditWidget", u"Form", None))
        self.btn_add.setText(QCoreApplication.translate("CPUEditWidget", u"+", None))
    # retranslateUi

