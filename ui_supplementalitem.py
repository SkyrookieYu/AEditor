# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supplementalitem.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SupplementalItem(object):
    def setupUi(self, SupplementalItem):
        SupplementalItem.setObjectName("SupplementalItem")
        SupplementalItem.resize(470, 70)
        SupplementalItem.setMinimumSize(QtCore.QSize(470, 38))
        self.label_file = QtWidgets.QLabel(SupplementalItem)
        self.label_file.setGeometry(QtCore.QRect(30, 10, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_file.setFont(font)
        self.label_file.setObjectName("label_file")
        self.lineEdit_file = QtWidgets.QLineEdit(SupplementalItem)
        self.lineEdit_file.setGeometry(QtCore.QRect(110, 10, 261, 20))
        self.lineEdit_file.setObjectName("lineEdit_file")
        self.pushButton_Browse = QtWidgets.QPushButton(SupplementalItem)
        self.pushButton_Browse.setGeometry(QtCore.QRect(380, 10, 62, 22))
        self.pushButton_Browse.setMinimumSize(QtCore.QSize(60, 20))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Browse.setFont(font)
        self.pushButton_Browse.setObjectName("pushButton_Browse")
        self.lineEdit_URL = QtWidgets.QLineEdit(SupplementalItem)
        self.lineEdit_URL.setGeometry(QtCore.QRect(110, 40, 331, 20))
        self.lineEdit_URL.setObjectName("lineEdit_URL")
        self.label_URL = QtWidgets.QLabel(SupplementalItem)
        self.label_URL.setGeometry(QtCore.QRect(30, 40, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_URL.setFont(font)
        self.label_URL.setObjectName("label_URL")
        self.radioButton_file = QtWidgets.QRadioButton(SupplementalItem)
        self.radioButton_file.setGeometry(QtCore.QRect(90, 10, 21, 21))
        self.radioButton_file.setMinimumSize(QtCore.QSize(21, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.radioButton_file.setFont(font)
        self.radioButton_file.setText("")
        self.radioButton_file.setChecked(True)
        self.radioButton_file.setObjectName("radioButton_file")
        self.radioButton_URL = QtWidgets.QRadioButton(SupplementalItem)
        self.radioButton_URL.setGeometry(QtCore.QRect(90, 40, 21, 21))
        self.radioButton_URL.setMinimumSize(QtCore.QSize(21, 21))
        self.radioButton_URL.setText("")
        self.radioButton_URL.setChecked(False)
        self.radioButton_URL.setObjectName("radioButton_URL")

        self.retranslateUi(SupplementalItem)
        QtCore.QMetaObject.connectSlotsByName(SupplementalItem)

    def retranslateUi(self, SupplementalItem):
        _translate = QtCore.QCoreApplication.translate
        SupplementalItem.setWindowTitle(_translate("SupplementalItem", "Form"))
        self.label_file.setText(_translate("SupplementalItem", "file:"))
        self.pushButton_Browse.setText(_translate("SupplementalItem", "Browse"))
        self.label_URL.setText(_translate("SupplementalItem", "URL:"))
