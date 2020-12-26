# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newbookwizard.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewBookWizard(object):
    def setupUi(self, NewBookWizard):
        NewBookWizard.setObjectName("NewBookWizard")
        NewBookWizard.resize(630, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewBookWizard.sizePolicy().hasHeightForWidth())
        NewBookWizard.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(24)
        NewBookWizard.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(NewBookWizard)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 140, 511, 238))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_BookTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_BookTitle.setFont(font)
        self.label_BookTitle.setObjectName("label_BookTitle")
        self.verticalLayout.addWidget(self.label_BookTitle)
        self.label_Author = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Author.setFont(font)
        self.label_Author.setObjectName("label_Author")
        self.verticalLayout.addWidget(self.label_Author)
        self.label_ReadBy = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_ReadBy.setFont(font)
        self.label_ReadBy.setObjectName("label_ReadBy")
        self.verticalLayout.addWidget(self.label_ReadBy)
        self.label_Publisher = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_Publisher.setFont(font)
        self.label_Publisher.setObjectName("label_Publisher")
        self.verticalLayout.addWidget(self.label_Publisher)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_BookTitle = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_BookTitle.setObjectName("lineEdit_BookTitle")
        self.verticalLayout_2.addWidget(self.lineEdit_BookTitle)
        self.lineEdit_Author = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Author.setObjectName("lineEdit_Author")
        self.verticalLayout_2.addWidget(self.lineEdit_Author)
        self.lineEdit_ReadBy = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ReadBy.setObjectName("lineEdit_ReadBy")
        self.verticalLayout_2.addWidget(self.lineEdit_ReadBy)
        self.lineEdit_Publisher = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Publisher.setObjectName("lineEdit_Publisher")
        self.verticalLayout_2.addWidget(self.lineEdit_Publisher)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(NewBookWizard)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 89, 591, 34))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_FilePath = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_FilePath.setFont(font)
        self.label_FilePath.setObjectName("label_FilePath")
        self.horizontalLayout_2.addWidget(self.label_FilePath)
        self.le_FilePath = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_FilePath.setReadOnly(True)
        self.le_FilePath.setObjectName("le_FilePath")
        self.horizontalLayout_2.addWidget(self.le_FilePath)
        self.button_Browse = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Browse.sizePolicy().hasHeightForWidth())
        self.button_Browse.setSizePolicy(sizePolicy)
        self.button_Browse.setMinimumSize(QtCore.QSize(81, 25))
        self.button_Browse.setMaximumSize(QtCore.QSize(81, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_Browse.setFont(font)
        self.button_Browse.setObjectName("button_Browse")
        self.horizontalLayout_2.addWidget(self.button_Browse)
        self.cb_Embedded = QtWidgets.QCheckBox(NewBookWizard)
        self.cb_Embedded.setGeometry(QtCore.QRect(70, 400, 461, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_Embedded.sizePolicy().hasHeightForWidth())
        self.cb_Embedded.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_Embedded.setFont(font)
        self.cb_Embedded.setObjectName("cb_Embedded")
        self.label_Logo = QtWidgets.QLabel(NewBookWizard)
        self.label_Logo.setGeometry(QtCore.QRect(11, 11, 181, 57))
        self.label_Logo.setText("")
        self.label_Logo.setPixmap(QtGui.QPixmap("hyread-footer-logo-pc.png"))
        self.label_Logo.setObjectName("label_Logo")
        self.label_PageTitle = QtWidgets.QLabel(NewBookWizard)
        self.label_PageTitle.setGeometry(QtCore.QRect(210, 30, 391, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_PageTitle.setFont(font)
        self.label_PageTitle.setObjectName("label_PageTitle")
        self.layoutWidget2 = QtWidgets.QWidget(NewBookWizard)
        self.layoutWidget2.setGeometry(QtCore.QRect(240, 440, 134, 27))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_Create = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Create.sizePolicy().hasHeightForWidth())
        self.button_Create.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_Create.setFont(font)
        self.button_Create.setObjectName("button_Create")
        self.horizontalLayout_3.addWidget(self.button_Create)
        self.button_Cancel = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_Cancel.sizePolicy().hasHeightForWidth())
        self.button_Cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button_Cancel.setFont(font)
        self.button_Cancel.setObjectName("button_Cancel")
        self.horizontalLayout_3.addWidget(self.button_Cancel)

        self.retranslateUi(NewBookWizard)
        QtCore.QMetaObject.connectSlotsByName(NewBookWizard)

    def retranslateUi(self, NewBookWizard):
        _translate = QtCore.QCoreApplication.translate
        NewBookWizard.setWindowTitle(_translate("NewBookWizard", "Dialog"))
        self.label_BookTitle.setText(_translate("NewBookWizard", "Book Title"))
        self.label_Author.setText(_translate("NewBookWizard", "Author"))
        self.label_ReadBy.setText(_translate("NewBookWizard", "ReadBy"))
        self.label_Publisher.setText(_translate("NewBookWizard", "Publisher"))
        self.label_FilePath.setText(_translate("NewBookWizard", "Book Directory:"))
        self.button_Browse.setText(_translate("NewBookWizard", "Browse"))
        self.cb_Embedded.setText(_translate("NewBookWizard", "Embeded Manifest in Primary Entry Page(PEP)"))
        self.label_PageTitle.setText(_translate("NewBookWizard", "New Audiobook Wizard"))
        self.button_Create.setText(_translate("NewBookWizard", "Create"))
        self.button_Cancel.setText(_translate("NewBookWizard", "Cancel"))
