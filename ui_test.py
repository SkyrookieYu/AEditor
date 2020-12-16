# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(655, 805)

        self.formLayout1 = QFormLayout()
        self.groupBox1 = QGroupBox()

        for n in range(100):
            label1 = QLabel('Slime_%2d' % n)
            label2 = QLabel()
            self.formLayout1.addRow(label1, label2)

        self.groupBox1.setLayout(self.formLayout1)
        
        self.formLayout2 = QFormLayout()
        self.groupBox2 = QGroupBox()

        for n in range(50):
            label1 = QLabel('TTT_%2d' % n)
            label2 = QLabel()
            self.formLayout2.addRow(label1, label2)

        self.groupBox2.setLayout(self.formLayout2)
        
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.groupBox1)
        layout.addWidget(self.groupBox2)
        widget.setLayout(layout)
        
        self.scroll = QScrollArea()
        self.scroll.setWidget(widget)
        self.scroll.setWidgetResizable(True)
       

        self.layout = QVBoxLayout(Form)
        self.layout.addWidget(self.scroll)
        
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
        self.groupBox1.setTitle(_translate("Form", "Required Metadata"))
        '''
        self.label_BT.setText(_translate("Form", "Book Title"))
        self.label_A.setText(_translate("Form", "Author"))
        self.label_R.setText(_translate("Form", "ReadBy"))
        self.label_P.setText(_translate("Form", "Publisher"))
        self.label_PD.setText(_translate("Form", "Publication Date"))
        '''
