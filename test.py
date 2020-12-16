# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from ui_test import Ui_Form


class Form(QWidget):
    
    switch_window = pyqtSignal()
    signal_exit = pyqtSignal()
    
    def __init__(self):
        super(Form, self).__init__()

        # QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        