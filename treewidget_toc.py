# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:53:09 2020

@author: ilove
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 

class TreeWidget_TOC(QMainWindow):
 
    def __init__( self, parent=None ):
 
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
        HEADERS = ( "Pickup one file/URL", "Description")
        self.treeWidget.setColumnCount(len(HEADERS))
        self.treeWidget.setHeaderLabels(HEADERS)
 
        # ----------------
        # Add Custom QTreeWidgetItem
        # ----------------
        ## Add Items:
        '''
        for name in [ 'rock', 'paper', 'scissors' ]:
            item = CustomTreeItem( self.treeWidget, name )
            seconditem = CustomTreeItem( item, "paper" )
        '''
        ## Set Columns Width to match content:
        for column in range(self.treeWidget.columnCount()):
            self.treeWidget.resizeColumnToContents(column)
            
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)  
        self.treeWidget.customContextMenuRequested.connect(self.on_menuContext)  
        # self.actionOuvrir.triggered.connect(self.menu)  
        
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
 
        ## Column 2 - Button:
        '''
        self.button = QPushButton()
        self.button.setText( "button %s" % self.option )
        self.treeWidget().setItemWidget(self, 2, self.button )
        '''
        ## Signals
        # self.button.clicked.connect(self.buttonPressed )
 
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