# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 659)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_window_title = QFrame(MainWindow)
        self.frame_window_title.setObjectName(u"frame_window_title")
        self.frame_window_title.setFrameShape(QFrame.StyledPanel)
        self.frame_window_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_window_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_logo = QPushButton(self.frame_window_title)
        self.btn_logo.setObjectName(u"btn_logo")
        self.btn_logo.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_logo)

        self.label_title = QLabel(self.frame_window_title)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout.addWidget(self.label_title)

        self.label_version = QLabel(self.frame_window_title)
        self.label_version.setObjectName(u"label_version")

        self.horizontalLayout.addWidget(self.label_version)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.frame_window_title)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_window_title)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_window_title)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_window_title)

        self.splitter = QSplitter(MainWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(0)
        self.stacked_widget = QStackedWidget(self.splitter)
        self.stacked_widget.setObjectName(u"stacked_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stacked_widget.sizePolicy().hasHeightForWidth())
        self.stacked_widget.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.stacked_widget)
        self.frame_tools = QFrame(self.splitter)
        self.frame_tools.setObjectName(u"frame_tools")
        self.frame_tools.setFrameShape(QFrame.NoFrame)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tools)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.splitter.addWidget(self.frame_tools)

        self.verticalLayout.addWidget(self.splitter)

        self.frame_status = QFrame(MainWindow)
        self.frame_status.setObjectName(u"frame_status")
        self.frame_status.setFrameShape(QFrame.NoFrame)
        self.frame_status.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_status)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_check = QPushButton(self.frame_status)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_check)

        self.btn_tip = QPushButton(self.frame_status)
        self.btn_tip.setObjectName(u"btn_tip")
        self.btn_tip.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_tip)

        self.btn_log = QPushButton(self.frame_status)
        self.btn_log.setObjectName(u"btn_log")
        self.btn_log.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.btn_log)


        self.verticalLayout.addWidget(self.frame_status)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.btn_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u865a\u62df\u5316\u914d\u7f6e\u7ba1\u7406\u5e73\u53f0", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v0.0", None))
        self.btn_minimize.setText("")
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5", None))
        self.btn_tip.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u793a", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
    # retranslateUi

