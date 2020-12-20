# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 01:15:55 2020

@URL: https://github.com/SkyrookieYu/AEditor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import librosa
# from mimetypes import MimeTypes
import filetype

from ui_supplementalitem import Ui_SupplementalItem

class SupplementalItem(QWidget):
    
    # switch_window = pyqtSignal()
    # signal_resize_item = pyqtSignal(int, int, int)
    
    def __init__(self, serialNo=-1):
        super(SupplementalItem, self).__init__()

        self.ui = Ui_SupplementalItem()
        self.ui.setupUi(self)
        self._translate = QCoreApplication.translate
        
        self.__serialNo = serialNo
        # 0/Even: Up, Odd: Down
        self.upDownCount = 0 
        self.upDownSize = self.size()
        
        self.ui.radioButton_file.toggled.connect(lambda: self.on_radioButton_toggled(self.serialNo()))
        
    def serialNo(self):
        return self.__serialNo
        
    @pyqtSlot()
    def on_pushButton_Browse_clicked(self):
        print("on_pushButton_Browse_clicked")
        pass
    
    @pyqtSlot(int)
    def on_radioButton_toggled(self, serialNo):
        print("{} on_radioButton_file_toggled".format(serialNo))
        pass 
 
class SupplementalListWidget(QWidget):
        
    def __init__(self, width=500, height=70):
        super(SupplementalListWidget, self).__init__()

        self.__listWidgetItemSerialNo = 0 # Unique index for 
        
        self.setGeometry(QRect(60, 70, 680, 790))
        
        self.resize(QSize(width + 100, height * 6))
        
        self.setStyleSheet("QListWidget::item { border-bottom: 1px red; }")
        
        self.listWidget = QListWidget(self)
        self.listWidget.setStyleSheet("QListWidget::item { border-bottom: 1px solid black; }")
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
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

        layout.addWidget(self.listWidget)
        layout.addLayout(horizontalLayout)
        
        self.setLayout(layout)
        
        self.retranslateUi(SupplementalListWidget)        
   
    def retranslateUi(self, SupplementalListWidget):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("SupplementalListWidget", "SupplementalListWidget"))
        self.pushButton_Add.setText(_translate("SupplementalListWidget", "Add"))
        self.pushButton_Remove.setText(_translate("SupplementalListWidget", "Remove"))
    
    def getItemSize(self):
        return QSize(self.__itemWidth, self.__itemHeight)
    
    def getSerialNo(self):
        return self.__listWidgetItemSerialNo
    
    def addItems(self, number=1):       
        for i in range(number):
            item = QListWidgetItem()  
            item.setText(str(self.listWidget.count()))
            item.setSizeHint(self.getItemSize()) 
            
            roi = SupplementalItem(self.getSerialNo())
            # roi.signal_resize_item.connect(self.on_signal_resize_item)
              
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, roi)
            self.__listWidgetItemSerialNo += 1

    def removeSelectedItems(self):       
        items = self.listWidget.selectedItems()  
        for item in items:
            oldItem = self.listWidget.takeItem(self.listWidget.row(item))
            del oldItem

    '''
    @pyqtSlot(int, int, int)
    def on_signal_resize_item(self, serialNo, width, height):  
        for i in range(self.listWidget.count()):
            if self.listWidget.itemWidget(self.listWidget.item(i)).serialNo() == serialNo:
                self.listWidget.item(i).setSizeHint(QSize(width, height)) # (width, height)
        print("item[{}] = {} * {}".format(serialNo, width, height))
    '''
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    

    item = SupplementalListWidget()
    item.addItems()
    item.show()
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

    roi1 = SupplementalItem()
    roi2 = SupplementalItem()
    
    listWidget.addItem(item1)
    listWidget.setItemWidget(item1, roi1)
    listWidget.addItem(item2)
    listWidget.setItemWidget(item2, roi2) 
    
    layout = QGridLayout()
    layout.addWidget(listWidget)
    w.setLayout(layout)
    w.show()
    '''
    
    

    
    
    sys.exit(app.exec_())