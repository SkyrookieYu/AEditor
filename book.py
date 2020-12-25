# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 03:40:52 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import librosa
# from mimetypes import MimeTypes
import filetype

"""
class Book: PEP + Publication Manifest + TOC
"""


class Book:
    # Singleton Pattern
    _instance = None
    
    @staticmethod
    def getInstance():
        if Book._instance is None:
            Book()
        return Book._instance
    
    # Private Constructor
    def __init__(self):
        if Book._instance is not None:
            raise Exception('Only one instace of Book should exist!')
        else:       
            self._id = id(self)
            
            
            
            
            Book._instance = self
    
    def getID(self):
        return self._id
    
if __name__ == '__main__':
    #app = QApplication(sys.argv)
    b = Book.getInstance()
    print(b)
    print(b.getID())
    #sys.exit(app.exec_())