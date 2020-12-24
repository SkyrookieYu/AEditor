# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:37:29 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_coverpreviewwidget import Ui_CoverPreviewWidget


class CoverPreviewWidget(QWidget):
    
    switch_window = pyqtSignal()
    #signal_exit = pyqtSignal()
    
    def __init__(self):
        super(CoverPreviewWidget, self).__init__()

        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = CoverPreviewWidget()
    cp.show()
    sys.exit(app.exec_())