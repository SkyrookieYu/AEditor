# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_newbookwizard import Ui_NewBookWizard

class NewBookWizard(QMainWindow):
    
    switch_window = pyqtSignal(dict)
    
    def __init__(self):
        super(NewBookWizard, self).__init__()

        QMainWindow.__init__(self)
        self.ui = Ui_NewBookWizard()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        self.ui.button_Browse.clicked.connect(self._button_Browse_clicked)
        self.ui.button_Create.clicked.connect(self._button_Create_clicked)
        self.ui.button_Cancel.clicked.connect(self._button_Cancel_clicked)
        
        
    def _button_Browse_clicked(self):
        saveDirectory = QFileDialog.getExistingDirectory(self, self._translate("NewBookWizard", "Select one directory"), "./")
        print(saveDirectory)
        if len(saveDirectory) > 0:
            self.ui.le_FilePath.setText(saveDirectory)
            self.ui.le_FilePath.setReadOnly(True)
            
    def _button_Create_clicked(self):
        saveDir = self.ui.le_FilePath.text()
        bookTitle = self.ui.lineEdit_BookTitle.text()
        author = self.ui.lineEdit_Author.text()
        publisher = self.ui.lineEdit_Publisher.text()
        readBy = self.ui.lineEdit_ReadBy.text()
        if len(saveDir) and len(bookTitle):
            print(saveDir + ":" + bookTitle)
            print(self.ui.cb_Embedded.isChecked())
            self.switch_window.emit({"saveDir": saveDir, "bookTitle": bookTitle, "author": author, "publisher": publisher, "readBy": readBy})
        else:
            QMessageBox.warning(self, self._translate("NewBookWizard", "Warning!"), self._translate("NewBookWizard", "You must select one directory and keyin the booktitle!"))
            
    def _button_Cancel_clicked(self):
        self.close()
        