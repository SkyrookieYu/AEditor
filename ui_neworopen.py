# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'neworopen.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewOrOpen(object):
    def setupUi(self, NewOrOpen):
        NewOrOpen.setObjectName("NewOrOpen")
        NewOrOpen.resize(479, 283)
        self.tb_Readme = QtWidgets.QTextBrowser(NewOrOpen)
        self.tb_Readme.setGeometry(QtCore.QRect(10, 29, 180, 201))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.tb_Readme.setFont(font)
        self.tb_Readme.setObjectName("tb_Readme")
        self.line = QtWidgets.QFrame(NewOrOpen)
        self.line.setGeometry(QtCore.QRect(190, 20, 20, 241))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(NewOrOpen)
        self.widget.setGeometry(QtCore.QRect(40, 240, 118, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_New = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.button_New.setFont(font)
        self.button_New.setObjectName("button_New")
        self.horizontalLayout.addWidget(self.button_New)
        self.button_Open = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.button_Open.setFont(font)
        self.button_Open.setIconSize(QtCore.QSize(20, 20))
        self.button_Open.setObjectName("button_Open")
        self.horizontalLayout.addWidget(self.button_Open)
        self.widget1 = QtWidgets.QWidget(NewOrOpen)
        self.widget1.setGeometry(QtCore.QRect(210, 11, 258, 261))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.widget1)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        self.retranslateUi(NewOrOpen)
        QtCore.QMetaObject.connectSlotsByName(NewOrOpen)

    def retranslateUi(self, NewOrOpen):
        _translate = QtCore.QCoreApplication.translate
        NewOrOpen.setWindowTitle(_translate("NewOrOpen", "New or Open?"))
        self.tb_Readme.setHtml(_translate("NewOrOpen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier New\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\';\">This is a public prototype conforming and demostrating the Audiobooks, W3C </span><span style=\" font-family:\'PMingLiU\'; color:#000000; background-color:#ffffff;\">Recommendation</span><span style=\" font-family:\'PMingLiU\'; color:#000000;\"> 10 November 2020.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'PMingLiU\'; color:#000000;\">Have fun!</span></p></body></html>"))
        self.button_New.setText(_translate("NewOrOpen", "New"))
        self.button_Open.setText(_translate("NewOrOpen", "Open"))
        self.label.setText(_translate("NewOrOpen", "Recently opened files..."))
