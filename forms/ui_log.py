# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        if not LogWidget.objectName():
            LogWidget.setObjectName(u"LogWidget")
        LogWidget.resize(424, 215)
        self.verticalLayout = QVBoxLayout(LogWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(LogWidget)
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
        self.horizontalLayout.setContentsMargins(11, 0, 11, 0)
        self.label_icon = QLabel(self.frame_title)
        self.label_icon.setObjectName(u"label_icon")

        self.horizontalLayout.addWidget(self.label_icon)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout.addWidget(self.label_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frame_title)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.combobox_level = QComboBox(self.frame_title)
        self.combobox_level.setObjectName(u"combobox_level")
        self.combobox_level.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.combobox_level)

        self.btn_clean = QPushButton(self.frame_title)
        self.btn_clean.setObjectName(u"btn_clean")
        self.btn_clean.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_clean)


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


        self.retranslateUi(LogWidget)

        QMetaObject.connectSlotsByName(LogWidget)
    # setupUi

    def retranslateUi(self, LogWidget):
        LogWidget.setWindowTitle(QCoreApplication.translate("LogWidget", u"Form", None))
        self.label_icon.setText("")
        self.label_title.setText(QCoreApplication.translate("LogWidget", u"\u65e5\u5fd7", None))
        self.label.setText(QCoreApplication.translate("LogWidget", u"\u65e5\u5fd7\u7b49\u7ea7", None))
        self.btn_clean.setText("")
        self.textbrowser.setHtml(QCoreApplication.translate("LogWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

