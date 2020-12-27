# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:53:09 2020

@author: ilove
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from multipledispatch import dispatch 

class TreeWidget_TOC(QMainWindow):
    
    @dispatch(list)
    def __init__( self, tocList ):
 
        ## Init:
        super(TreeWidget_TOC, self).__init__(None)
 
        # ----------------
        # Create Simple UI with QTreeWidget
        # ----------------
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.setCentralWidget(self.centralwidget)
 
        # ----------------
        # Set TreeWidget Headers
        # ----------------
        HEADERS = ( "Pickup one file/URL", "Description", "Start Time", "End Time")
        self.treeWidget.setColumnCount(len(HEADERS))
        self.treeWidget.setHeaderLabels(HEADERS)
 
        ## Set Columns Width to match content:
        for column in range(self.treeWidget.columnCount()):
            self.treeWidget.resizeColumnToContents(column)
            
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  
        self.treeWidget.customContextMenuRequested.connect(self.on_menuContext)  
        
        self.treeWidget.setDragDropMode(QAbstractItemView.InternalMove) 
        
        self.on_generateTreeAction_triggered(tocList)
        
    
 
    
    @dispatch()
    def __init__( self, parent = None ):
 
        ## Init:
        super(TreeWidget_TOC, self).__init__( parent )
 
        # ----------------
        # Create Simple UI with QTreeWidget
        # ----------------
        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.setCentralWidget(self.centralwidget)
 
        # ----------------
        # Set TreeWidget Headers
        # ----------------
        HEADERS = ( "Pickup one file/URL", "Description", "Start Time", "End Time")
        self.treeWidget.setColumnCount(len(HEADERS))
        self.treeWidget.setHeaderLabels(HEADERS)
 
        ## Set Columns Width to match content:
        for column in range(self.treeWidget.columnCount()):
            self.treeWidget.resizeColumnToContents(column)
            
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  
        self.treeWidget.customContextMenuRequested.connect(self.on_menuContext)  
        
        self.treeWidget.setDragDropMode(QAbstractItemView.InternalMove)
        
    def on_menuContext(self, point):
        print("on_menuContext")
        item = self.treeWidget.itemAt(point)
        if item is not None:
            print("is not none")
            self.menu_context = QMenu()
            # ajoutFileAtt = self.menu_contextuelAlb.addAction("Ajouter l'album à la file d'attente")
            self.addChildItemAction = self.menu_context.addAction("addChildItem")
            self.addChildItemAction.triggered.connect(self.on_addChildItemAction_triggered)
            self.removeItemAction = self.menu_context.addAction("removeItem")
            self.removeItemAction.triggered.connect(self.on_removeItemAction_triggered)
            self.menu_context.exec_(self.treeWidget.mapToGlobal(point))
            
        else:
            print("none")
            self.menu_context = QMenu()
            # ajoutFileAtt = self.menu_contextuelAlb.addAction("Ajouter l'album à la file d'attente")
            self.addTopLevelItemAction = self.menu_context.addAction("addTopLevelItem")
            self.addTopLevelItemAction.triggered.connect(self.on_addTopLevelItemAction_triggered)
            #self.removeItemAction = self.menu_context.addAction("removeItem")
            #self.removeItemAction.triggered.connect(self.on_removeItemAction_triggered)
            self.traverseTreeAction = self.menu_context.addAction("travere")
            self.traverseTreeAction.triggered.connect(self.on_traverseTreeAction_triggered) # (self.getItemsRecursively) #
            #self.generateTreeAction = self.menu_context.addAction("generate")
            #self.generateTreeAction.triggered.connect(lambda : self.on_generateTreeAction_triggered([{'level': 0, 'href': '1#t=0,100.24', 'title': '111', 'children': []}, {'level': 0, 'href': ' 2#t=100.24,150.52', 'title': '2222', 'children': [{'level': 1, 'href': '  3#t=150.52,200.06', 'title': '3333', 'children': []}]}])) # (self.getItemsRecursively) #
            self.menu_context.exec_(self.treeWidget.mapToGlobal(point))
            
            
    @pyqtSlot(bool)
    def on_addTopLevelItemAction_triggered(self, checked):
        
        print("addTopLevelItem is clicked")
        print(checked)      
        self.treeWidget.addTopLevelItem(CustomTreeItem(self.treeWidget))
        for column in range(self.treeWidget.columnCount()):
            self.treeWidget.resizeColumnToContents(column)
        #self.addItems(1)

    @pyqtSlot(bool)
    def on_addChildItemAction_triggered(self, checked):
        print("addChildItem is clicked")     
        parentItem = self.treeWidget.currentItem()
        item = CustomTreeItem(parentItem)
        
        root = self.treeWidget.invisibleRootItem() 
        (item.parent() or root).setExpanded(True)
        
        for column in range(self.treeWidget.columnCount()):      
            self.treeWidget.header().setSectionResizeMode(column, QHeaderView.ResizeToContents);
        
    @pyqtSlot(bool)
    def on_removeItemAction_triggered(self, checked):  
        print("removeItem is clicked")
        # print("topLevelItemCount() = %d" % self.treeWidget.topLevelItemCount() )
        item = self.treeWidget.currentItem()
        if item.childCount() > 0:
            response = QMessageBox.warning(self,'Warning','This item has child items!', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
            if response == QMessageBox.Discard:       
                root = self.treeWidget.invisibleRootItem() 
                (item.parent() or root).removeChild(item) 
                    
                for column in range(self.treeWidget.columnCount()):
                    self.treeWidget.resizeColumnToContents(column)
            else:
                return
        else:
            root = self.treeWidget.invisibleRootItem() 
            print(root)
            #for item in self.treeWidget.selectedItems(): 
                
            (item.parent() or root).removeChild(item) 
                
            for column in range(self.treeWidget.columnCount()):
                self.treeWidget.resizeColumnToContents(column)            

    
    '''
    e.g., 
    [{'level': 0, 'href': '1', 'title': '1', 'children': [{'level': 1, 'href': '1', 'title': '1.2', 'children': []}]}, 
     {'level': 0, 'href': ' 2', 'title': '2', 'children': [{'level': 1, 'href': '1', 'title': '2.1', 'children': []}, {'level': 1, 'href': ' 2', 'title': '2.2', 'children': []}]}]
    '''
    @pyqtSlot()
    def on_traverseTreeAction_triggered(self):
        print("on_traverseAction_triggered")
        self._TOCList = []
        def serchChildItem(item = None, level = 0):
            TOCList = []
            if not item: 
                return
            for m in range(item.childCount()): 
                child = item.child(m) 
                if child.lineEdit_Start.text() != "" and child.lineEdit_End.text() != "":
                    TOCList.append({"level" : level, "href" : child.comboBox.currentText() + "#t=" + child.lineEdit_Start.text() + "," + child.lineEdit_End.text(), "title" : child.lineEdit.text(), "children" : serchChildItem(child, level + 1)})
                else:               
                    TOCList.append({"level" : level, "href" : child.comboBox.currentText(), "title" : child.lineEdit.text(), "children" : serchChildItem(child, level + 1)})   
            return TOCList
            
        for i in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(i)
            level = 0
            if item.lineEdit_Start.text() != "" and item.lineEdit_End.text() != "":
                self._TOCList.append({"level" : level, "href" : item.comboBox.currentText() + "#t=" + item.lineEdit_Start.text() + "," + item.lineEdit_End.text(), "title" : item.lineEdit.text(), "children" : serchChildItem(item, level + 1)})
            else:
                self._TOCList.append({"level" : level, "href" : item.comboBox.currentText(), "title" : item.lineEdit.text(), "children" : serchChildItem(item, level + 1)})
        print(self._TOCList)

    '''
    e.g., 
    [{'level': 0, 'href': '1', 'title': '1', 'children': [{'level': 1, 'href': '1', 'title': '1.2', 'children': []}]}, 
     {'level': 0, 'href': ' 2', 'title': '2', 'children': [{'level': 1, 'href': '1', 'title': '2.1', 'children': []}, {'level': 1, 'href': ' 2', 'title': '2.2', 'children': []}]}]
    '''
    # https://blog.csdn.net/lly1122334/article/details/103040110 : dict
    def on_generateTreeAction_triggered(self, data, root = None):
        self.treeWidget.clear()
        
        def addChildItem(data, level, parentItem):
            children = data['children']
            if children == []:
                return
            for i in range(len(children)): 
                child = children[i]
                lvl = child['level']
                if lvl == level:
                    item = CustomTreeItem(parentItem)
                    href = child["href"]
                    indexOfSharpSign = href.find('#t=')
                    if indexOfSharpSign == -1: # Not in
                        pass
                    else:
                        timeStamp = href[indexOfSharpSign + 3:]
                        [startTime, endTime] = timeStamp.split(',')
                        item.lineEdit_Start.setText(startTime)
                        item.lineEdit_End.setText(endTime)
                        
                    item.lineEdit.setText(child["title"])
                    addChildItem(child, level + 1, item)
                    
        if isinstance(data, list):
            # self.generateTreeWidget(value, child)
            for i in range(len(data)):
                dict_TOC = data[i]
                level = dict_TOC["level"]
                if level == 0:
                    item = CustomTreeItem(self.treeWidget)
                    # item.comboxBox = 
                    href = dict_TOC["href"]
                    indexOfSharpSign = href.find('#t=')
                    if indexOfSharpSign == -1: # Not in
                        pass
                    else:
                        timeStamp = href[indexOfSharpSign + 3:]
                        [startTime, endTime] = timeStamp.split(',')
                        item.lineEdit_Start.setText(startTime)
                        item.lineEdit_End.setText(endTime)
                    
                    # Todo : comboBox must pickup one item from Reading Order List
                    # item.comboBox.setText(href[0:posOfTimeStamp])
                    
                    item.lineEdit.setText(dict_TOC["title"])
                    self.treeWidget.addTopLevelItem(item) 
                    # if dict_TOC['children'] != []:
                    addChildItem(dict_TOC, level + 1, item)
                    
# ------------------------------------------------------------------------------
# Custom QTreeWidgetItem
# ------------------------------------------------------------------------------
class CustomTreeItem(QTreeWidgetItem):
    '''
    Custom QTreeWidgetItem with Widgets
    '''
    on_comboBoxContextMenuRequested = pyqtSignal(QPoint)
    
    def __init__(self, parent):
        '''
        parent (QTreeWidget) : Item's QTreeWidget parent.
        name   (str)         : Item's name. just an example.
        '''
 
        ## Init super class ( QtGui.QTreeWidgetItem )
        super(CustomTreeItem, self).__init__(parent)
 
        ## Column 0 - Text:
        # self.setText(0, name )
        self.comboBox = QComboBox()
        self.comboBox.addItem("1")
        self.comboBox.addItem(" 2")
        self.comboBox.addItem("  3")
        self.comboBox.setContextMenuPolicy(Qt.CustomContextMenu)
        self.comboBox.customContextMenuRequested.connect(lambda point: self.on_customContextMenuRequested_triggered(self.comboBox.mapToParent(point)))
        self.treeWidget().setItemWidget(self, 0, self.comboBox)        
        
        ## Column 1 - SpinBox:
        self.spinBox = QSpinBox()
        self.spinBox.setValue(0)
        self.lineEdit = QLineEdit()
        self.lineEdit.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit.customContextMenuRequested.connect(lambda point: self.on_customContextMenuRequested_triggered(self.lineEdit.mapToParent(point)))
        self.treeWidget().setItemWidget(self, 1, self.lineEdit)
 
        ## Column 2 - Text:
        self.lineEdit_Start = QLineEdit()
        doubleValidator_Start = QDoubleValidator(self.lineEdit_Start)
        doubleValidator_Start.setRange(0, 100000)
        doubleValidator_Start.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator_Start.setDecimals(2)
        self.lineEdit_Start.setValidator(doubleValidator_Start)
        self.lineEdit_Start.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit_Start.customContextMenuRequested.connect(lambda point: self.on_customContextMenuRequested_triggered(self.lineEdit_Start.mapToParent(point)))
        self.treeWidget().setItemWidget(self, 2, self.lineEdit_Start)

        
        ## Column 3 - Text:
        self.lineEdit_End = QLineEdit()
        doubleValidator_End = QDoubleValidator(self.lineEdit_End)
        doubleValidator_End.setRange(0, 100000)
        doubleValidator_End.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator_End.setDecimals(2)
        self.lineEdit_End.setValidator(doubleValidator_End)
        self.lineEdit_End.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lineEdit_End.customContextMenuRequested.connect(lambda point: self.on_customContextMenuRequested_triggered(self.lineEdit_End.mapToParent(point)))
        self.treeWidget().setItemWidget(self, 3, self.lineEdit_End)
 
    @property
    def href(self):
        '''
        Return name ( 0st column text )
        '''
        return self.comboBox.currentText()
 
    @property
    def description(self):
        '''
        Return value (1nd column)
        '''
        return self.lineEdit.text() 
    
    def on_customContextMenuRequested_triggered(self, point):
        print("on_menuContext")
        # print(type(self)) # <class '__main__.CustomTreeItem'>
        print(point)
        
        # pointInItem = self.comboBox.mapToParent(point)
        # print(pointInItem)        
        customTreeItem = self.treeWidget().itemAt(point)
        
        if customTreeItem is not None:
            print("is not none")
            self.menu_context = QMenu()
            self.addChildItemAction = self.menu_context.addAction("addChildItem")
            self.addChildItemAction.triggered.connect(self.on_addChildItemAction_triggered)
            self.removeItemAction = self.menu_context.addAction("removeItem")
            self.removeItemAction.triggered.connect(self.on_removeItemAction_triggered)
            self.menu_context.exec_(self.treeWidget().mapToGlobal(point))
            
        else:
            print("none")
            self.menu_context = QMenu()
            self.addTopLevelItemAction = self.menu_context.addAction("addTopLevelItem")
            self.addTopLevelItemAction.triggered.connect(self.on_addTopLevelItemAction_triggered)
            #self.removeItemAction = self.menu_context.addAction("removeItem")
            #self.removeItemAction.triggered.connect(self.on_removeItemAction_triggered)
            self.menu_context.exec_(self.treeWidget.mapToGlobal(point))
    
    
    def on_addChildItemAction_triggered(self):
        print("on_addChildItemAction_triggered")
        # parentItem = self.treeWidget().currentItem()
        childItem = CustomTreeItem(self)
        
        root = self.treeWidget().invisibleRootItem() 
        (self or root).setExpanded(True)
        '''
        for column in range(self.treeWidget().columnCount()):      
            self.treeWidget().header().setSectionResizeMode(column, QHeaderView.ResizeToContents);
        '''
        
    def on_removeItemAction_triggered(self):
        print("on_removeItemAction_triggered")
        # item = self.treeWidget().currentItem()
        if self.childCount() > 0:
            response = QMessageBox.warning(self.treeWidget(), 'Warning', 'This item has child items!', QMessageBox.Discard | QMessageBox.Cancel, QMessageBox.Cancel)
            if response == QMessageBox.Discard:       
                root = self.treeWidget().invisibleRootItem() 
                (self.parent() or root).removeChild(self) 
                '''    
                for column in range(self.treeWidget.columnCount()):
                    self.treeWidget.resizeColumnToContents(column)
                '''
            else:
                return
        else:
            root = self.treeWidget().invisibleRootItem() 
            print(root)
            #for item in self.treeWidget.selectedItems(): 
                
            (self.parent() or root).removeChild(self) 
            '''    
            for column in range(self.treeWidget().columnCount()):
                self.treeWidget.resizeColumnToContents(column)            
            '''

 
# ------------------------------------------------------------------------------
# __name__
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TreeWidget_TOC()
    ex.show()
    sys.exit(app.exec_())