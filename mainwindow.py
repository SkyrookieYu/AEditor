# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
from publicationmanifest import PublicationManifest


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
        
        self.layout = QVBoxLayout()
        self.publicationManifest = PublicationManifest()
        self.layout.addWidget(self.publicationManifest)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.ui.tab_Metadata.setLayout(self.layout)
        '''
        layout = QVBoxLayout()
        self.groups = Groups()
        layout.addWidget(self.groups)
        '''

        
        
        
    def _exit(self):
        self.signal_exit.emit()