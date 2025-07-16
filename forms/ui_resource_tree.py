# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resource_tree.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ResourceTree(object):
    def setupUi(self, ResourceTree):
        if not ResourceTree.objectName():
            ResourceTree.setObjectName(u"ResourceTree")
        ResourceTree.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ResourceTree)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeview = QTreeView(ResourceTree)
        self.treeview.setObjectName(u"treeview")

        self.verticalLayout.addWidget(self.treeview)


        self.retranslateUi(ResourceTree)

        QMetaObject.connectSlotsByName(ResourceTree)
    # setupUi

    def retranslateUi(self, ResourceTree):
        ResourceTree.setWindowTitle(QCoreApplication.translate("ResourceTree", u"Form", None))
    # retranslateUi

