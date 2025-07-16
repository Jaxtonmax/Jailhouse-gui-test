# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateWidget(object):
    def setupUi(self, CreateWidget):
        if not CreateWidget.objectName():
            CreateWidget.setObjectName(u"CreateWidget")
        CreateWidget.resize(559, 344)
        self.verticalLayout_2 = QVBoxLayout(CreateWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_win_title = QFrame(CreateWidget)
        self.frame_win_title.setObjectName(u"frame_win_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_win_title.sizePolicy().hasHeightForWidth())
        self.frame_win_title.setSizePolicy(sizePolicy)
        self.frame_win_title.setFrameShape(QFrame.NoFrame)
        self.frame_win_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_win_title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.label_win_title = QLabel(self.frame_win_title)
        self.label_win_title.setObjectName(u"label_win_title")

        self.horizontalLayout_3.addWidget(self.label_win_title)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_close = QPushButton(self.frame_win_title)
        self.btn_close.setObjectName(u"btn_close")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout_2.addWidget(self.frame_win_title)

        self.frame_content = QFrame(CreateWidget)
        self.frame_content.setObjectName(u"frame_content")
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame_select_mode = QFrame(self.frame_content)
        self.frame_select_mode.setObjectName(u"frame_select_mode")
        sizePolicy.setHeightForWidth(self.frame_select_mode.sizePolicy().hasHeightForWidth())
        self.frame_select_mode.setSizePolicy(sizePolicy)
        self.frame_select_mode.setFrameShape(QFrame.NoFrame)
        self.frame_select_mode.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_select_mode)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radiobtn_new = QRadioButton(self.frame_select_mode)
        self.radiobtn_new.setObjectName(u"radiobtn_new")

        self.horizontalLayout.addWidget(self.radiobtn_new)

        self.radiobtn_demo = QRadioButton(self.frame_select_mode)
        self.radiobtn_demo.setObjectName(u"radiobtn_demo")

        self.horizontalLayout.addWidget(self.radiobtn_demo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_select_mode)

        self.frame_param = QFrame(self.frame_content)
        self.frame_param.setObjectName(u"frame_param")
        self.frame_param.setFrameShape(QFrame.NoFrame)
        self.frame_param.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_param)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_name = QLabel(self.frame_param)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)

        self.lineedit_name = QLineEdit(self.frame_param)
        self.lineedit_name.setObjectName(u"lineedit_name")

        self.gridLayout.addWidget(self.lineedit_name, 0, 1, 1, 1)

        self.stackedwidget_params = QStackedWidget(self.frame_param)
        self.stackedwidget_params.setObjectName(u"stackedwidget_params")
        sizePolicy.setHeightForWidth(self.stackedwidget_params.sizePolicy().hasHeightForWidth())
        self.stackedwidget_params.setSizePolicy(sizePolicy)
        self.page_new = QWidget()
        self.page_new.setObjectName(u"page_new")
        self.gridLayout_3 = QGridLayout(self.page_new)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_platform = QLabel(self.page_new)
        self.label_platform.setObjectName(u"label_platform")

        self.gridLayout_3.addWidget(self.label_platform, 1, 0, 1, 1)

        self.combobox_platform = QComboBox(self.page_new)
        self.combobox_platform.setObjectName(u"combobox_platform")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combobox_platform.sizePolicy().hasHeightForWidth())
        self.combobox_platform.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.combobox_platform, 1, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.stackedwidget_params.addWidget(self.page_new)
        self.page_demo = QWidget()
        self.page_demo.setObjectName(u"page_demo")
        self.gridLayout_4 = QGridLayout(self.page_demo)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_demo = QLabel(self.page_demo)
        self.label_demo.setObjectName(u"label_demo")

        self.gridLayout_4.addWidget(self.label_demo, 0, 0, 1, 1)

        self.combobox_demo = QComboBox(self.page_demo)
        self.combobox_demo.setObjectName(u"combobox_demo")
        sizePolicy.setHeightForWidth(self.combobox_demo.sizePolicy().hasHeightForWidth())
        self.combobox_demo.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.combobox_demo, 0, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.stackedwidget_params.addWidget(self.page_demo)

        self.gridLayout.addWidget(self.stackedwidget_params, 1, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_param)

        self.frame_bottom = QFrame(self.frame_content)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_btns = QFrame(self.frame_bottom)
        self.frame_btns.setObjectName(u"frame_btns")
        sizePolicy.setHeightForWidth(self.frame_btns.sizePolicy().hasHeightForWidth())
        self.frame_btns.setSizePolicy(sizePolicy)
        self.frame_btns.setFrameShape(QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.frame_btns)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_create = QPushButton(self.frame_btns)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout_2.addWidget(self.btn_create)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.frame_btns)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_bottom)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.retranslateUi(CreateWidget)

        self.stackedwidget_params.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(CreateWidget)
    # setupUi

    def retranslateUi(self, CreateWidget):
        CreateWidget.setWindowTitle(QCoreApplication.translate("CreateWidget", u"Form", None))
        self.label_win_title.setText(QCoreApplication.translate("CreateWidget", u"\u65b0\u5efa\u914d\u7f6e", None))
        self.btn_close.setText("")
        self.radiobtn_new.setText(QCoreApplication.translate("CreateWidget", u"\u65b0\u914d\u7f6e", None))
        self.radiobtn_demo.setText(QCoreApplication.translate("CreateWidget", u"Demo\u914d\u7f6e", None))
        self.label_name.setText(QCoreApplication.translate("CreateWidget", u"\u540d\u79f0", None))
        self.label_platform.setText(QCoreApplication.translate("CreateWidget", u"\u786c\u4ef6\u5e73\u53f0", None))
        self.label_demo.setText(QCoreApplication.translate("CreateWidget", u"Demo", None))
        self.btn_cancel.setText(QCoreApplication.translate("CreateWidget", u"\u53d6\u6d88", None))
        self.btn_create.setText(QCoreApplication.translate("CreateWidget", u"\u521b\u5efa", None))
    # retranslateUi

