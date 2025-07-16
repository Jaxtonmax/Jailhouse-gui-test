# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainPageWidget(object):
    def setupUi(self, MainPageWidget):
        if not MainPageWidget.objectName():
            MainPageWidget.setObjectName(u"MainPageWidget")
        MainPageWidget.resize(767, 731)
        self.verticalLayout_2 = QVBoxLayout(MainPageWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_toolbar = QFrame(MainPageWidget)
        self.frame_toolbar.setObjectName(u"frame_toolbar")
        self.frame_toolbar.setFrameShape(QFrame.NoFrame)
        self.frame_toolbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_toolbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save_and_exit = QPushButton(self.frame_toolbar)
        self.btn_save_and_exit.setObjectName(u"btn_save_and_exit")

        self.horizontalLayout.addWidget(self.btn_save_and_exit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_name = QLabel(self.frame_toolbar)
        self.label_name.setObjectName(u"label_name")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_name)

        self.label_state = QLabel(self.frame_toolbar)
        self.label_state.setObjectName(u"label_state")

        self.horizontalLayout.addWidget(self.label_state)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(self.frame_toolbar)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_export = QPushButton(self.frame_toolbar)
        self.btn_export.setObjectName(u"btn_export")

        self.horizontalLayout.addWidget(self.btn_export)


        self.verticalLayout_2.addWidget(self.frame_toolbar)

        self.frame_main = QFrame(MainPageWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_cav = QFrame(self.frame_main)
        self.frame_cav.setObjectName(u"frame_cav")
        self.frame_cav.setFrameShape(QFrame.NoFrame)
        self.frame_cav.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_cav)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_hw_platform = QPushButton(self.frame_cav)
        self.btn_hw_platform.setObjectName(u"btn_hw_platform")
        self.btn_hw_platform.setMouseTracking(False)
        self.btn_hw_platform.setAutoFillBackground(True)
        self.btn_hw_platform.setCheckable(True)
        self.btn_hw_platform.setAutoExclusive(True)
        self.btn_hw_platform.setFlat(True)

        self.verticalLayout.addWidget(self.btn_hw_platform)

        self.btn_vm_config = QPushButton(self.frame_cav)
        self.btn_vm_config.setObjectName(u"btn_vm_config")
        self.btn_vm_config.setMouseTracking(False)
        self.btn_vm_config.setAutoFillBackground(True)
        self.btn_vm_config.setCheckable(True)
        self.btn_vm_config.setAutoExclusive(True)
        self.btn_vm_config.setFlat(True)

        self.verticalLayout.addWidget(self.btn_vm_config)

        self.btn_vm_manage = QPushButton(self.frame_cav)
        self.btn_vm_manage.setObjectName(u"btn_vm_manage")
        self.btn_vm_manage.setMouseTracking(False)
        self.btn_vm_manage.setAutoFillBackground(True)
        self.btn_vm_manage.setCheckable(True)
        self.btn_vm_manage.setAutoExclusive(True)
        self.btn_vm_manage.setFlat(True)

        self.verticalLayout.addWidget(self.btn_vm_manage)

        self.verticalSpacer = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_cav)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_right)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stacked_widget = QStackedWidget(self.frame_right)
        self.stacked_widget.setObjectName(u"stacked_widget")

        self.verticalLayout_3.addWidget(self.stacked_widget)


        self.horizontalLayout_2.addWidget(self.frame_right)


        self.verticalLayout_2.addWidget(self.frame_main)


        self.retranslateUi(MainPageWidget)

        QMetaObject.connectSlotsByName(MainPageWidget)
    # setupUi

    def retranslateUi(self, MainPageWidget):
        MainPageWidget.setWindowTitle(QCoreApplication.translate("MainPageWidget", u"Form", None))
        self.btn_save_and_exit.setText(QCoreApplication.translate("MainPageWidget", u"\u4fdd\u5b58\u5e76\u8fd4\u56de", None))
        self.label_name.setText(QCoreApplication.translate("MainPageWidget", u"#name", None))
        self.label_state.setText(QCoreApplication.translate("MainPageWidget", u"#state", None))
        self.btn_save.setText(QCoreApplication.translate("MainPageWidget", u"\u4fdd\u5b58", None))
        self.btn_export.setText(QCoreApplication.translate("MainPageWidget", u"\u5bfc\u51fa", None))
        self.btn_hw_platform.setText(QCoreApplication.translate("MainPageWidget", u"\u786c\u4ef6\u5e73\u53f0", None))
        self.btn_vm_config.setText(QCoreApplication.translate("MainPageWidget", u"\u865a\u62df\u673a\u914d\u7f6e", None))
        self.btn_vm_manage.setText(QCoreApplication.translate("MainPageWidget", u"\u865a\u62df\u673a\u7ba1\u7406", None))
    # retranslateUi

