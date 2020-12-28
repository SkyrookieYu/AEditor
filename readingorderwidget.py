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
# import librosa
# from mimetypes import MimeTypes
import filetype
from multipledispatch import dispatch

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
    
    @dispatch(list, str)    
    def __init__(self, rList, bookDir, width=400, height=130):
        super(ReadingOrderWidget, self).__init__()

        self.__listWidgetItemSerialNo = 0 # Unique index for 
        
        self.setGeometry(QRect(60, 70, 680, 790))
        
        self.resize(QSize(width + 100, height * 6))
        
        self.setStyleSheet("QListWidget::item { border-bottom: 1px red; }")
        
        self.listWidget = QListWidget(self)
        self.listWidget.setStyleSheet("QListWidget::item { border-bottom: 1px solid black; }")
    
        self.__itemWidth = width
        self.__itemHeight = height

        layout = QVBoxLayout()  # QGridLayout(self)  # 
        
 
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setObjectName("pushButton_Add")
        horizontalLayout.addWidget(self.pushButton_Add)
        self.pushButton_Remove = QPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Remove.sizePolicy().hasHeightForWidth())
        self.pushButton_Remove.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        horizontalLayout.addWidget(self.pushButton_Remove)
        
        self.label_ReadingOrderEditor = QLabel(self)
        self.label_ReadingOrderEditor.setGeometry(QRect(220, 10, 301, 63))
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_ReadingOrderEditor.setFont(font)
        self.label_ReadingOrderEditor.setAlignment(Qt.AlignCenter)
        self.label_ReadingOrderEditor.setObjectName("label_ReadingOrderEditor")
        
        layout.addWidget(self.label_ReadingOrderEditor)
        layout.addWidget(self.listWidget)
        layout.addLayout(horizontalLayout)
        
        self.setLayout(layout)
        
        self.retranslateUi(ReadingOrderWidget)      
        
        for r in rList:
            if isinstance(r, dict):
                url = r.get("url", "")
                
                item = QListWidgetItem()  
                item.setText(str(self.listWidget.count()))
                item.setSizeHint(self.getItemSize()) 
                
                roi = ReadingOrderItem(self.getSerialNo())
                roi.signal_resize_item.connect(self.on_signal_resize_item)
                
                if url.startswith("http"):
                    roi.ui.radioButton_URL.setChecked(True)
                    roi.ui.lineEdit_URL.setText(url)
                    roi.ui.lineEdit_file.setText("")
                else:
                    roi.ui.radioButton_file.setChecked(True)
                    roi.ui.lineEdit_file.setText(url)
                    roi.ui.lineEdit_URL.setText("")
                        
                roi.ui.lineEdit_duration.setText(r.get("duration", ""))    
                roi.ui.lineEdit_title.setText(r.get("name", ""))   
                
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, roi)
                self.__listWidgetItemSerialNo += 1
                
            elif isinstance(r, str):
                print("isinstance(r, str)")
                url = r
                
                item = QListWidgetItem()  
                item.setText(str(self.listWidget.count()))
                item.setSizeHint(self.getItemSize()) 
                
                roi = ReadingOrderItem(self.getSerialNo())
                roi.signal_resize_item.connect(self.on_signal_resize_item)
                
                if url.startswith("http"):
                    roi.ui.radioButton_URL.setChecked(True)
                    roi.ui.lineEdit_URL.setText(url)
                    roi.ui.lineEdit_file.setText("")
                else:
                    roi.ui.radioButton_file.setChecked(True)
                    roi.ui.lineEdit_file.setText(url)
                    roi.ui.lineEdit_URL.setText("")
                    
                    kind = filetype.guess(bookDir + r'/' + url)
                    if kind is None:
                        print('Cannot guess file type!')
                    else:    
                        print('File extension: %s' % kind.extension)
                        print('File MIME type: %s' % kind.mime)
                        if kind.extension == ".mp3" and kind.mime.beginswith("audio"):
                            duration = Helper.getMP3Duration(bookDir + r'/' + url)
                            roi.ui.lineEdit_duration.setText("PT" + str(duration) + "S")    
                                       
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, roi)
                self.__listWidgetItemSerialNo += 1    
    
    
    
    
    
    @dispatch()    
    def __init__(self, width=400, height=130):
        super(ReadingOrderWidget, self).__init__()

        self.__listWidgetItemSerialNo = 0 # Unique index for 
        
        self.setGeometry(QRect(60, 70, 680, 790))
        
        self.resize(QSize(width + 100, height * 6))
        
        self.setStyleSheet("QListWidget::item { border-bottom: 1px red; }")
        
        self.listWidget = QListWidget(self)
        self.listWidget.setStyleSheet("QListWidget::item { border-bottom: 1px solid black; }")
    
        self.__itemWidth = width
        self.__itemHeight = height

        layout = QVBoxLayout()  # QGridLayout(self)  # 
        
 
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Add = QPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setObjectName("pushButton_Add")
        horizontalLayout.addWidget(self.pushButton_Add)
        self.pushButton_Remove = QPushButton(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Remove.sizePolicy().hasHeightForWidth())
        self.pushButton_Remove.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        horizontalLayout.addWidget(self.pushButton_Remove)
        
        self.label_ReadingOrderEditor = QLabel(self)
        self.label_ReadingOrderEditor.setGeometry(QRect(220, 10, 301, 63))
        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        self.label_ReadingOrderEditor.setFont(font)
        self.label_ReadingOrderEditor.setAlignment(Qt.AlignCenter)
        self.label_ReadingOrderEditor.setObjectName("label_ReadingOrderEditor")
        
        layout.addWidget(self.label_ReadingOrderEditor)
        layout.addWidget(self.listWidget)
        layout.addLayout(horizontalLayout)
        
        self.setLayout(layout)
        
        self.pushButton_Add.clicked.connect(self.addItems)
        self.pushButton_Remove.clicked.connect(self.removeSelectedItems)
        
        self.retranslateUi(ReadingOrderWidget)        
   
    def retranslateUi(self, ReadingOrderWidget):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("ReadingOrderWidget", "ReadingOrderWidget"))
        self.pushButton_Add.setText(_translate("ReadingOrderWidget", "Add"))
        self.pushButton_Remove.setText(_translate("ReadingOrderWidget", "Remove"))
        self.label_ReadingOrderEditor.setText(_translate("ReadingOrderWidget", "Reading Order Editor"))
    
    def getItemSize(self):
        return QSize(self.__itemWidth, self.__itemHeight)
    
    def getSerialNo(self):
        return self.__listWidgetItemSerialNo
    
    @pyqtSlot()
    def addItems(self, number=1):       
        for i in range(number):
            item = QListWidgetItem()  
            item.setText(str(self.listWidget.count()))
            item.setSizeHint(self.getItemSize()) 
            
            roi = ReadingOrderItem(self.getSerialNo())
            roi.signal_resize_item.connect(self.on_signal_resize_item)
              
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, roi)
            self.__listWidgetItemSerialNo += 1

    @pyqtSlot()
    def removeSelectedItems(self):       
        items = self.listWidget.selectedItems()  
        for item in items:
            oldItem = self.listWidget.takeItem(self.listWidget.row(item))
            del oldItem
        self.resortItems()

    @pyqtSlot(int, int, int)
    def on_signal_resize_item(self, serialNo, width, height):  
        for i in range(self.listWidget.count()):
            if self.listWidget.itemWidget(self.listWidget.item(i)).serialNo() == serialNo:
                self.listWidget.item(i).setSizeHint(QSize(width, height)) # (width, height)
        print("item[{}] = {} * {}".format(serialNo, width, height))
        
    def resortItems(self):
        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setText(str(i))
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    rOW = ReadingOrderWidget()
    rOW.addItems(3)
    rOW.removeSelectedItems()
    
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