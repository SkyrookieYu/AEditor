# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""


import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

## ==> LAUNCH PAGE
from ui_launchpage import Ui_LaunchPage

## ==> NEW OR OPEN
from neworopen import NewOrOpen

## ==> NEW OR OPEN
from newbookwizard import NewBookWizard

## ==> GLOBALS
counter = 0


# LAUNCH PAGE
class LaunchPage(QMainWindow):
    switch_window = pyqtSignal()
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LaunchPage()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        # self.ui.label_Description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label_Description.setText("<strong>LOADING</strong> DATABASE"))
        # QtCore.QTimer.singleShot(3000, lambda: self.ui.label_Description.setText("<strong>LOADING</strong> USER INTERFACE"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = MainWindow()
            # self.main.show()

            self.switch_window.emit()
            # CLOSE LAUNCH PAGE
            self.close()

        # INCREASE COUNTER
        counter += 1


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
        self.newOrOpen.close()
        self.newBookWizard.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # launchPage = LaunchPage()
    # launchPage.show()
    # newOrOpen = NewOrOpen()
    # newOrOpen.show()
    # newBookWizard = NewBookWizard()
    # newBookWizard.show()
    controller = Controller()
    controller.show_LaunchPage()    
    sys.exit(app.exec_())
