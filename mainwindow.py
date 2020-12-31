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
import json
import jsonschema
import subprocess
# subprocess.call(["python", "myscript.py"])

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
        self.ui.action_Save.triggered.connect(self._save)
        self.ui.action_Close.triggered.connect(self._close)
        self.ui.action_Validate.triggered.connect(self._validate)
        #self.ui.action_Qt.triggered.connect(self.on_action_Qt_triggered)
        #self.ui.action_PyQt5.triggered.connect(self.on_action_PyQt5_triggered)
        
        
        
        layout = QVBoxLayout(self.ui.tab_Metadata)
        self.publicationManifest = PublicationManifest(self.book.getManifestDict())
        layout.addWidget(self.publicationManifest)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        # self.ui.tab_Metadata.setLayout(self.layout)
        

        
        layout = QVBoxLayout(self.ui.dockWidgetContents)
        self.coverPreviewWidget = CoverPreviewWidget(self.book.getCoverDict(), self.book.getBookDir())
        layout.addWidget(self.coverPreviewWidget)
                       
        w = QWidget()
        layout = QHBoxLayout(w)
        #layout.addStretch(0)
        self.readingOrderWidget = ReadingOrderWidget(self.book.getReadingOrderList(), self.book.getBookDir())
        layout.addWidget(self.readingOrderWidget)
        #layout.addStretch(0)      
        self.setCentralWidget(w)
        # self.readingOrderWidget.addItems(3)
        
        #urlList = self.readingOrderWidget.resortItems()
        
        layout = QVBoxLayout(self.ui.tab_TOC)
        self.treeWidget_TOC = TreeWidget_TOC(self.book.getTOCList()) # TOCWidget()
        layout.addWidget(self.treeWidget_TOC)        
        
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
        #self.ui.action_Qt.triggered.connect(self.on_action_Qt_triggered)
        #self.ui.action_PyQt5.triggered.connect(self.on_action_PyQt5_triggered)
        
        layout = QVBoxLayout(self.ui.tab_Metadata)
        self.publicationManifest = PublicationManifest()
        layout.addWidget(self.publicationManifest)
        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        # self.ui.tab_Metadata.setLayout(self.layout)
        

        
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
        self.readingOrderWidget.addItems(1)
        
        layout = QVBoxLayout(self.ui.tab_TOC)
        self.treeWidget_TOC = TreeWidget_TOC() # TOCWidget()
        layout.addWidget(self.treeWidget_TOC)        
        
        layout = QVBoxLayout(self.ui.dockWidgetContents_2)
        self.supplementalListWidget = SupplementalListWidget()
        layout.addWidget(self.supplementalListWidget)
        self.supplementalListWidget.addItems(2)
        
    @pyqtSlot()  
    def on_action_Qt_triggered(self):
        QApplication.aboutQt()
        
    @pyqtSlot()    
    def on_action_PyQt5_triggered(self):
        QApplication.aboutPyQt5()
        
        
    def _exit(self):
        self.signal_exit.emit()
        
    def _save(self):
        # Todo
        
        manifest = self.publicationManifest.save()
        
        
        toc = self.treeWidget_TOC.save()
        
        
        
        cover = self.coverPreviewWidget.save()
        
        
        readingOrder = self.readingOrderWidget.save()
        
        
        supplementalList = self.supplementalListWidget.save()
        
        print(manifest)
        self.book.setManifestDict(manifest)
        
        print(readingOrder)
        self.book.setReadingOrderList(readingOrder)
        
        
        print(toc)
        self.book.setTOCList(toc)
        
        print(cover)
        self.book.setCoverDict(cover)
        
        print(supplementalList)
        self.book.setSupplementalList(supplementalList)
        
        self.book.on_action_Save_Audiobook_triggered()

    def refreshToc():
        tocList = []
        
        return tocList
    
    def refreshManifest():
        
        return {}
    
    def _close(self):
        '''
        toc_refreshed = refreshToc()
        manifest_refreshed = refreshManifest()
        '''
        self.book.on_action_Save_Audiobook_triggered()
        
    def _validate(self):
        ret = subprocess.call("python jsonschemavalidator.py", shell = True)
        print(ret)
        '''
        with open('audiobooks.schema.json', 'r', encoding="utf-8") as file_Json:
            schema = json.load(file_Json)

            
            instance_test = self.book.getManifestDict()    # {"name" : "Eggs", "price" : 34.99}
            # schema = 
            ret = False
            try:
                jsonschema.validate(instance = instance_test, schema = schema)
                # print("validation is passed")
                ret = True
            except jsonschema.ValidationError as ve:
                print(ve.message)
        
            if ret:
                print("Congratulations!")        
        '''
        