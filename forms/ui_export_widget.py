# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ExportWidget(object):
    def setupUi(self, ExportWidget):
        if not ExportWidget.objectName():
            ExportWidget.setObjectName(u"ExportWidget")
        ExportWidget.resize(611, 503)
        self.verticalLayout = QVBoxLayout(ExportWidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_title = QFrame(ExportWidget)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_3.addWidget(self.label_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_close = QPushButton(self.frame_title)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_title)

        self.frame_select = QFrame(ExportWidget)
        self.frame_select.setObjectName(u"frame_select")
        self.frame_select.setFrameShape(QFrame.NoFrame)
        self.frame_select.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_select)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_select_cell = QLabel(self.frame_select)
        self.label_select_cell.setObjectName(u"label_select_cell")

        self.horizontalLayout.addWidget(self.label_select_cell)

        self.combobox_cell = QComboBox(self.frame_select)
        self.combobox_cell.setObjectName(u"combobox_cell")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_cell.sizePolicy().hasHeightForWidth())
        self.combobox_cell.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.combobox_cell)


        self.verticalLayout.addWidget(self.frame_select)

        self.frame_main = QFrame(ExportWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_gens = QFrame(self.frame_left)
        self.frame_gens.setObjectName(u"frame_gens")
        self.frame_gens.setFrameShape(QFrame.NoFrame)
        self.frame_gens.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_gens)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_gens)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_gens)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_gens)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_right)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textbrowser = QTextBrowser(self.frame_right)
        self.textbrowser.setObjectName(u"textbrowser")
        self.textbrowser.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_4.addWidget(self.textbrowser)

        self.frame_btns = QFrame(self.frame_right)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(self.frame_btns)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_4.addWidget(self.btn_save)


        self.verticalLayout_4.addWidget(self.frame_btns)


        self.horizontalLayout_2.addWidget(self.frame_right)


        self.verticalLayout.addWidget(self.frame_main)


        self.retranslateUi(ExportWidget)

        QMetaObject.connectSlotsByName(ExportWidget)
    # setupUi

    def retranslateUi(self, ExportWidget):
        ExportWidget.setWindowTitle(QCoreApplication.translate("ExportWidget", u"Form", None))
        self.label_title.setText("")
        self.btn_close.setText("")
        self.label_select_cell.setText(QCoreApplication.translate("ExportWidget", u"\u9009\u62e9Cell", None))
        self.pushButton_2.setText(QCoreApplication.translate("ExportWidget", u"cell\u914d\u7f6e\u6e90\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("ExportWidget", u"cell\u914d\u7f6e\u4e8c\u8fdb\u5236", None))
        self.textbrowser.setHtml(QCoreApplication.translate("ExportWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'SimSun';\">asdf</span></p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("ExportWidget", u"\u4fdd\u5b58", None))
    # retranslateUi

