# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ivshmem_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_IVShMemWidget(object):
    def setupUi(self, IVShMemWidget):
        if not IVShMemWidget.objectName():
            IVShMemWidget.setObjectName(u"IVShMemWidget")
        IVShMemWidget.resize(1222, 1099)
        self.verticalLayout_5 = QVBoxLayout(IVShMemWidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollarea = QScrollArea(IVShMemWidget)
        self.scrollarea.setObjectName(u"scrollarea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollarea.sizePolicy().hasHeightForWidth())
        self.scrollarea.setSizePolicy(sizePolicy)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea_content = QWidget()
        self.scrollarea_content.setObjectName(u"scrollarea_content")
        self.scrollarea_content.setGeometry(QRect(0, 0, 1220, 1097))
        self.verticalLayout_2 = QVBoxLayout(self.scrollarea_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.scrollarea_content)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        sizePolicy.setHeightForWidth(self.frame_left.sizePolicy().hasHeightForWidth())
        self.frame_left.setSizePolicy(sizePolicy)
        self.frame_left.setFrameShape(QFrame.NoFrame)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_ivsm = QFrame(self.frame_left)
        self.frame_ivsm.setObjectName(u"frame_ivsm")
        self.frame_ivsm.setFrameShape(QFrame.NoFrame)
        self.frame_ivsm.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_ivsm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_ivsm_title = QFrame(self.frame_ivsm)
        self.frame_ivsm_title.setObjectName(u"frame_ivsm_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_ivsm_title.sizePolicy().hasHeightForWidth())
        self.frame_ivsm_title.setSizePolicy(sizePolicy1)
        self.frame_ivsm_title.setFrameShape(QFrame.NoFrame)
        self.frame_ivsm_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_ivsm_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_ivsm = QLabel(self.frame_ivsm_title)
        self.label_ivsm.setObjectName(u"label_ivsm")
        sizePolicy1.setHeightForWidth(self.label_ivsm.sizePolicy().hasHeightForWidth())
        self.label_ivsm.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_ivsm)


        self.verticalLayout.addWidget(self.frame_ivsm_title)

        self.frame_ivsm_content = QFrame(self.frame_ivsm)
        self.frame_ivsm_content.setObjectName(u"frame_ivsm_content")
        self.frame_ivsm_content.setFrameShape(QFrame.NoFrame)
        self.frame_ivsm_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_ivsm_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_ivsm_values = QFrame(self.frame_ivsm_content)
        self.frame_ivsm_values.setObjectName(u"frame_ivsm_values")
        self.frame_ivsm_values.setFrameShape(QFrame.NoFrame)
        self.frame_ivsm_values.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_ivsm_values)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_ivsm_values)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_ivsm_values)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_ivsm_values)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame_ivsm_values)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.lineedit_ivshmem_phy = QLineEdit(self.frame_ivsm_values)
        self.lineedit_ivshmem_phy.setObjectName(u"lineedit_ivshmem_phy")

        self.gridLayout.addWidget(self.lineedit_ivshmem_phy, 0, 1, 1, 1)

        self.lineedit_ivshmem_state_size = QLineEdit(self.frame_ivsm_values)
        self.lineedit_ivshmem_state_size.setObjectName(u"lineedit_ivshmem_state_size")

        self.gridLayout.addWidget(self.lineedit_ivshmem_state_size, 1, 1, 1, 1)

        self.lineedit_ivshmem_rw_size = QLineEdit(self.frame_ivsm_values)
        self.lineedit_ivshmem_rw_size.setObjectName(u"lineedit_ivshmem_rw_size")

        self.gridLayout.addWidget(self.lineedit_ivshmem_rw_size, 2, 1, 1, 1)

        self.lineedit_ivshmem_out_size = QLineEdit(self.frame_ivsm_values)
        self.lineedit_ivshmem_out_size.setObjectName(u"lineedit_ivshmem_out_size")

        self.gridLayout.addWidget(self.lineedit_ivshmem_out_size, 3, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_ivsm_values)


        self.verticalLayout.addWidget(self.frame_ivsm_content)


        self.verticalLayout_3.addWidget(self.frame_ivsm)


        self.horizontalLayout.addWidget(self.frame_left)

        self.frame_right = QFrame(self.frame_main)
        self.frame_right.setObjectName(u"frame_right")
        sizePolicy.setHeightForWidth(self.frame_right.sizePolicy().hasHeightForWidth())
        self.frame_right.setSizePolicy(sizePolicy)
        self.frame_right.setFrameShape(QFrame.NoFrame)
        self.frame_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_right)


        self.verticalLayout_2.addWidget(self.frame_main)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.scrollarea.setWidget(self.scrollarea_content)

        self.verticalLayout_5.addWidget(self.scrollarea)


        self.retranslateUi(IVShMemWidget)

        QMetaObject.connectSlotsByName(IVShMemWidget)
    # setupUi

    def retranslateUi(self, IVShMemWidget):
        IVShMemWidget.setWindowTitle(QCoreApplication.translate("IVShMemWidget", u"Form", None))
        self.label_ivsm.setText(QCoreApplication.translate("IVShMemWidget", u"\u6838\u95f4\u901a\u4fe1", None))
        self.label.setText(QCoreApplication.translate("IVShMemWidget", u"\u8d77\u59cb\u7269\u7406\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("IVShMemWidget", u"State section \u5927\u5c0f", None))
        self.label_4.setText(QCoreApplication.translate("IVShMemWidget", u"Output section \u5927\u5c0f", None))
        self.label_3.setText(QCoreApplication.translate("IVShMemWidget", u"Read/Write section \u5927\u5c0f", None))
    # retranslateUi

