# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:38:48 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_publicationmanifest import Ui_PublicationManifest


class PublicationManifest(QWidget):
    
    switch_window = pyqtSignal()
    #signal_exit = pyqtSignal()
    
    def __init__(self):
        super(PublicationManifest, self).__init__()

        self.ui = Ui_PublicationManifest()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
