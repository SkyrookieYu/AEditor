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
from multipledispatch import dispatch 

class CoverPreviewWidget(QWidget):
    
    switch_window = pyqtSignal()
    #signal_exit = pyqtSignal()
    
    @dispatch(dict, str)
    def __init__(self, dict_Cover, dir_Book):
        super(CoverPreviewWidget, self).__init__()

        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        
        '''
        buttons = self.ui.buttonGroup.buttons()
        for button in buttons:
            print("id = %d with text = %s" % (self.ui.buttonGroup.id(button), button.text()))
        '''
        
        self.ui.buttonGroup.buttonClicked[int].connect(self.on_button_clicked)
        # self._translate = QCoreApplication.translate    
        url = dict_Cover.get("url", "")
        if url == "":
            pass
        else:
            pixmap = QPixmap(dir_Book + r"/" + url)
            pixmap = pixmap.scaled(self.ui.label_Cover.size(), Qt.KeepAspectRatio)
            self.ui.label_Cover.setPixmap(pixmap)
            self.ui.lineEdit.setText(dict_Cover.get("name", "Cover"))
        
    
    
    
    @dispatch()
    def __init__(self):
        super(CoverPreviewWidget, self).__init__()

        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        
        '''
        buttons = self.ui.buttonGroup.buttons()
        for button in buttons:
            print("id = %d with text = %s" % (self.ui.buttonGroup.id(button), button.text()))
        '''
        
        self.ui.buttonGroup.buttonClicked[int].connect(self.on_button_clicked)
        # self._translate = QCoreApplication.translate
    

    def on_button_clicked(self, id):
        for button in self.ui.buttonGroup.buttons():
            if button is self.ui.buttonGroup.button(id):
                #self.lineEdit.setText(button.text())
                if button.text() == 'Add':
                    print('button_Add is clicked')
                    
                elif button.text() == 'Remove':
                    print('button_Remove is clicked')
                    
                pass
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = CoverPreviewWidget()
    cp.show()
    sys.exit(app.exec_())