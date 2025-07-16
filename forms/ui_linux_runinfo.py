# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linux_runinfo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LinuxRunInfoWidget(object):
    def setupUi(self, LinuxRunInfoWidget):
        if not LinuxRunInfoWidget.objectName():
            LinuxRunInfoWidget.setObjectName(u"LinuxRunInfoWidget")
        LinuxRunInfoWidget.resize(546, 478)
        self.verticalLayout = QVBoxLayout(LinuxRunInfoWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(LinuxRunInfoWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_msl = QFrame(self.frame)
        self.frame_msl.setObjectName(u"frame_msl")
        self.frame_msl.setFrameShape(QFrame.NoFrame)
        self.frame_msl.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_msl)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.label_4 = QLabel(self.frame_msl)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineedit_kernel_path = QLineEdit(self.frame_msl)
        self.lineedit_kernel_path.setObjectName(u"lineedit_kernel_path")

        self.gridLayout_2.addWidget(self.lineedit_kernel_path, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame_msl)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)

        self.btn_select_kernel = QPushButton(self.frame_msl)
        self.btn_select_kernel.setObjectName(u"btn_select_kernel")
        self.btn_select_kernel.setFlat(True)

        self.gridLayout_2.addWidget(self.btn_select_kernel, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_msl)

        self.frame_msl_2 = QFrame(self.frame)
        self.frame_msl_2.setObjectName(u"frame_msl_2")
        self.frame_msl_2.setFrameShape(QFrame.NoFrame)
        self.frame_msl_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_msl_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(7, 7, 7, 7)
        self.label_5 = QLabel(self.frame_msl_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineedit_devicetree_path = QLineEdit(self.frame_msl_2)
        self.lineedit_devicetree_path.setObjectName(u"lineedit_devicetree_path")

        self.gridLayout_3.addWidget(self.lineedit_devicetree_path, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_msl_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 2)

        self.btn_select_devicetree = QPushButton(self.frame_msl_2)
        self.btn_select_devicetree.setObjectName(u"btn_select_devicetree")
        self.btn_select_devicetree.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_select_devicetree, 1, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_msl_2)

        self.frame_msl_3 = QFrame(self.frame)
        self.frame_msl_3.setObjectName(u"frame_msl_3")
        self.frame_msl_3.setFrameShape(QFrame.NoFrame)
        self.frame_msl_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_msl_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(7, 7, 7, 7)
        self.lineedit_ramdisk_path = QLineEdit(self.frame_msl_3)
        self.lineedit_ramdisk_path.setObjectName(u"lineedit_ramdisk_path")

        self.gridLayout_4.addWidget(self.lineedit_ramdisk_path, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_msl_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_msl_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 2)

        self.btn_select_ramdisk = QPushButton(self.frame_msl_3)
        self.btn_select_ramdisk.setObjectName(u"btn_select_ramdisk")
        self.btn_select_ramdisk.setFlat(True)

        self.gridLayout_4.addWidget(self.btn_select_ramdisk, 1, 3, 1, 1)

        self.label_8 = QLabel(self.frame_msl_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.listwidget_rootfs_overlay = QListWidget(self.frame_msl_3)
        self.listwidget_rootfs_overlay.setObjectName(u"listwidget_rootfs_overlay")
        self.listwidget_rootfs_overlay.setFrameShape(QFrame.NoFrame)

        self.gridLayout_4.addWidget(self.listwidget_rootfs_overlay, 2, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_msl_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.textedit_bootargs = QTextEdit(self.frame_2)
        self.textedit_bootargs.setObjectName(u"textedit_bootargs")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_bootargs.sizePolicy().hasHeightForWidth())
        self.textedit_bootargs.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.textedit_bootargs)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(LinuxRunInfoWidget)

        QMetaObject.connectSlotsByName(LinuxRunInfoWidget)
    # setupUi

    def retranslateUi(self, LinuxRunInfoWidget):
        LinuxRunInfoWidget.setWindowTitle(QCoreApplication.translate("LinuxRunInfoWidget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineedit_kernel_path.setText("")
        self.label_2.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u5185\u6838", None))
        self.btn_select_kernel.setText("")
        self.label_5.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.lineedit_devicetree_path.setText("")
        self.lineedit_devicetree_path.setPlaceholderText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u4e0d\u6307\u5b9a\u5219\u81ea\u52a8\u751f\u6210", None))
        self.label_3.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u8bbe\u5907\u6811", None))
        self.btn_select_devicetree.setText("")
        self.lineedit_ramdisk_path.setText("")
        self.label_6.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"ramdisk", None))
        self.btn_select_ramdisk.setText("")
        self.label_8.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u9644\u52a0\u6587\u4ef6:", None))
        self.label.setText(QCoreApplication.translate("LinuxRunInfoWidget", u"\u542f\u52a8\u53c2\u6570\uff1a", None))
    # retranslateUi

