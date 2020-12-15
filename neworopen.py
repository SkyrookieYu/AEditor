# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_neworopen import Ui_NewOrOpen

class NewOrOpen(QMainWindow):
    
    switch_window = pyqtSignal()
    
    MaxRecentFiles = 10
    # windowList = []

    def __init__(self):
        super(NewOrOpen, self).__init__()

        # QMainWindow.__init__(self)
        self.ui = Ui_NewOrOpen()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        # self.recentFile = []
        
        self.settings = QSettings("Audiobooks Editor", "NewOrOpen")
        self.recentFilesInSettings = self.settings.value('RecentlyOpenedFiles', [])
        print(self.recentFilesInSettings)
        #if self.recentFilesInSettings is not None:
        slm = QStringListModel()                 
        slm.setStringList(self.recentFilesInSettings)
        self.ui.listView.setModel(slm)
        self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)    
        self.ui.listView.doubleClicked.connect(self.doubleClicked)
        
        ''' DRAG AND DROP
        self.ui.listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.listView.setDragEnabled(True)
        self.ui.listView.setAcceptDrops(True)
        self.ui.listView.setDropIndicatorShown(True)
        '''
        
        self.ui.button_New.clicked.connect(self.new)
        self.ui.button_Open.clicked.connect(self.open)
        
        

    def new(self):
        # QMessageBox.information(self, self._translate("NewOrOpen", "Hint!"), self._translate("NewOrOpen", "New !"), QMessageBox.Ok)
        saveDirectory = QFileDialog.getExistingDirectory(self, self._translate("NewOrOpen", "Select one directory"), self._translate("NewOrOpen", "./"))
        print(saveDirectory)
        self.switch_window.emit()

    def open(self):
        # QMessageBox.information(self, self._translate("NewOrOpen", "Hint!"), self._translate("NewOrOpen", "Open !"), QMessageBox.Ok)      
        filename, filetype = QFileDialog.getOpenFileName(self, self._translate("NewOrOpen", "Select a book"), "./", self._translate("NewOrOpen", "Audiobooks(*.lpf)"))
        if len(filename) > 0: 
            print(filename)
        else:
            return
        if filename in self.recentFilesInSettings and self.recentFilesInSettings.index(filename) == 0:
            return
        self.updateSettings(filename)
           
    def doubleClicked(self, qModelIndex):
        print(self.recentFilesInSettings[qModelIndex.row()])
        if qModelIndex.row() == 0:
            return
        filename = self.recentFilesInSettings[qModelIndex.row()]
        self.updateSettings(filename)
     
    def updateSettings(self, filename):
        # filename = self.recentFilesInSettings[qModelIndex.row()]
        slm = QStringListModel()
        slm.setStringList([])
        self.ui.listView.setModel(slm)
        
        try:
            self.recentFilesInSettings.remove(filename)
        except ValueError:
            pass

        self.recentFilesInSettings.insert(0, filename)
        del self.recentFilesInSettings[NewOrOpen.MaxRecentFiles:]
        
        slm = QStringListModel()
        slm.setStringList(self.recentFilesInSettings)
        self.ui.listView.setModel(slm)

        self.settings.setValue('RecentlyOpenedFiles', self.recentFilesInSettings)
        
    def clearSettings(self):    
        self.settings.setValue('RecentlyOpenedFiles', [])
'''
    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()
'''
