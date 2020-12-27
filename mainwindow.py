# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:19:51 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""


from bs4 import BeautifulSoup
import filetype
import glob
import json
# import librosa
from mutagen.mp3 import MP3
# from mimetypes import MimeTypes
import os
import re
import sys
import tempfile
import time
import urllib.request
import zipfile
from multipledispatch import dispatch

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui_mainwindow import Ui_MainWindow
from publicationmanifest import PublicationManifest
from readingorderwidget import ReadingOrderWidget
from supplementalitem import SupplementalListWidget
from tocitem import TOCWidget
from treewidget_toc import TreeWidget_TOC
from coverpreviewwidget import CoverPreviewWidget
from book import Audiobook

class MainWindow(QMainWindow):
    
    switch_window = pyqtSignal()
    signal_exit = pyqtSignal()
    
    @dispatch(Audiobook)
    def __init__(self, book):
        super(MainWindow, self).__init__()

        self.book = book
        
        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.action_Exit.triggered.connect(self._exit)
        
        layout = QVBoxLayout(self.ui.tab_Metadata)
        self.publicationManifest = PublicationManifest(self.book.getManifestDict())
        layout.addWidget(self.publicationManifest)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        # self.ui.tab_Metadata.setLayout(self.layout)
        
        layout = QVBoxLayout(self.ui.tab_TOC)
        self.treeWidget_TOC = TreeWidget_TOC(self.book.getTOCList()) # TOCWidget()
        layout.addWidget(self.treeWidget_TOC)
        
        layout = QVBoxLayout(self.ui.dockWidgetContents)
        self.coverPreviewWidget = CoverPreviewWidget(self.book.getCoverDict(), self.book.getBookDir())
        layout.addWidget(self.coverPreviewWidget)
                       
        w = QWidget()
        layout = QHBoxLayout(w)
        #layout.addStretch(0)
        self.readingOrderWidget = ReadingOrderWidget(self.book.getReadingOrderList())
        layout.addWidget(self.readingOrderWidget)
        #layout.addStretch(0)      
        self.setCentralWidget(w)
        # self.readingOrderWidget.addItems(3)
        
        
        layout = QVBoxLayout(self.ui.dockWidgetContents_2)
        self.supplementalListWidget = SupplementalListWidget(self.book.getSupplementalList())
        layout.addWidget(self.supplementalListWidget)
        # self.supplementalListWidget.addItems(2)    
    
    
    
    @dispatch()
    def __init__(self):
        super(MainWindow, self).__init__()

        # QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

        self.ui.action_Exit.triggered.connect(self._exit)
        
        layout = QVBoxLayout(self.ui.tab_Metadata)
        self.publicationManifest = PublicationManifest()
        layout.addWidget(self.publicationManifest)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        # self.ui.tab_Metadata.setLayout(self.layout)
        
        layout = QVBoxLayout(self.ui.tab_TOC)
        self.treeWidget_TOC = TreeWidget_TOC() # TOCWidget()
        layout.addWidget(self.treeWidget_TOC)
        
        layout = QVBoxLayout(self.ui.dockWidgetContents)
        self.coverPreviewWidget = CoverPreviewWidget()
        layout.addWidget(self.coverPreviewWidget)
                       
        w = QWidget()
        layout = QHBoxLayout(w)
        #layout.addStretch(0)
        self.readingOrderWidget = ReadingOrderWidget()
        layout.addWidget(self.readingOrderWidget)
        #layout.addStretch(0)      
        self.setCentralWidget(w)
        self.readingOrderWidget.addItems(3)
        
        
        layout = QVBoxLayout(self.ui.dockWidgetContents_2)
        self.supplementalListWidget = SupplementalListWidget()
        layout.addWidget(self.supplementalListWidget)
        self.supplementalListWidget.addItems(2)
        
        
    def _exit(self):
        self.signal_exit.emit()
