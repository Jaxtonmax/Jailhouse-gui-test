# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpu_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CPUWidget(object):
    def setupUi(self, CPUWidget):
        if not CPUWidget.objectName():
            CPUWidget.setObjectName(u"CPUWidget")
        CPUWidget.resize(904, 696)
        self.verticalLayout_8 = QVBoxLayout(CPUWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollarea_main = QScrollArea(CPUWidget)
        self.scrollarea_main.setObjectName(u"scrollarea_main")
        self.scrollarea_main.setFrameShape(QFrame.NoFrame)
        self.scrollarea_main.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 904, 696))
        self.verticalLayout_2 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_left)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_sysinfo = QFrame(self.frame_left)
        self.frame_sysinfo.setObjectName(u"frame_sysinfo")
        self.frame_sysinfo.setFrameShape(QFrame.NoFrame)
        self.frame_sysinfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_sysinfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_sysinfo_title = QFrame(self.frame_sysinfo)
        self.frame_sysinfo_title.setObjectName(u"frame_sysinfo_title")
        self.frame_sysinfo_title.setFrameShape(QFrame.NoFrame)
        self.frame_sysinfo_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_sysinfo_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_sysinfo = QLabel(self.frame_sysinfo_title)
        self.label_sysinfo.setObjectName(u"label_sysinfo")

        self.horizontalLayout_4.addWidget(self.label_sysinfo)

        self.btn_update_from_plt = QPushButton(self.frame_sysinfo_title)
        self.btn_update_from_plt.setObjectName(u"btn_update_from_plt")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update_from_plt.sizePolicy().hasHeightForWidth())
        self.btn_update_from_plt.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.btn_update_from_plt)


        self.verticalLayout.addWidget(self.frame_sysinfo_title)

        self.frame_cpu_count = QFrame(self.frame_sysinfo)
        self.frame_cpu_count.setObjectName(u"frame_cpu_count")
        self.frame_cpu_count.setFrameShape(QFrame.NoFrame)
        self.frame_cpu_count.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_cpu_count)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineedit_cpu_count = QLineEdit(self.frame_cpu_count)
        self.lineedit_cpu_count.setObjectName(u"lineedit_cpu_count")
        self.lineedit_cpu_count.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_cpu_count, 1, 1, 1, 1)

        self.label_cpu_count = QLabel(self.frame_cpu_count)
        self.label_cpu_count.setObjectName(u"label_cpu_count")

        self.gridLayout.addWidget(self.label_cpu_count, 1, 0, 1, 1)

        self.label_cpu_count_2 = QLabel(self.frame_cpu_count)
        self.label_cpu_count_2.setObjectName(u"label_cpu_count_2")

        self.gridLayout.addWidget(self.label_cpu_count_2, 0, 0, 1, 1)

        self.lineedit_cpu_name = QLineEdit(self.frame_cpu_count)
        self.lineedit_cpu_name.setObjectName(u"lineedit_cpu_name")
        self.lineedit_cpu_name.setEnabled(False)

        self.gridLayout.addWidget(self.lineedit_cpu_name, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_cpu_count)

        self.frame_gic = QFrame(self.frame_sysinfo)
        self.frame_gic.setObjectName(u"frame_gic")
        self.frame_gic.setFrameShape(QFrame.NoFrame)
        self.frame_gic.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_gic)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_gic_title = QLabel(self.frame_gic)
        self.label_gic_title.setObjectName(u"label_gic_title")

        self.verticalLayout_3.addWidget(self.label_gic_title)

        self.frame_gic_values = QFrame(self.frame_gic)
        self.frame_gic_values.setObjectName(u"frame_gic_values")
        self.frame_gic_values.setFrameShape(QFrame.NoFrame)
        self.frame_gic_values.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_gic_values)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_gicd = QLabel(self.frame_gic_values)
        self.label_gicd.setObjectName(u"label_gicd")

        self.gridLayout_2.addWidget(self.label_gicd, 0, 0, 1, 1)

        self.label_gicr = QLabel(self.frame_gic_values)
        self.label_gicr.setObjectName(u"label_gicr")

        self.gridLayout_2.addWidget(self.label_gicr, 1, 0, 1, 1)

        self.label_gicc = QLabel(self.frame_gic_values)
        self.label_gicc.setObjectName(u"label_gicc")

        self.gridLayout_2.addWidget(self.label_gicc, 2, 0, 1, 1)

        self.label_gich = QLabel(self.frame_gic_values)
        self.label_gich.setObjectName(u"label_gich")

        self.gridLayout_2.addWidget(self.label_gich, 3, 0, 1, 1)

        self.lineedit_gicd = QLineEdit(self.frame_gic_values)
        self.lineedit_gicd.setObjectName(u"lineedit_gicd")
        self.lineedit_gicd.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_gicd, 0, 1, 1, 1)

        self.label_gicv = QLabel(self.frame_gic_values)
        self.label_gicv.setObjectName(u"label_gicv")

        self.gridLayout_2.addWidget(self.label_gicv, 4, 0, 1, 1)

        self.lineedit_gicr = QLineEdit(self.frame_gic_values)
        self.lineedit_gicr.setObjectName(u"lineedit_gicr")
        self.lineedit_gicr.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_gicr, 1, 1, 1, 1)

        self.lineedit_gicc = QLineEdit(self.frame_gic_values)
        self.lineedit_gicc.setObjectName(u"lineedit_gicc")
        self.lineedit_gicc.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_gicc, 2, 1, 1, 1)

        self.lineedit_gich = QLineEdit(self.frame_gic_values)
        self.lineedit_gich.setObjectName(u"lineedit_gich")
        self.lineedit_gich.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_gich, 3, 1, 1, 1)

        self.lineedit_gicv = QLineEdit(self.frame_gic_values)
        self.lineedit_gicv.setObjectName(u"lineedit_gicv")
        self.lineedit_gicv.setEnabled(False)

        self.gridLayout_2.addWidget(self.lineedit_gicv, 4, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_gic_values)


        self.verticalLayout.addWidget(self.frame_gic)


        self.verticalLayout_6.addWidget(self.frame_sysinfo)

        self.frame_regions = QFrame(self.frame_left)
        self.frame_regions.setObjectName(u"frame_regions")
        self.frame_regions.setFrameShape(QFrame.NoFrame)
        self.frame_regions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_regions)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_regions_title = QFrame(self.frame_regions)
        self.frame_regions_title.setObjectName(u"frame_regions_title")
        self.frame_regions_title.setFrameShape(QFrame.NoFrame)
        self.frame_regions_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_regions_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_regions = QLabel(self.frame_regions_title)
        self.label_regions.setObjectName(u"label_regions")

        self.horizontalLayout_5.addWidget(self.label_regions)


        self.verticalLayout_4.addWidget(self.frame_regions_title)

        self.frame_regions_content = QFrame(self.frame_regions)
        self.frame_regions_content.setObjectName(u"frame_regions_content")
        self.frame_regions_content.setFrameShape(QFrame.NoFrame)
        self.frame_regions_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_regions_content)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tablewidget_regions = QTableWidget(self.frame_regions_content)
        if (self.tablewidget_regions.columnCount() < 5):
            self.tablewidget_regions.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablewidget_regions.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablewidget_regions.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablewidget_regions.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablewidget_regions.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablewidget_regions.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tablewidget_regions.rowCount() < 3):
            self.tablewidget_regions.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablewidget_regions.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablewidget_regions.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tablewidget_regions.setVerticalHeaderItem(2, __qtablewidgetitem7)
        self.tablewidget_regions.setObjectName(u"tablewidget_regions")
        self.tablewidget_regions.setFrameShape(QFrame.NoFrame)
        self.tablewidget_regions.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablewidget_regions.setAutoScroll(False)
        self.tablewidget_regions.setAlternatingRowColors(True)
        self.tablewidget_regions.horizontalHeader().setVisible(True)
        self.tablewidget_regions.horizontalHeader().setHighlightSections(True)
        self.tablewidget_regions.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.tablewidget_regions)


        self.verticalLayout_4.addWidget(self.frame_regions_content)


        self.verticalLayout_6.addWidget(self.frame_regions)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_right)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_devices = QFrame(self.frame_right)
        self.frame_devices.setObjectName(u"frame_devices")
        self.frame_devices.setFrameShape(QFrame.NoFrame)
        self.frame_devices.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_devices)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_devices_title = QFrame(self.frame_devices)
        self.frame_devices_title.setObjectName(u"frame_devices_title")
        self.frame_devices_title.setFrameShape(QFrame.NoFrame)
        self.frame_devices_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_devices_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_devices = QLabel(self.frame_devices_title)
        self.label_devices.setObjectName(u"label_devices")

        self.horizontalLayout_3.addWidget(self.label_devices)


        self.verticalLayout_5.addWidget(self.frame_devices_title)

        self.frame_device_content = QFrame(self.frame_devices)
        self.frame_device_content.setObjectName(u"frame_device_content")
        self.frame_device_content.setFrameShape(QFrame.NoFrame)
        self.frame_device_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_device_content)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tablewidget_device = QTableWidget(self.frame_device_content)
        if (self.tablewidget_device.columnCount() < 4):
            self.tablewidget_device.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tablewidget_device.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tablewidget_device.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tablewidget_device.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablewidget_device.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        if (self.tablewidget_device.rowCount() < 3):
            self.tablewidget_device.setRowCount(3)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablewidget_device.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablewidget_device.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablewidget_device.setVerticalHeaderItem(2, __qtablewidgetitem14)
        self.tablewidget_device.setObjectName(u"tablewidget_device")
        self.tablewidget_device.setFrameShape(QFrame.NoFrame)
        self.tablewidget_device.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tablewidget_device.setAutoScroll(False)
        self.tablewidget_device.setAlternatingRowColors(True)
        self.tablewidget_device.horizontalHeader().setVisible(True)
        self.tablewidget_device.horizontalHeader().setHighlightSections(True)
        self.tablewidget_device.verticalHeader().setVisible(False)

        self.verticalLayout_10.addWidget(self.tablewidget_device)


        self.verticalLayout_5.addWidget(self.frame_device_content)


        self.verticalLayout_7.addWidget(self.frame_devices)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame_right)


        self.verticalLayout_2.addWidget(self.frame_main)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollarea_main.setWidget(self.scrollarea_content)

        self.verticalLayout_8.addWidget(self.scrollarea_main)


        self.retranslateUi(CPUWidget)

        QMetaObject.connectSlotsByName(CPUWidget)
    # setupUi

    def retranslateUi(self, CPUWidget):
        CPUWidget.setWindowTitle(QCoreApplication.translate("CPUWidget", u"Form", None))
        self.label_sysinfo.setText(QCoreApplication.translate("CPUWidget", u"\u7cfb\u7edf\u4fe1\u606f", None))
        self.btn_update_from_plt.setText(QCoreApplication.translate("CPUWidget", u"\u4ece\u5e73\u53f0\u66f4\u65b0", None))
        self.label_cpu_count.setText(QCoreApplication.translate("CPUWidget", u"CPU\u6838\u6570", None))
        self.label_cpu_count_2.setText(QCoreApplication.translate("CPUWidget", u"CPU\u540d\u79f0", None))
        self.label_gic_title.setText(QCoreApplication.translate("CPUWidget", u"GIC", None))
        self.label_gicd.setText(QCoreApplication.translate("CPUWidget", u"GICD Base", None))
        self.label_gicr.setText(QCoreApplication.translate("CPUWidget", u"GICR Base", None))
        self.label_gicc.setText(QCoreApplication.translate("CPUWidget", u"GICC Base", None))
        self.label_gich.setText(QCoreApplication.translate("CPUWidget", u"GICH Base", None))
        self.label_gicv.setText(QCoreApplication.translate("CPUWidget", u"GICV Base", None))
        self.label_regions.setText(QCoreApplication.translate("CPUWidget", u"\u5730\u5740\u7a7a\u95f4\u5e03\u5c40", None))
        ___qtablewidgetitem = self.tablewidget_regions.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CPUWidget", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.tablewidget_regions.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CPUWidget", u"\u5c5e\u6027", None));
        ___qtablewidgetitem2 = self.tablewidget_regions.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CPUWidget", u"\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.tablewidget_regions.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CPUWidget", u"\u5730\u5740", None));
        ___qtablewidgetitem4 = self.tablewidget_regions.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CPUWidget", u"\u5927\u5c0f", None));
        ___qtablewidgetitem5 = self.tablewidget_regions.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("CPUWidget", u"uart0", None));
        ___qtablewidgetitem6 = self.tablewidget_regions.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("CPUWidget", u"uart1", None));
        ___qtablewidgetitem7 = self.tablewidget_regions.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("CPUWidget", u"uart2", None));
        self.label_devices.setText(QCoreApplication.translate("CPUWidget", u"\u8bbe\u5907", None))
        ___qtablewidgetitem8 = self.tablewidget_device.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("CPUWidget", u"\u8bbe\u5907", None));
        ___qtablewidgetitem9 = self.tablewidget_device.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("CPUWidget", u"\u5730\u5740", None));
        ___qtablewidgetitem10 = self.tablewidget_device.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("CPUWidget", u"\u5927\u5c0f", None));
        ___qtablewidgetitem11 = self.tablewidget_device.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("CPUWidget", u"\u4e2d\u65ad", None));
        ___qtablewidgetitem12 = self.tablewidget_device.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("CPUWidget", u"uart0", None));
        ___qtablewidgetitem13 = self.tablewidget_device.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("CPUWidget", u"uart1", None));
        ___qtablewidgetitem14 = self.tablewidget_device.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("CPUWidget", u"uart2", None));
    # retranslateUi

