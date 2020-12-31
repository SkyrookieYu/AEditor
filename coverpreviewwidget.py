# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 19:37:29 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""


import filetype
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_coverpreviewwidget import Ui_CoverPreviewWidget
from multipledispatch import dispatch 
from book import Audiobook

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
        '''
        self.ui.pushButton_Add.setEnabled(True)
        self.ui.pushButton_Remove.setEnabled(False)
        '''
        self.ui.buttonGroup.buttonClicked[int].connect(self.on_button_clicked)
        # self._translate = QCoreApplication.translate    
        url = dict_Cover.get("url", "")
        if url == "":
            self.ui.pushButton_Add.setEnabled(True)
        else:
            try:
                pixmap = QPixmap(dir_Book + r"/" + url)
                self.coverFilename = dir_Book + r"/" + url
                self.ui.pushButton_Add.setEnabled(False)
            except ex:
                return
            pixmap = pixmap.scaled(self.ui.label_Cover.size(), Qt.KeepAspectRatio)
            self.ui.label_Cover.setPixmap(pixmap)
            self.ui.lineEdit.setText(dict_Cover.get("name", "Cover"))
        
        self._translate = QCoreApplication.translate
    
    
    @dispatch()
    def __init__(self):
        super(CoverPreviewWidget, self).__init__()

        self.ui = Ui_CoverPreviewWidget()
        self.ui.setupUi(self)
        
        '''
        self.ui.pushButton_Add.setEnabled(True)
        self.ui.pushButton_Remove.setEnabled(False)
        '''
        self.ui.pushButton_Add.setEnabled(True)
        
        '''
        buttons = self.ui.buttonGroup.buttons()
        for button in buttons:
            print("id = %d with text = %s" % (self.ui.buttonGroup.id(button), button.text()))
        '''
        
        self.ui.buttonGroup.buttonClicked[int].connect(self.on_button_clicked)
        self._translate = QCoreApplication.translate
    

    def on_button_clicked(self, id):
        for button in self.ui.buttonGroup.buttons():
            if button is self.ui.buttonGroup.button(id):
                #self.lineEdit.setText(button.text())
                if button.text() == 'Add':
                    print('button_Add is clicked')
                    filename, filetype = QFileDialog.getOpenFileName(self, self._translate("CoverPreviewWidget", "Select an image"), "./", self._translate("CoverPreviewWidget", "jpeg(*.jpg, *.jpeg); png(*.png)"))
                    if len(filename) > 0: 
                        print(filename)
                        self.ui.label_Cover.setPixmap(QPixmap(filename))
                        self.ui.pushButton_Add.setEnabled(False)
                        self.coverFilename = filename
                    else:
                        
                        return
                elif button.text() == 'Remove':
                    print('button_Remove is clicked')
                    self.ui.label_Cover.setPixmap(QPixmap("W3C.svg"))
                    self.ui.lineEdit.setText('')
                    self.ui.pushButton_Add.setEnabled(True)
                    self.coverFilename = ''
                pass
            
    def save(self):
        book = Audiobook.getInstance()
        kind = filetype.guess(self.coverFilename)
        dict_cover = {"url" : self.coverFilename.replace(book.getBookDir() + r"/", ''), \
                      "encodingFormat" : kind.mime, \
                      "name" : self.ui.lineEdit.text() or "Cover", \
                      "rel" : "cover" }
        return dict_cover
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    cp = CoverPreviewWidget()
    cp.show()
    sys.exit(app.exec_())