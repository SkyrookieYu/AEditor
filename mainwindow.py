# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow
from leftdockwidget import LeftDockWidget
from groups import Groups

from test import Form

class MainWindow(QMainWindow):
    
    switch_window = pyqtSignal()
    signal_exit = pyqtSignal()
    
    def __init__(self):
        super(MainWindow, self).__init__()

        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.action_Exit.triggered.connect(self._exit)
        
        layout = QVBoxLayout()
        self.form = Form()
        layout.addWidget(self.form)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.ui.tab_Metadata.setLayout(layout)
        '''
        layout = QVBoxLayout()
        self.groups = Groups()
        layout.addWidget(self.groups)
        '''
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.ui.tab_Metadata.setLayout(layout)  
        
        
        
    def _exit(self):
        self.signal_exit.emit()
