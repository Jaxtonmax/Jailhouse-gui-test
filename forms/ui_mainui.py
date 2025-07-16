# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
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
        MainWindow.resize(802, 643)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_export = QAction(MainWindow)
        self.action_export.setObjectName(u"action_export")
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab_resource = QWidget()
        self.tab_resource.setObjectName(u"tab_resource")
        self.verticalLayout_2 = QVBoxLayout(self.tab_resource)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedwidget_resource = QStackedWidget(self.tab_resource)
        self.stackedwidget_resource.setObjectName(u"stackedwidget_resource")

        self.verticalLayout_2.addWidget(self.stackedwidget_resource)

        self.tabWidget.addTab(self.tab_resource, "")
        self.tab_mem = QWidget()
        self.tab_mem.setObjectName(u"tab_mem")
        self.tabWidget.addTab(self.tab_mem, "")
        self.tab_source = QWidget()
        self.tab_source.setObjectName(u"tab_source")
        self.verticalLayout_3 = QVBoxLayout(self.tab_source)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fram_source_select = QFrame(self.tab_source)
        self.fram_source_select.setObjectName(u"fram_source_select")
        self.fram_source_select.setFrameShape(QFrame.StyledPanel)
        self.fram_source_select.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.fram_source_select)

        self.textbrowser_source = QTextBrowser(self.tab_source)
        self.textbrowser_source.setObjectName(u"textbrowser_source")

        self.verticalLayout_3.addWidget(self.textbrowser_source)

        self.tabWidget.addTab(self.tab_source, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 802, 28))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addAction(self.action_export)
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_export)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa", None))
#if QT_CONFIG(shortcut)
        self.action_new.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#if QT_CONFIG(tooltip)
        self.action_export.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_export.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_resource), QCoreApplication.translate("MainWindow", u"\u8d44\u6e90", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mem), QCoreApplication.translate("MainWindow", u"\u5185\u5b58\u89c6\u56fe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_source), QCoreApplication.translate("MainWindow", u"\u6e90\u7801", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

