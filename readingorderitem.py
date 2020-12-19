# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:18:39 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_readingorderitem import Ui_ReadingOrderItem
import librosa
# from mimetypes import MimeTypes
import filetype

class ReadingOrderItem(QWidget):
    
    switch_window = pyqtSignal()
    #signal_exit = pyqtSignal()
    
    def __init__(self):
        super(ReadingOrderItem, self).__init__()

        self.ui = Ui_ReadingOrderItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        # 0/Even: Up, Odd: Down
        self.upDownCount = 0 
        self.upDownSize = self.size()
        self.ui.pushButton_UpDown.clicked.connect(self.on_pushButton_UpDown_clicked)
        
        self.ui.pushButton_Browse.clicked.connect(self.on_pushButton_Browse_clicked)
        
        # self.ui.radioButton_file.toggled.connect(lambda: self.on_radioButton_Toggled())
        # self.ui.radioButton_URL.toggled.connect(lambda: self.on_radioButton_Toggled("URL"))
        
    @pyqtSlot()
    def on_pushButton_UpDown_clicked(self):
        print("current state = {}".format(self.upDownCount % 2 == 0))
        if self.upDownCount % 2 == 0:
            self.resize(self.width(), self.ui.pushButton_UpDown.height() + 2)
            self.ui.pushButton_UpDown.setIcon(QIcon("Down-20.png"))
        else:
            self.resize(self.upDownSize)            
            self.ui.pushButton_UpDown.setIcon(QIcon("Up-20.png"))
        self.upDownCount += 1
        
    @pyqtSlot()
    def on_pushButton_Browse_clicked(self):
        print("on_pushButton_Browse_clicked")
        pass
    
            
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    item = ReadingOrderItem()
    item.show()
    
    sys.exit(app.exec_())