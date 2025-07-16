# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guestcells_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GuestCellsWidget(object):
    def setupUi(self, GuestCellsWidget):
        if not GuestCellsWidget.objectName():
            GuestCellsWidget.setObjectName(u"GuestCellsWidget")
        GuestCellsWidget.resize(1268, 1100)
        self.verticalLayout_11 = QVBoxLayout(GuestCellsWidget)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(GuestCellsWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setFrameShape(QFrame.NoFrame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 1268, 1100))
        self.verticalLayout_4 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 11)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_left)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_guestcells = QFrame(self.frame_left)
        self.frame_guestcells.setObjectName(u"frame_guestcells")
        self.frame_guestcells.setFrameShape(QFrame.NoFrame)
        self.frame_guestcells.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_guestcells)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_guestcells_title = QFrame(self.frame_guestcells)
        self.frame_guestcells_title.setObjectName(u"frame_guestcells_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_guestcells_title.sizePolicy().hasHeightForWidth())
        self.frame_guestcells_title.setSizePolicy(sizePolicy)
        self.frame_guestcells_title.setFrameShape(QFrame.NoFrame)
        self.frame_guestcells_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_guestcells_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_guestcells = QLabel(self.frame_guestcells_title)
        self.label_guestcells.setObjectName(u"label_guestcells")

        self.horizontalLayout_4.addWidget(self.label_guestcells)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.btn_create_cell = QPushButton(self.frame_guestcells_title)
        self.btn_create_cell.setObjectName(u"btn_create_cell")

        self.horizontalLayout_4.addWidget(self.btn_create_cell)


        self.verticalLayout.addWidget(self.frame_guestcells_title)

        self.frame_guestcells_content = QFrame(self.frame_guestcells)
        self.frame_guestcells_content.setObjectName(u"frame_guestcells_content")
        self.frame_guestcells_content.setFrameShape(QFrame.NoFrame)
        self.frame_guestcells_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_guestcells_content)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.listwidget_guestcells = QListWidget(self.frame_guestcells_content)
        self.listwidget_guestcells.setObjectName(u"listwidget_guestcells")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listwidget_guestcells.sizePolicy().hasHeightForWidth())
        self.listwidget_guestcells.setSizePolicy(sizePolicy1)
        self.listwidget_guestcells.setFrameShape(QFrame.NoFrame)
        self.listwidget_guestcells.setAutoScroll(True)
        self.listwidget_guestcells.setAlternatingRowColors(True)

        self.verticalLayout_12.addWidget(self.listwidget_guestcells)


        self.verticalLayout.addWidget(self.frame_guestcells_content)


        self.verticalLayout_7.addWidget(self.frame_guestcells)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_right)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_guestcell = QFrame(self.frame_right)
        self.frame_guestcell.setObjectName(u"frame_guestcell")
        self.frame_guestcell.setFrameShape(QFrame.NoFrame)
        self.frame_guestcell.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_guestcell)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_guestcell_title = QFrame(self.frame_guestcell)
        self.frame_guestcell_title.setObjectName(u"frame_guestcell_title")
        sizePolicy.setHeightForWidth(self.frame_guestcell_title.sizePolicy().hasHeightForWidth())
        self.frame_guestcell_title.setSizePolicy(sizePolicy)
        self.frame_guestcell_title.setFrameShape(QFrame.NoFrame)
        self.frame_guestcell_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_guestcell_title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_guestcell = QLabel(self.frame_guestcell_title)
        self.label_guestcell.setObjectName(u"label_guestcell")

        self.horizontalLayout_6.addWidget(self.label_guestcell)

        self.label_guestcell_name = QLabel(self.frame_guestcell_title)
        self.label_guestcell_name.setObjectName(u"label_guestcell_name")

        self.horizontalLayout_6.addWidget(self.label_guestcell_name)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btn_remove_cell = QPushButton(self.frame_guestcell_title)
        self.btn_remove_cell.setObjectName(u"btn_remove_cell")

        self.horizontalLayout_6.addWidget(self.btn_remove_cell)


        self.verticalLayout_9.addWidget(self.frame_guestcell_title)

        self.frame_guestcell_content = QFrame(self.frame_guestcell)
        self.frame_guestcell_content.setObjectName(u"frame_guestcell_content")
        self.frame_guestcell_content.setFrameShape(QFrame.NoFrame)
        self.frame_guestcell_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_guestcell_content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_9.addWidget(self.frame_guestcell_content)


        self.verticalLayout_8.addWidget(self.frame_guestcell)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_right)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_4.addWidget(self.frame_main)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.verticalLayout_11.addWidget(self.scrollarea)


        self.retranslateUi(GuestCellsWidget)

        QMetaObject.connectSlotsByName(GuestCellsWidget)
    # setupUi

    def retranslateUi(self, GuestCellsWidget):
        GuestCellsWidget.setWindowTitle(QCoreApplication.translate("GuestCellsWidget", u"Form", None))
        self.label_guestcells.setText(QCoreApplication.translate("GuestCellsWidget", u"\u865a\u62df\u673a\u5217\u8868", None))
        self.btn_create_cell.setText(QCoreApplication.translate("GuestCellsWidget", u"\u521b\u5efa\u865a\u62df\u673a", None))
        self.label_guestcell.setText(QCoreApplication.translate("GuestCellsWidget", u"\u865a\u62df\u673a\u914d\u7f6e", None))
        self.label_guestcell_name.setText(QCoreApplication.translate("GuestCellsWidget", u"#name", None))
        self.btn_remove_cell.setText(QCoreApplication.translate("GuestCellsWidget", u"\u5220\u9664", None))
    # retranslateUi

