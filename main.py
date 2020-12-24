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

## ==> LAUNCH PAGE
from launchpage import LaunchPage

## ==> NEW OR OPEN
from neworopen import NewOrOpen

## ==> NEW OR OPEN
from newbookwizard import NewBookWizard

## ==> MAINWINDOW
from mainwindow import MainWindow

class Controller:
    
    def __init__(self):
        pass

    def show_LaunchPage(self):
        self.launchPage = LaunchPage()
        self.launchPage.switch_window.connect(self.show_NewOrOpen)
        self.launchPage.show()

    def show_NewOrOpen(self):
        self.newOrOpen = NewOrOpen()
        self.newOrOpen.switch_window.connect(self.show_NewBookWizard)
        self.launchPage.close()
        self.newOrOpen.show()

    def show_NewBookWizard(self):
        self.newBookWizard = NewBookWizard()
        self.newBookWizard.switch_window.connect(self.show_MainWindow)
        self.newOrOpen.close()
        self.newBookWizard.show()
        
    def show_MainWindow(self):
        self.mainWindow = MainWindow()
        self.mainWindow.signal_exit.connect(self.exit)
        if hasattr(self, 'newBookWizard'):
            self.newBookWizard.close()
        self.mainWindow.show()
        
    def show_Groups(self):
        self.groups = Groups()
        # self.groups.signal_exit.connect(self.exit)
        if hasattr(self, 'mainWindow'):
            self.mainWindow.close()
        self.groups.show()
        
        
    def exit(self):
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
    controller.show_MainWindow()    
    
    sys.exit(app.exec_())
