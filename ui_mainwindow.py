# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1335, 1282)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("hyread-logo-pc@3x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1335, 18))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget_Left = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_Left.sizePolicy().hasHeightForWidth())
        self.dockWidget_Left.setSizePolicy(sizePolicy)
        self.dockWidget_Left.setMinimumSize(QtCore.QSize(240, 640))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.dockWidget_Left.setFont(font)
        self.dockWidget_Left.setAutoFillBackground(False)
        self.dockWidget_Left.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 6px solid red;\n"
"}")
        self.dockWidget_Left.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_Left.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_Left.setObjectName("dockWidget_Left")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Metadata = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_Metadata.sizePolicy().hasHeightForWidth())
        self.tab_Metadata.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.tab_Metadata.setFont(font)
        self.tab_Metadata.setObjectName("tab_Metadata")
        self.tabWidget.addTab(self.tab_Metadata, "")
        self.tab_TOC = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_TOC.sizePolicy().hasHeightForWidth())
        self.tab_TOC.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.tab_TOC.setFont(font)
        self.tab_TOC.setObjectName("tab_TOC")
        self.tabWidget.addTab(self.tab_TOC, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.dockWidget_Left.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_Left)
        self.dockWidget_CoverPreviewWidget = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_CoverPreviewWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget_CoverPreviewWidget.setSizePolicy(sizePolicy)
        self.dockWidget_CoverPreviewWidget.setMinimumSize(QtCore.QSize(300, 402))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.dockWidget_CoverPreviewWidget.setFont(font)
        self.dockWidget_CoverPreviewWidget.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 5px solid red;\n"
"}")
        self.dockWidget_CoverPreviewWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_CoverPreviewWidget.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_CoverPreviewWidget.setObjectName("dockWidget_CoverPreviewWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setMinimumSize(QtCore.QSize(300, 380))
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget_CoverPreviewWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_CoverPreviewWidget)
        self.dockWidget_SupplementalList = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_SupplementalList.sizePolicy().hasHeightForWidth())
        self.dockWidget_SupplementalList.setSizePolicy(sizePolicy)
        self.dockWidget_SupplementalList.setMinimumSize(QtCore.QSize(300, 422))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.dockWidget_SupplementalList.setFont(font)
        self.dockWidget_SupplementalList.setStyleSheet("QDockWidget > QWidget {\n"
"    border: 5px solid red;\n"
"}")
        self.dockWidget_SupplementalList.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget_SupplementalList.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_SupplementalList.setObjectName("dockWidget_SupplementalList")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setMinimumSize(QtCore.QSize(300, 400))
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.dockWidget_SupplementalList.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_SupplementalList)
        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Qt = QtWidgets.QAction(MainWindow)
        self.action_Qt.setObjectName("action_Qt")
        self.action_PyQt5 = QtWidgets.QAction(MainWindow)
        self.action_PyQt5.setObjectName("action_PyQt5")
        self.action_Preview = QtWidgets.QAction(MainWindow)
        self.action_Preview.setObjectName("action_Preview")
        self.action_Validate = QtWidgets.QAction(MainWindow)
        self.action_Validate.setObjectName("action_Validate")
        self.action_Pack = QtWidgets.QAction(MainWindow)
        self.action_Pack.setObjectName("action_Pack")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addAction(self.action_Exit)
        self.menuAbout.addAction(self.action_Qt)
        self.menuAbout.addAction(self.action_PyQt5)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.action_New)
        self.toolBar.addAction(self.action_Preview)
        self.toolBar.addAction(self.action_Validate)
        self.toolBar.addAction(self.action_Pack)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Metadata), _translate("MainWindow", "Metadata"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_TOC), _translate("MainWindow", "TOC"))
        self.dockWidget_CoverPreviewWidget.setWindowTitle(_translate("MainWindow", "Cover Preview Widget"))
        self.dockWidget_SupplementalList.setWindowTitle(_translate("MainWindow", "Supplemental List"))
        self.action_New.setText(_translate("MainWindow", "&New"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))
        self.action_Qt.setText(_translate("MainWindow", "&Qt"))
        self.action_PyQt5.setText(_translate("MainWindow", "&PyQt5"))
        self.action_Preview.setText(_translate("MainWindow", "&Preview"))
        self.action_Validate.setText(_translate("MainWindow", "&Validate"))
        self.action_Pack.setText(_translate("MainWindow", "&Pack"))
        self.action_Pack.setToolTip(_translate("MainWindow", "Pack"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
