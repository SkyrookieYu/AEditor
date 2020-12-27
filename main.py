# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from multipledispatch import dispatch

## ==> LAUNCH PAGE
from launchpage import LaunchPage

## ==> NEW OR OPEN
from neworopen import NewOrOpen

## ==> NEW OR OPEN
from newbookwizard import NewBookWizard

## ==> MAINWINDOW
from mainwindow import MainWindow

from book import Audiobook

class Controller(QObject):
    
    signal_switch_to_mainwindow = pyqtSignal(str)
    
    def __init__(self):
        QWidget.__init__(self)
        

    def show_LaunchPage(self):
        self.launchPage = LaunchPage()
        self.launchPage.switch_window.connect(self.show_NewOrOpen)
        self.launchPage.show()

    def show_NewOrOpen(self):
        self.newOrOpen = NewOrOpen()
        self.newOrOpen.signal_switch_window[bool, str].connect(self.show_NewBookWizard)
        self.launchPage.close()
        self.newOrOpen.show()
    
    #@pyqtSlot(bool, str)
    def show_NewBookWizard(self, newOrOpen, info):
        print("newBookWizard")
        if newOrOpen == True:
            self.newBookWizard = NewBookWizard()
            self.newOrOpen.close()
            self.newBookWizard.switch_window[dict].connect(self.show_MainWindow)
            self.newBookWizard.show()
        else:
            #self.newBookWizard = NewBookWizard(item)
            self.newOrOpen.close()
            self.signal_switch_to_mainwindow[str].connect(self.show_MainWindow)
            self.signal_switch_to_mainwindow[str].emit(info)
    
    @dispatch(dict)           
    def show_MainWindow(self, dict_New):
        print("show_MainWindow for dict")
        # todo
        self.book = Audiobook.getInstance(dict_New)
        # todo
        self.mainWindow = MainWindow()
        self.mainWindow.signal_exit.connect(self.exit)
        if hasattr(self, 'newBookWizard'):
            self.newBookWizard.close()
        self.mainWindow.show()    

    @dispatch(str)
    def show_MainWindow(self, item):
        print("show_MainWindow for str")
        # todo
        self.book = Audiobook.getInstance(item)
        self.mainWindow = MainWindow(self.book)
        self.mainWindow.signal_exit.connect(self.exit)
        if hasattr(self, 'newBookWizard'):
            self.newBookWizard.close()
        self.mainWindow.show()
     
    '''
    def show_Groups(self):
        self.groups = Groups()
        # self.groups.signal_exit.connect(self.exit)
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
        self.groups.show()
    '''    
        
    def exit(self):
        print("exit")
        self.mainWindow.close()
        
        del self.mainWindow
        del self.book
        
        QCoreApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # launchPage = LaunchPage()
    # launchPage.show()
    # newOrOpen = NewOrOpen()
    # newOrOpen.show()
    # newBookWizard = NewBookWizard()
    # newBookWizard.show()
    # mainWindow = MainWindow()
    # mainWindow.show()
    
    # groups = Groups()
    # groups.show()
    
    # form = Form()
    # form.show()
    
    controller = Controller()
    controller.show_LaunchPage()    
    
    sys.exit(app.exec_())
