# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:18:39 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_readingorderitem import Ui_ReadingOrderItem
import librosa
# from mimetypes import MimeTypes
import filetype

class ReadingOrderItem(QWidget):
    
    # switch_window = pyqtSignal()
    signal_resize_item = pyqtSignal(int, int, int)
    
    def __init__(self, serialNo=-1):
        super(ReadingOrderItem, self).__init__()

        self.ui = Ui_ReadingOrderItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        self.__serialNo = serialNo
        # 0/Even: Up, Odd: Down
        self.upDownCount = 0 
        self.upDownSize = self.size()
        
        
        
        # Use pyqtSlot to automatically connect to slots
        # self.ui.pushButton_UpDown.clicked.connect(self.on_pushButton_UpDown_clicked)
        # self.ui.pushButton_Browse.clicked.connect(self.on_pushButton_Browse_clicked)
        
        # self.ui.radioButton_file.toggled.connect(lambda: self.on_radioButton_Toggled())
        # self.ui.radioButton_URL.toggled.connect(lambda: self.on_radioButton_Toggled("URL"))
        
    def serialNo(self):
        return self.__serialNo
    
    @pyqtSlot()
    def on_pushButton_UpDown_clicked(self):
        print("current state = {}".format(self.upDownCount % 2 == 0))
        if self.upDownCount % 2 == 0:
            self.resize(self.width(), self.ui.pushButton_UpDown.height() + 2)
            self.ui.pushButton_UpDown.setIcon(QIcon("Down-20.png"))
            self.signal_resize_item.emit(self.serialNo(), self.width(), self.ui.pushButton_UpDown.height() + 2)
        else:
            self.resize(self.upDownSize)   
            self.ui.pushButton_UpDown.setIcon(QIcon("Up-20.png"))
            self.signal_resize_item.emit(self.serialNo(), self.width(), self.height())           
        self.upDownCount += 1
     
    @pyqtSlot()
    def on_pushButton_Browse_clicked(self):
        print("on_pushButton_Browse_clicked")
        pass
    
    @pyqtSlot()
    def on_radioButton_file_toggled(self):
        print("on_radioButton_file_toggled")
        pass            
        
    
class ReadingOrderWidget(QWidget):
        
    def __init__(self, width=400, height=130):
        super(ReadingOrderWidget, self).__init__()

        self.__listWidgetItemSerialNo = 0 # Unique index for 
        self.resize(QSize(width + 100, height * 5))
        self.setStyleSheet("QListWidget::item { border-bottom: 1px red; }")
        
        self.listWidget = QListWidget(self)
        self.listWidget.setStyleSheet("QListWidget::item { border-bottom: 1px solid black; }")
    
        self.__itemWidth = width
        self.__itemHeight = height
        '''
        item2 = QListWidgetItem()  # 创建QListWidgetItem对象
        item2.setText("2")
        item2.setSizeHint(QSize(400, 130))  # 设置QListWidgetItem大小
    
        roi1 = ReadingOrderItem()
        
        roi1.signal_resize_item.connect(self.on_signal_resize_item)
        
        roi2 = ReadingOrderItem()
        
        roi2.signal_resize_item.connect(self.on_signal_resize_item)
        
        self.listWidget.addItem(item1)
        self.listWidget.setItemWidget(item1, roi1)
        self.listWidget.addItem(item2)
        self.listWidget.setItemWidget(item2, roi2) 
        '''
        layout = QGridLayout(self)
        layout.addWidget(self.listWidget)
        self.setLayout(layout)
    
    def getItemSize(self):
        return QSize(self.__itemWidth, self.__itemHeight)
    
    def getSerialNo(self):
        return self.__listWidgetItemSerialNo
    
    def addItems(self, number=1):
        
        for i in range(number):
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setText(str(self.listWidget.count()))
            item.setSizeHint(self.getItemSize())  # 设置QListWidgetItem大小
            
            roi = ReadingOrderItem(self.getSerialNo())
            roi.signal_resize_item.connect(self.on_signal_resize_item)
              
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, roi)
            self.__listWidgetItemSerialNo += 1
        '''
        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setText(str(self.listWidget.count()))
        item.setSizeHint(getItemSize())  # 设置QListWidgetItem大小
        
        roi = ReadingOrderItem(self.listWidgetItemSerialNo)      
        roi.signal_resize_item.connect(self.on_signal_resize_item)
          
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, roi)
        self.listWidgetItemSerialNo += 1
        '''
    @pyqtSlot(int, int, int)
    def on_signal_resize_item(self, serialNo, width, height):  
        for i in range(self.listWidget.count()):
            if self.listWidget.itemWidget(self.listWidget.item(i)).serialNo() == serialNo:
                self.listWidget.item(i).setSizeHint(QSize(width, height)) # (width, height)
        print("item[{}] = {} * {}".format(serialNo, width, height))
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    rOW = ReadingOrderWidget()
    rOW.addItems(3)
    
    rOW.show()
    '''
    # 主窗口
    w = QWidget()
    w.resize(QSize(500, 700))
    w.setWindowTitle("QListWindow")
    # 新建QListWidget
    listWidget = QListWidget(w)
    listWidget.setStyleSheet("QListWidget::item { border-bottom: 1px red; }")
    
    #listWidget.setSize(QSize(500, 800))
    
    item1 = QListWidgetItem()  # 创建QListWidgetItem对象
    item1.setSizeHint(QSize(400, 130))  # 设置QListWidgetItem大小
    item2 = QListWidgetItem()  # 创建QListWidgetItem对象
    item2.setSizeHint(QSize(400, 130))  # 设置QListWidgetItem大小

    roi1 = ReadingOrderItem()
    roi2 = ReadingOrderItem()
    
    listWidget.addItem(item1)
    listWidget.setItemWidget(item1, roi1)
    listWidget.addItem(item2)
    listWidget.setItemWidget(item2, roi2) 
    
    layout = QGridLayout()
    layout.addWidget(listWidget)
    w.setLayout(layout)
    
    
    w.show()
    '''
    # item = ReadingOrderItem()
    # item.show()
    
    
    sys.exit(app.exec_())