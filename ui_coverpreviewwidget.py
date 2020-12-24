# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coverpreviewwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CoverPreviewWidget(object):
    def setupUi(self, CoverPreviewWidget):
        CoverPreviewWidget.setObjectName("CoverPreviewWidget")
        CoverPreviewWidget.resize(420, 483)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CoverPreviewWidget.sizePolicy().hasHeightForWidth())
        CoverPreviewWidget.setSizePolicy(sizePolicy)
        CoverPreviewWidget.setMinimumSize(QtCore.QSize(420, 483))
        CoverPreviewWidget.setMaximumSize(QtCore.QSize(420, 483))
        self.label_Cover = QtWidgets.QLabel(CoverPreviewWidget)
        self.label_Cover.setGeometry(QtCore.QRect(50, 30, 320, 320))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Cover.sizePolicy().hasHeightForWidth())
        self.label_Cover.setSizePolicy(sizePolicy)
        self.label_Cover.setMinimumSize(QtCore.QSize(320, 320))
        self.label_Cover.setMaximumSize(QtCore.QSize(320, 320))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_Cover.setFont(font)
        self.label_Cover.setText("")
        self.label_Cover.setPixmap(QtGui.QPixmap("W3C.svg"))
        self.label_Cover.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cover.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_Cover.setObjectName("label_Cover")
        self.pushButton_Add = QtWidgets.QPushButton(CoverPreviewWidget)
        self.pushButton_Add.setGeometry(QtCore.QRect(120, 432, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Add.sizePolicy().hasHeightForWidth())
        self.pushButton_Add.setSizePolicy(sizePolicy)
        self.pushButton_Add.setMinimumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setAutoExclusive(True)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.buttonGroup = QtWidgets.QButtonGroup(CoverPreviewWidget)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.pushButton_Add)
        self.pushButton_Remove = QtWidgets.QPushButton(CoverPreviewWidget)
        self.pushButton_Remove.setGeometry(QtCore.QRect(229, 432, 71, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Remove.sizePolicy().hasHeightForWidth())
        self.pushButton_Remove.setSizePolicy(sizePolicy)
        self.pushButton_Remove.setMinimumSize(QtCore.QSize(71, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setAutoExclusive(True)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.buttonGroup.addButton(self.pushButton_Remove)
        self.lineEdit = QtWidgets.QLineEdit(CoverPreviewWidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 380, 320, 22))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(CoverPreviewWidget)
        QtCore.QMetaObject.connectSlotsByName(CoverPreviewWidget)

    def retranslateUi(self, CoverPreviewWidget):
        _translate = QtCore.QCoreApplication.translate
        CoverPreviewWidget.setWindowTitle(_translate("CoverPreviewWidget", "CoverPreviewWidget"))
        self.pushButton_Add.setText(_translate("CoverPreviewWidget", "Add"))
        self.pushButton_Remove.setText(_translate("CoverPreviewWidget", "Remove"))
