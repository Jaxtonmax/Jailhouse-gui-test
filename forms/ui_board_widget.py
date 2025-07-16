# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'board_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BoardWidget(object):
    def setupUi(self, BoardWidget):
        if not BoardWidget.objectName():
            BoardWidget.setObjectName(u"BoardWidget")
        BoardWidget.resize(663, 471)
        self.verticalLayout_5 = QVBoxLayout(BoardWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(BoardWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 661, 469))
        self.verticalLayout_4 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.scrollarea_content)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_content)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_left = QFrame(self.frame_content)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_left)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_system = QFrame(self.frame_left)
        self.frame_system.setObjectName(u"frame_system")
        self.frame_system.setFrameShape(QFrame.NoFrame)
        self.frame_system.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_system)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_system_title = QFrame(self.frame_system)
        self.frame_system_title.setObjectName(u"frame_system_title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_system_title.sizePolicy().hasHeightForWidth())
        self.frame_system_title.setSizePolicy(sizePolicy)
        self.frame_system_title.setFrameShape(QFrame.NoFrame)
        self.frame_system_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_system_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_system_title)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_update_from_plt = QPushButton(self.frame_system_title)
        self.btn_update_from_plt.setObjectName(u"btn_update_from_plt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_update_from_plt.sizePolicy().hasHeightForWidth())
        self.btn_update_from_plt.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.btn_update_from_plt)


        self.verticalLayout.addWidget(self.frame_system_title)

        self.frame_system_content = QFrame(self.frame_system)
        self.frame_system_content.setObjectName(u"frame_system_content")
        self.frame_system_content.setFrameShape(QFrame.NoFrame)
        self.frame_system_content.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_system_content)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_model_title = QLabel(self.frame_system_content)
        self.label_model_title.setObjectName(u"label_model_title")

        self.gridLayout.addWidget(self.label_model_title, 0, 0, 1, 1)

        self.label_model = QLabel(self.frame_system_content)
        self.label_model.setObjectName(u"label_model")

        self.gridLayout.addWidget(self.label_model, 0, 1, 1, 1)

        self.label_vendor_title = QLabel(self.frame_system_content)
        self.label_vendor_title.setObjectName(u"label_vendor_title")

        self.gridLayout.addWidget(self.label_vendor_title, 1, 0, 1, 1)

        self.label_vendor = QLabel(self.frame_system_content)
        self.label_vendor.setObjectName(u"label_vendor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_vendor.sizePolicy().hasHeightForWidth())
        self.label_vendor.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.label_vendor, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_system_content)


        self.verticalLayout_7.addWidget(self.frame_system)

        self.frame_mem = QFrame(self.frame_left)
        self.frame_mem.setObjectName(u"frame_mem")
        self.frame_mem.setFrameShape(QFrame.NoFrame)
        self.frame_mem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_mem)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_mem_title = QFrame(self.frame_mem)
        self.frame_mem_title.setObjectName(u"frame_mem_title")
        sizePolicy.setHeightForWidth(self.frame_mem_title.sizePolicy().hasHeightForWidth())
        self.frame_mem_title.setSizePolicy(sizePolicy)
        self.frame_mem_title.setFrameShape(QFrame.NoFrame)
        self.frame_mem_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_mem_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame_mem_title)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.frame_mem_title)

        self.frame_mem_content = QFrame(self.frame_mem)
        self.frame_mem_content.setObjectName(u"frame_mem_content")
        self.frame_mem_content.setFrameShape(QFrame.NoFrame)
        self.frame_mem_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_mem_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_board_mems = QFrame(self.frame_mem_content)
        self.frame_board_mems.setObjectName(u"frame_board_mems")
        self.frame_board_mems.setFrameShape(QFrame.NoFrame)
        self.frame_board_mems.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_board_mems)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")

        self.verticalLayout_3.addWidget(self.frame_board_mems)


        self.verticalLayout_2.addWidget(self.frame_mem_content)


        self.verticalLayout_7.addWidget(self.frame_mem)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_content)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_right)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_cpus = QFrame(self.frame_right)
        self.frame_cpus.setObjectName(u"frame_cpus")
        self.frame_cpus.setFrameShape(QFrame.NoFrame)
        self.frame_cpus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_cpus)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_cpus_title = QFrame(self.frame_cpus)
        self.frame_cpus_title.setObjectName(u"frame_cpus_title")
        self.frame_cpus_title.setFrameShape(QFrame.NoFrame)
        self.frame_cpus_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_cpus_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_cpus_title)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.verticalLayout_10.addWidget(self.frame_cpus_title)

        self.frame_cpus_content = QFrame(self.frame_cpus)
        self.frame_cpus_content.setObjectName(u"frame_cpus_content")
        self.frame_cpus_content.setFrameShape(QFrame.NoFrame)
        self.frame_cpus_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_cpus_content)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_10.addWidget(self.frame_cpus_content)


        self.verticalLayout_8.addWidget(self.frame_cpus)

        self.frame_devices = QFrame(self.frame_right)
        self.frame_devices.setObjectName(u"frame_devices")
        self.frame_devices.setFrameShape(QFrame.NoFrame)
        self.frame_devices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_devices)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_devices_title = QFrame(self.frame_devices)
        self.frame_devices_title.setObjectName(u"frame_devices_title")
        sizePolicy.setHeightForWidth(self.frame_devices_title.sizePolicy().hasHeightForWidth())
        self.frame_devices_title.setSizePolicy(sizePolicy)
        self.frame_devices_title.setFrameShape(QFrame.NoFrame)
        self.frame_devices_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_devices_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.frame_devices_title)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_4)


        self.verticalLayout_9.addWidget(self.frame_devices_title)

        self.frame_devices_content = QFrame(self.frame_devices)
        self.frame_devices_content.setObjectName(u"frame_devices_content")
        self.frame_devices_content.setFrameShape(QFrame.NoFrame)
        self.frame_devices_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_devices_content)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_devices_items = QFrame(self.frame_devices_content)
        self.frame_devices_items.setObjectName(u"frame_devices_items")
        self.frame_devices_items.setFrameShape(QFrame.NoFrame)
        self.frame_devices_items.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_devices_items)


        self.verticalLayout_9.addWidget(self.frame_devices_content)


        self.verticalLayout_8.addWidget(self.frame_devices)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame_right)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.verticalLayout_5.addWidget(self.scrollarea)


        self.retranslateUi(BoardWidget)

        QMetaObject.connectSlotsByName(BoardWidget)
    # setupUi

    def retranslateUi(self, BoardWidget):
        BoardWidget.setWindowTitle(QCoreApplication.translate("BoardWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("BoardWidget", u"\u7cfb\u7edf", None))
        self.btn_update_from_plt.setText(QCoreApplication.translate("BoardWidget", u"\u4ece\u5e73\u53f0\u66f4\u65b0", None))
        self.label_model_title.setText(QCoreApplication.translate("BoardWidget", u"\u578b\u53f7", None))
        self.label_model.setText(QCoreApplication.translate("BoardWidget", u"#model", None))
        self.label_vendor_title.setText(QCoreApplication.translate("BoardWidget", u"\u5382\u5546", None))
        self.label_vendor.setText(QCoreApplication.translate("BoardWidget", u"#vendor", None))
        self.label_2.setText(QCoreApplication.translate("BoardWidget", u"\u5185\u5b58", None))
        self.label_3.setText(QCoreApplication.translate("BoardWidget", u"CPU", None))
        self.label_4.setText(QCoreApplication.translate("BoardWidget", u"\u8bbe\u5907", None))
    # retranslateUi

