# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 01:38:48 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from multipledispatch import dispatch

from ui_publicationmanifest import Ui_PublicationManifest


class PublicationManifest(QWidget):
    
    switch_window = pyqtSignal()
    #signal_exit = pyqtSignal()
    
    @dispatch()
    def __init__(self):
        super(PublicationManifest, self).__init__()

        self.ui = Ui_PublicationManifest()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate

    @dispatch(dict)
    def __init__(self, manifestDict):
        super(PublicationManifest, self).__init__()

        self.ui = Ui_PublicationManifest()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        # Required 
        self.ui.lineEdit_name.setText(manifestDict.get("name", ""))
        self.ui.lineEdit_conformsTo.setText(manifestDict.get("conformsTo", ""))
        self.ui.lineEdit_context.setText(str(manifestDict.get("@context", [])))
        
        self.ui.comboBox_abridged.setCurrentText(str(manifestDict.get("abridged", True)))
        self.ui.lineEdit_accessibilityFeature.setText(str(manifestDict.get("accessibilityFeature", [])))
        self.ui.lineEdit_accessibilityHazard.setText(manifestDict.get("accessibilityHazard", ""))
        self.ui.lineEdit_accessibilitySummary.setText(manifestDict.get("accessibilitySummary", ""))
        
        self.ui.comboBox_accessMode.setCurrentData(manifestDict.get("accessMode", []))
        self.ui.lineEdit_accessModeSufficient.setText(str(manifestDict.get("accessModeSufficient", [])))
        self.ui.lineEdit_author.setText(manifestDict.get("author", ""))
        self.ui.lineEdit_cover.setText(manifestDict.get("cover", ""))
        self.ui.lineEdit_duration.setText(manifestDict.get("duration", ""))
        self.ui.dateTimeEdit_dateModified.setDateTime(QDateTime.fromString(manifestDict.get("dateModified", "")))
        self.ui.dateTimeEdit_datePublished.setDateTime(QDateTime.fromString(manifestDict.get("datePublished", "")))
        self.ui.lineEdit_id.setText(manifestDict.get("id", ""))
        #manifestDict.get("inLanguage", ""))
        self.ui.lineEdit_readBy.setText(manifestDict.get("readBy", ""))
        self.ui.lineEdit_readingProgression.setText(manifestDict.get("readingProgression", ""))
        self.ui.lineEdit_type.setText(manifestDict.get("type", "CreativeWork"))
        self.ui.lineEdit_url.setText(manifestDict.get("url", ""))
        
        
        
        
        
        
        
        
        