# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launchpage.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LaunchPage(object):
    def setupUi(self, LaunchPage):
        LaunchPage.setObjectName("LaunchPage")
        LaunchPage.resize(674, 384)
        self.centralwidget = QtWidgets.QWidget(LaunchPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(255, 255, 255);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 12px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_Title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_Title.setGeometry(QtCore.QRect(-10, 80, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        self.label_Title.setFont(font)
        self.label_Title.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.label_Description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_Description.setGeometry(QtCore.QRect(0, 180, 661, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_Description.setFont(font)
        self.label_Description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_Description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Description.setObjectName("label_Description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 230, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(90,90,90);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_Loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_Loading.setGeometry(QtCore.QRect(0, 260, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_Loading.setFont(font)
        self.label_Loading.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_Loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Loading.setObjectName("label_Loading")
        self.label_Credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_Credits.setGeometry(QtCore.QRect(10, 300, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_Credits.setFont(font)
        self.label_Credits.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_Credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Credits.setObjectName("label_Credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        LaunchPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LaunchPage)
        QtCore.QMetaObject.connectSlotsByName(LaunchPage)

    def retranslateUi(self, LaunchPage):
        _translate = QtCore.QCoreApplication.translate
        LaunchPage.setWindowTitle(_translate("LaunchPage", "MainWindow"))
        self.label_Title.setText(_translate("LaunchPage", "<strong>Audiobook Editor</strong>"))
        self.label_Description.setText(_translate("LaunchPage", "<strong>https://github.com/SkyrookieYu/AEditor.git</strong>"))
        self.label_Loading.setText(_translate("LaunchPage", "loading..."))
        self.label_Credits.setText(_translate("LaunchPage", "<strong>Powered by HyRead</strong>"))
