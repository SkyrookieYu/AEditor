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
        self.ui.dateEdit_datePublished.setDate(QDate.fromString(manifestDict.get("datePublished", "2000-1-1")))
        self.ui.lineEdit_id.setText(manifestDict.get("id", ""))
        #manifestDict.get("inLanguage", ""))
        self.ui.lineEdit_readBy.setText(manifestDict.get("readBy", ""))
        self.ui.lineEdit_readingProgression.setText(manifestDict.get("readingProgression", ""))
        self.ui.lineEdit_type.setText(manifestDict.get("type", "CreativeWork"))
        self.ui.lineEdit_url.setText(manifestDict.get("url", ""))
        
    def save(self):
        dict_pm = {}
        
        # Required 
        dict_pm["name"] = self.ui.lineEdit_name.text()
        dict_pm["conformsTo"] ="https://www.w3.org/TR/audiobooks/" 
        dict_pm["@context"] = ["https://schema.org", "https://www.w3.org/ns/pub-context"] 
        
        # Optional
        
        dict_pm["abridged"] = self.ui.comboBox_abridged.currentText()
        
        dict_pm["accessibilityFeature"] = self.ui.lineEdit_accessibilityFeature.text() 
        dict_pm["accessibilityHazard"] = self.ui.lineEdit_accessibilityHazard.text()
        dict_pm["accessibilitySummary"] = self.ui.lineEdit_accessibilitySummary.text()
        dict_pm["accessModeSufficient"] = self.ui.lineEdit_accessModeSufficient.text()
        dict_pm["accessMode"] = self.ui.comboBox_accessMode.currentText()
        
        dict_pm["author"] = self.ui.lineEdit_author.text()
        dict_pm["cover"] = self.ui.lineEdit_cover.text()
        dict_pm["duration"] = self.ui.lineEdit_duration.text()
        dict_pm["dateModified"] = self.ui.dateTimeEdit_dateModified.dateTime().toString()
        dict_pm["datePublished"] = self.ui.dateEdit_datePublished.date().toString()
        dict_pm["id"] = self.ui.lineEdit_id.text()
        dict_pm["inLanguage"] = self.ui.comboBox_inLanguage.currentText()
        dict_pm["readBy"] = self.ui.lineEdit_readBy.text()
        dict_pm["readingProgression"] = self.ui.lineEdit_readingProgression.text()
        dict_pm["type"] =  'Audiobook'
        dict_pm["url"] = self.ui.lineEdit_url.text()        
        
        return dict_pm
        
        
        
        
        
        
        
        
        