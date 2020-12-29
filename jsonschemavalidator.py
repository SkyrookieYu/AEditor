# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:32:28 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from multipledispatch import dispatch

import json
import jsonschema


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    '''
    data = {
        "type" : "object",
        "properties" : {
            "price" : {"type" : "number"},
            "name" : {"type" : "string"},
        },
    }
    with open('test.schema.json', 'w', encoding="utf-8") as file_Json:
        json.dump(data, file_Json)
    '''
    
    with open('test.schema.json', 'r', encoding="utf-8") as file_Json:
        schema = json.load(file_Json)
        '''
        schema_test = {
            "type" : "object",
            "properties" : {
                "price" : {"type" : "number"},
                "name" : {"type" : "string"},
            },
        }
        '''
        
        instance_test = {"name" : "Eggs", "price" : 34.99}
        # schema = 
        ret = False
        try:
            jsonschema.validate(instance = instance_test, schema = schema)
            # print("validation is passed")
            return True
        except jsonschema.ValidationError as ve:
            #print(ve.message)
            return False
    
        #if ret:
            #print("Congratulations!")
    # sys.exit(app.exec_())