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
    
    signal_switch_window = pyqtSignal(bool, str)  
    
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
        self.recentFilesOrDirectoriesInSettings = self.settings.value('RecentlyOpenedFilesOrDirectories', [])
        print(self.recentFilesOrDirectoriesInSettings)
        #if self.recentFilesInSettings is not None:
        slm = QStringListModel()                 
        slm.setStringList(self.recentFilesOrDirectoriesInSettings)
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
        self.updateSettings(True, saveDirectory)
        

    def open(self):
        # QMessageBox.information(self, self._translate("NewOrOpen", "Hint!"), self._translate("NewOrOpen", "Open !"), QMessageBox.Ok)      
        reply = QMessageBox.question(self, 'Question', 'Do you wanna open an Audiobook directory? Default is "Yes"!', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            #self.la.setText('你选择了Yes！')
            openDirectory = QFileDialog.getExistingDirectory(self, self._translate("NewOrOpen", "Select one directory"), self._translate("NewOrOpen", "./"))
            print(openDirectory)
            '''
            if openDirectory in self.recentFilesOrDirectoriesInSettings and self.recentFilesOrDirectoriesInSettings.index(openDirectory) == 0:
                return
            '''
            self.updateSettings(False, openDirectory)
            
            
        elif reply == QMessageBox.No:
            #self.la.setText('你选择了No！')
        
            filename, filetype = QFileDialog.getOpenFileName(self, self._translate("NewOrOpen", "Select a book"), "./", self._translate("NewOrOpen", "Audiobooks(*.lpf)"))
            if len(filename) > 0: 
                print(filename)
            else:
                return
            '''
            if filename in self.recentlyOpenedFilesOrDirectories and self.recentlyOpenedFilesOrDirectories.index(filename) == 0:
                return
            '''
            self.updateSettings(False, filename)
           
    def doubleClicked(self, qModelIndex):
        print(self.recentFilesOrDirectoriesInSettings[qModelIndex.row()])
        item = self.recentFilesOrDirectoriesInSettings[qModelIndex.row()]
        '''
        if qModelIndex.row() == 0:
            return
        '''
        self.updateSettings(False, item)
        
        
     
    def updateSettings(self, newOrOpen, item):
        # filename = self.recentFilesInSettings[qModelIndex.row()]
        slm = QStringListModel()
        slm.setStringList([])
        self.ui.listView.setModel(slm)
        
        try:
            self.recentFilesOrDirectoriesInSettings.remove(item)
        except ValueError:
            pass

        self.recentFilesOrDirectoriesInSettings.insert(0, item)
        del self.recentFilesOrDirectoriesInSettings[NewOrOpen.MaxRecentFiles:]
        
        slm = QStringListModel()
        slm.setStringList(self.recentFilesOrDirectoriesInSettings)
        self.ui.listView.setModel(slm)

        self.settings.setValue('RecentlyOpenedFilesOrDirectories', self.recentFilesOrDirectoriesInSettings)
        print(newOrOpen)
        print(item)
        self.signal_switch_window[bool, str].emit(newOrOpen, item)
        
    def clearSettings(self):    
        self.settings.setValue('RecentlyOpenedFilesOrDirectories', [])
'''
    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()
'''
