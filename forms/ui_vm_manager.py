# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vm_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VMManageWidget(object):
    def setupUi(self, VMManageWidget):
        if not VMManageWidget.objectName():
            VMManageWidget.setObjectName(u"VMManageWidget")
        VMManageWidget.resize(1067, 769)
        self.horizontalLayout_2 = QHBoxLayout(VMManageWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(VMManageWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setFrameShape(QFrame.NoFrame)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 1067, 769))
        self.verticalLayout = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left.sizePolicy().hasHeightForWidth())
        self.frame_left.setSizePolicy(sizePolicy)
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_connect = QFrame(self.frame_left)
        self.frame_connect.setObjectName(u"frame_connect")
        self.frame_connect.setFrameShape(QFrame.NoFrame)
        self.frame_connect.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_connect)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_connect_title = QFrame(self.frame_connect)
        self.frame_connect_title.setObjectName(u"frame_connect_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_connect_title.sizePolicy().hasHeightForWidth())
        self.frame_connect_title.setSizePolicy(sizePolicy1)
        self.frame_connect_title.setFrameShape(QFrame.NoFrame)
        self.frame_connect_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_connect_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_connect_title)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_connect_title)

        self.frame_content = QFrame(self.frame_connect)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_addr = QFrame(self.frame_content)
        self.frame_addr.setObjectName(u"frame_addr")
        self.frame_addr.setFrameShape(QFrame.NoFrame)
        self.frame_addr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_addr)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineedit_addr = QLineEdit(self.frame_addr)
        self.lineedit_addr.setObjectName(u"lineedit_addr")

        self.horizontalLayout_4.addWidget(self.lineedit_addr)

        self.btn_connect = QPushButton(self.frame_addr)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.btn_connect)


        self.verticalLayout_3.addWidget(self.frame_addr)

        self.frame_hyp_ctrl = QFrame(self.frame_content)
        self.frame_hyp_ctrl.setObjectName(u"frame_hyp_ctrl")
        self.frame_hyp_ctrl.setFrameShape(QFrame.NoFrame)
        self.frame_hyp_ctrl.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_hyp_ctrl)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_hyp_ctrl)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_hyp_stop = QPushButton(self.frame_hyp_ctrl)
        self.btn_hyp_stop.setObjectName(u"btn_hyp_stop")
        self.btn_hyp_stop.setCheckable(False)

        self.horizontalLayout_7.addWidget(self.btn_hyp_stop)

        self.btn_hyp_start = QPushButton(self.frame_hyp_ctrl)
        self.btn_hyp_start.setObjectName(u"btn_hyp_start")
        self.btn_hyp_start.setCheckable(False)

        self.horizontalLayout_7.addWidget(self.btn_hyp_start)


        self.verticalLayout_3.addWidget(self.frame_hyp_ctrl)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.verticalLayout_4.addWidget(self.frame_connect)

        self.frame_cells = QFrame(self.frame_left)
        self.frame_cells.setObjectName(u"frame_cells")
        self.frame_cells.setFrameShape(QFrame.NoFrame)
        self.frame_cells.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_cells)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_cells_title = QFrame(self.frame_cells)
        self.frame_cells_title.setObjectName(u"frame_cells_title")
        self.frame_cells_title.setFrameShape(QFrame.NoFrame)
        self.frame_cells_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_cells_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_cells_title)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.btn_cell_flush = QPushButton(self.frame_cells_title)
        self.btn_cell_flush.setObjectName(u"btn_cell_flush")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_cell_flush.sizePolicy().hasHeightForWidth())
        self.btn_cell_flush.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.btn_cell_flush)


        self.verticalLayout_6.addWidget(self.frame_cells_title)

        self.frame_cells_content = QFrame(self.frame_cells)
        self.frame_cells_content.setObjectName(u"frame_cells_content")
        self.frame_cells_content.setFrameShape(QFrame.NoFrame)
        self.frame_cells_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_cells_content)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listwidget_cells = QListWidget(self.frame_cells_content)
        self.listwidget_cells.setObjectName(u"listwidget_cells")
        sizePolicy.setHeightForWidth(self.listwidget_cells.sizePolicy().hasHeightForWidth())
        self.listwidget_cells.setSizePolicy(sizePolicy)
        self.listwidget_cells.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_7.addWidget(self.listwidget_cells)


        self.verticalLayout_6.addWidget(self.frame_cells_content)


        self.verticalLayout_4.addWidget(self.frame_cells)

        self.frame_rootcell = QFrame(self.frame_left)
        self.frame_rootcell.setObjectName(u"frame_rootcell")
        self.frame_rootcell.setFrameShape(QFrame.NoFrame)
        self.frame_rootcell.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_rootcell)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_rootcell_title = QFrame(self.frame_rootcell)
        self.frame_rootcell_title.setObjectName(u"frame_rootcell_title")
        self.frame_rootcell_title.setFrameShape(QFrame.NoFrame)
        self.frame_rootcell_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_rootcell_title)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_rootcell_title)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_8.addWidget(self.frame_rootcell_title)

        self.frame_rootcell_content = QFrame(self.frame_rootcell)
        self.frame_rootcell_content.setObjectName(u"frame_rootcell_content")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_rootcell_content.sizePolicy().hasHeightForWidth())
        self.frame_rootcell_content.setSizePolicy(sizePolicy3)
        self.frame_rootcell_content.setFrameShape(QFrame.NoFrame)
        self.frame_rootcell_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_rootcell_content)


        self.verticalLayout_4.addWidget(self.frame_rootcell)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        sizePolicy.setHeightForWidth(self.frame_right.sizePolicy().hasHeightForWidth())
        self.frame_right.setSizePolicy(sizePolicy)
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_right)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_runcell = QFrame(self.frame_right)
        self.frame_runcell.setObjectName(u"frame_runcell")
        self.frame_runcell.setFrameShape(QFrame.NoFrame)
        self.frame_runcell.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_runcell)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_runcell_title = QFrame(self.frame_runcell)
        self.frame_runcell_title.setObjectName(u"frame_runcell_title")
        self.frame_runcell_title.setFrameShape(QFrame.NoFrame)
        self.frame_runcell_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_runcell_title)
        self.horizontalLayout_8.setSpacing(12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_runcell_title)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.label_cellname = QLabel(self.frame_runcell_title)
        self.label_cellname.setObjectName(u"label_cellname")

        self.horizontalLayout_8.addWidget(self.label_cellname)


        self.verticalLayout_9.addWidget(self.frame_runcell_title)

        self.frame_runcell_content = QFrame(self.frame_runcell)
        self.frame_runcell_content.setObjectName(u"frame_runcell_content")
        self.frame_runcell_content.setFrameShape(QFrame.NoFrame)
        self.frame_runcell_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_runcell_content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_os_runinfo_title = QFrame(self.frame_runcell_content)
        self.frame_os_runinfo_title.setObjectName(u"frame_os_runinfo_title")
        self.frame_os_runinfo_title.setFrameShape(QFrame.NoFrame)
        self.frame_os_runinfo_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_os_runinfo_title)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_loadimg_os_tag = QLabel(self.frame_os_runinfo_title)
        self.label_loadimg_os_tag.setObjectName(u"label_loadimg_os_tag")
        sizePolicy4.setHeightForWidth(self.label_loadimg_os_tag.sizePolicy().hasHeightForWidth())
        self.label_loadimg_os_tag.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.label_loadimg_os_tag)

        self.label_7 = QLabel(self.frame_os_runinfo_title)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.frame_os_runinfo_title)

        self.frame_os_runinfo_content = QFrame(self.frame_runcell_content)
        self.frame_os_runinfo_content.setObjectName(u"frame_os_runinfo_content")
        sizePolicy1.setHeightForWidth(self.frame_os_runinfo_content.sizePolicy().hasHeightForWidth())
        self.frame_os_runinfo_content.setSizePolicy(sizePolicy1)
        self.frame_os_runinfo_content.setFrameShape(QFrame.NoFrame)
        self.frame_os_runinfo_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_os_runinfo_content)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_select_os = QFrame(self.frame_os_runinfo_content)
        self.frame_select_os.setObjectName(u"frame_select_os")
        self.frame_select_os.setFrameShape(QFrame.NoFrame)
        self.frame_select_os.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_select_os)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_select_os)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.combobox_os_type = QComboBox(self.frame_select_os)
        self.combobox_os_type.setObjectName(u"combobox_os_type")

        self.horizontalLayout_12.addWidget(self.combobox_os_type)


        self.verticalLayout_11.addWidget(self.frame_select_os)

        self.stackedwidget_os_runinfo = QStackedWidget(self.frame_os_runinfo_content)
        self.stackedwidget_os_runinfo.setObjectName(u"stackedwidget_os_runinfo")
        self.stackedwidget_os_runinfo.setMinimumSize(QSize(0, 0))

        self.verticalLayout_11.addWidget(self.stackedwidget_os_runinfo)


        self.verticalLayout_10.addWidget(self.frame_os_runinfo_content)

        self.frame_sd_img_title = QFrame(self.frame_runcell_content)
        self.frame_sd_img_title.setObjectName(u"frame_sd_img_title")
        self.frame_sd_img_title.setFrameShape(QFrame.NoFrame)
        self.frame_sd_img_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_sd_img_title)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_loadimg_sd_tag = QLabel(self.frame_sd_img_title)
        self.label_loadimg_sd_tag.setObjectName(u"label_loadimg_sd_tag")
        sizePolicy4.setHeightForWidth(self.label_loadimg_sd_tag.sizePolicy().hasHeightForWidth())
        self.label_loadimg_sd_tag.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label_loadimg_sd_tag)

        self.label_8 = QLabel(self.frame_sd_img_title)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_11.addWidget(self.label_8)


        self.verticalLayout_10.addWidget(self.frame_sd_img_title)

        self.frame_sd_img_content = QFrame(self.frame_runcell_content)
        self.frame_sd_img_content.setObjectName(u"frame_sd_img_content")
        self.frame_sd_img_content.setFrameShape(QFrame.NoFrame)
        self.frame_sd_img_content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_sd_img_content)

        self.frame_runcell_btns = QFrame(self.frame_runcell_content)
        self.frame_runcell_btns.setObjectName(u"frame_runcell_btns")
        self.frame_runcell_btns.setFrameShape(QFrame.NoFrame)
        self.frame_runcell_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_runcell_btns)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.btn_cell_stop = QPushButton(self.frame_runcell_btns)
        self.btn_cell_stop.setObjectName(u"btn_cell_stop")

        self.horizontalLayout_9.addWidget(self.btn_cell_stop)

        self.btn_cell_run = QPushButton(self.frame_runcell_btns)
        self.btn_cell_run.setObjectName(u"btn_cell_run")

        self.horizontalLayout_9.addWidget(self.btn_cell_run)


        self.verticalLayout_10.addWidget(self.frame_runcell_btns)


        self.verticalLayout_9.addWidget(self.frame_runcell_content)


        self.verticalLayout_5.addWidget(self.frame_runcell)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_right)


        self.verticalLayout.addWidget(self.frame_main)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.horizontalLayout_2.addWidget(self.scrollarea)


        self.retranslateUi(VMManageWidget)

        QMetaObject.connectSlotsByName(VMManageWidget)
    # setupUi

    def retranslateUi(self, VMManageWidget):
        VMManageWidget.setWindowTitle(QCoreApplication.translate("VMManageWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("VMManageWidget", u"\u8fdc\u7a0b\u8fde\u63a5", None))
        self.lineedit_addr.setText(QCoreApplication.translate("VMManageWidget", u"tcp://127.0.0.1:9492", None))
        self.btn_connect.setText(QCoreApplication.translate("VMManageWidget", u"\u8fde\u63a5", None))
        self.label_4.setText(QCoreApplication.translate("VMManageWidget", u"Hypervisor\u63a7\u5236", None))
        self.btn_hyp_stop.setText(QCoreApplication.translate("VMManageWidget", u"\u505c\u6b62", None))
        self.btn_hyp_start.setText(QCoreApplication.translate("VMManageWidget", u"\u542f\u52a8", None))
        self.label_2.setText(QCoreApplication.translate("VMManageWidget", u"\u865a\u62df\u673a\u72b6\u6001\u5217\u8868", None))
        self.btn_cell_flush.setText(QCoreApplication.translate("VMManageWidget", u"\u5237\u65b0", None))
        self.label_3.setText(QCoreApplication.translate("VMManageWidget", u"Root Cell\u72b6\u6001", None))
        self.label_5.setText(QCoreApplication.translate("VMManageWidget", u"\u8fd0\u884c\u865a\u62df\u673a", None))
        self.label_cellname.setText("")
        self.label_loadimg_os_tag.setText("")
        self.label_7.setText(QCoreApplication.translate("VMManageWidget", u"\u64cd\u4f5c\u7cfb\u7edf\u8fd0\u884c\u4fe1\u606f", None))
        self.label_6.setText(QCoreApplication.translate("VMManageWidget", u"\u9009\u62e9\u64cd\u4f5c\u7cfb\u7edf", None))
        self.label_loadimg_sd_tag.setText("")
        self.label_8.setText(QCoreApplication.translate("VMManageWidget", u"\u81ea\u5b9a\u4e49\u955c\u50cf", None))
        self.btn_cell_stop.setText(QCoreApplication.translate("VMManageWidget", u"\u505c\u6b62", None))
        self.btn_cell_run.setText(QCoreApplication.translate("VMManageWidget", u"\u542f\u52a8", None))
    # retranslateUi

