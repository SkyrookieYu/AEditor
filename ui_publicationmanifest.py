# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'publicationmanifest_test.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PublicationManifest(object):
    def setupUi(self, PublicationManifest):
        PublicationManifest.setObjectName("PublicationManifest")
        PublicationManifest.resize(574, 871)
        self.gridLayout_2 = QtWidgets.QGridLayout(PublicationManifest)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(PublicationManifest)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 800))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 560, 857))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(400, 850))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 422, 808))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_Required = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_Required.setMinimumSize(QtCore.QSize(420, 170))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.groupBox_Required.setFont(font)
        self.groupBox_Required.setObjectName("groupBox_Required")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_Required)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(self.groupBox_Required)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.label_conformsTo = QtWidgets.QLabel(self.groupBox_Required)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label_conformsTo.setFont(font)
        self.label_conformsTo.setObjectName("label_conformsTo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_conformsTo)
        self.label_context = QtWidgets.QLabel(self.groupBox_Required)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.label_context.setFont(font)
        self.label_context.setObjectName("label_context")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_context)
        self.lineEdit_context = QtWidgets.QLineEdit(self.groupBox_Required)
        self.lineEdit_context.setObjectName("lineEdit_context")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_context)
        self.lineEdit_conformsTo = QtWidgets.QLineEdit(self.groupBox_Required)
        self.lineEdit_conformsTo.setObjectName("lineEdit_conformsTo")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_conformsTo)
        self.lineEdit_name = QtWidgets.QLineEdit(self.groupBox_Required)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_name)
        self.verticalLayout.addWidget(self.groupBox_Required)
        self.groupBox_Optional = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_Optional.setMinimumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        self.groupBox_Optional.setFont(font)
        self.groupBox_Optional.setObjectName("groupBox_Optional")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_Optional)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.groupBox_Optional)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(400, 600))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -319, 600, 900))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(600, 900))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_abridged = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_abridged.setObjectName("label_abridged")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_abridged)
        self.comboBox_abridged = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_abridged.setObjectName("comboBox_abridged")
        self.comboBox_abridged.addItem("")
        self.comboBox_abridged.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.comboBox_abridged)
        self.label_accessibilityFeature = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_accessibilityFeature.setObjectName("label_accessibilityFeature")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_accessibilityFeature)
        self.lineEdit_accessibilityFeature = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_accessibilityFeature.setObjectName("lineEdit_accessibilityFeature")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_accessibilityFeature)
        self.label_accessibilityHazard = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_accessibilityHazard.setObjectName("label_accessibilityHazard")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_accessibilityHazard)
        self.lineEdit_accessibilityHazard = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_accessibilityHazard.setObjectName("lineEdit_accessibilityHazard")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_accessibilityHazard)
        self.label_accessibilitySummary = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_accessibilitySummary.setObjectName("label_accessibilitySummary")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_accessibilitySummary)
        self.lineEdit_accessibilitySummary = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_accessibilitySummary.setObjectName("lineEdit_accessibilitySummary")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_accessibilitySummary)
        self.label_accessMode = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_accessMode.setObjectName("label_accessMode")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_accessMode)
        self.comboBox_accessMode = CheckableComboBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_accessMode.sizePolicy().hasHeightForWidth())
        self.comboBox_accessMode.setSizePolicy(sizePolicy)
        self.comboBox_accessMode.setMinimumSize(QtCore.QSize(227, 0))
        self.comboBox_accessMode.setCurrentText("auditory")
        self.comboBox_accessMode.setMaxVisibleItems(10)
        self.comboBox_accessMode.setObjectName("comboBox_accessMode")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.addItem("")
        self.comboBox_accessMode.setItemText(10, "textOnVisual")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.comboBox_accessMode)
        self.label_accessModeSufficient = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_accessModeSufficient.setObjectName("label_accessModeSufficient")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_accessModeSufficient)
        self.lineEdit_accessModeSufficient = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_accessModeSufficient.setObjectName("lineEdit_accessModeSufficient")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_accessModeSufficient)
        self.label_author = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_author.setObjectName("label_author")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_author)
        self.lineEdit_author = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_author)
        self.label_cover = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_cover.setObjectName("label_cover")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_cover)
        self.lineEdit_cover = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_cover.setObjectName("lineEdit_cover")
        self.formLayout_3.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_cover)
        self.label_duration = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_duration.setObjectName("label_duration")
        self.formLayout_3.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_duration)
        self.lineEdit_duration = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_duration.setText("")
        self.lineEdit_duration.setReadOnly(True)
        self.lineEdit_duration.setObjectName("lineEdit_duration")
        self.formLayout_3.setWidget(17, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_duration)
        self.label_dateModified = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_dateModified.setObjectName("label_dateModified")
        self.formLayout_3.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.label_dateModified)
        self.dateTimeEdit_dateModified = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents_2)
        self.dateTimeEdit_dateModified.setObjectName("dateTimeEdit_dateModified")
        self.formLayout_3.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.dateTimeEdit_dateModified)
        self.label_datePublished = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_datePublished.setObjectName("label_datePublished")
        self.formLayout_3.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_datePublished)
        self.dateTimeEdit_datePublished = QtWidgets.QDateTimeEdit(self.scrollAreaWidgetContents_2)
        self.dateTimeEdit_datePublished.setObjectName("dateTimeEdit_datePublished")
        self.formLayout_3.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.dateTimeEdit_datePublished)
        self.label_id = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_id.setObjectName("label_id")
        self.formLayout_3.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout_3.setWidget(23, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_id)
        self.label_inLanguage = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_inLanguage.setObjectName("label_inLanguage")
        self.formLayout_3.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_inLanguage)
        self.label_readBy = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_readBy.setObjectName("label_readBy")
        self.formLayout_3.setWidget(26, QtWidgets.QFormLayout.LabelRole, self.label_readBy)
        self.lineEdit_readBy = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_readBy.setObjectName("lineEdit_readBy")
        self.formLayout_3.setWidget(27, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_readBy)
        self.label_readingProgression = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_readingProgression.setObjectName("label_readingProgression")
        self.formLayout_3.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.label_readingProgression)
        self.lineEdit_readingProgression = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_readingProgression.setObjectName("lineEdit_readingProgression")
        self.formLayout_3.setWidget(29, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_readingProgression)
        self.label_type = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_type.setObjectName("label_type")
        self.formLayout_3.setWidget(30, QtWidgets.QFormLayout.LabelRole, self.label_type)
        self.lineEdit_type = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_type.setObjectName("lineEdit_type")
        self.formLayout_3.setWidget(31, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_type)
        self.label_url = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_url.setObjectName("label_url")
        self.formLayout_3.setWidget(32, QtWidgets.QFormLayout.LabelRole, self.label_url)
        self.lineEdit_url = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.formLayout_3.setWidget(33, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_url)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setCurrentText("zh-TW")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_3.setWidget(25, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_Optional)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(PublicationManifest)
        self.comboBox_accessMode.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(36)
        QtCore.QMetaObject.connectSlotsByName(PublicationManifest)

    def retranslateUi(self, PublicationManifest):
        _translate = QtCore.QCoreApplication.translate
        PublicationManifest.setWindowTitle(_translate("PublicationManifest", "Form"))
        self.groupBox_Required.setTitle(_translate("PublicationManifest", "Required Metadata"))
        self.label_name.setText(_translate("PublicationManifest", "name(publication title)"))
        self.label_conformsTo.setText(_translate("PublicationManifest", "conformsTo"))
        self.label_context.setText(_translate("PublicationManifest", "@context"))
        self.groupBox_Optional.setTitle(_translate("PublicationManifest", "Optional Metadata"))
        self.label_abridged.setText(_translate("PublicationManifest", "abridged"))
        self.comboBox_abridged.setItemText(0, _translate("PublicationManifest", "true"))
        self.comboBox_abridged.setItemText(1, _translate("PublicationManifest", "false"))
        self.label_accessibilityFeature.setText(_translate("PublicationManifest", "accessibilityFeature"))
        self.label_accessibilityHazard.setText(_translate("PublicationManifest", "accessibilityHazard"))
        self.label_accessibilitySummary.setText(_translate("PublicationManifest", "accessibilitySummary"))
        self.label_accessMode.setText(_translate("PublicationManifest", "accessMode"))
        self.comboBox_accessMode.setItemText(0, _translate("PublicationManifest", "auditory"))
        self.comboBox_accessMode.setItemText(1, _translate("PublicationManifest", "tactile"))
        self.comboBox_accessMode.setItemText(2, _translate("PublicationManifest", "textual"))
        self.comboBox_accessMode.setItemText(3, _translate("PublicationManifest", "visual"))
        self.comboBox_accessMode.setItemText(4, _translate("PublicationManifest", "colorDependent"))
        self.comboBox_accessMode.setItemText(5, _translate("PublicationManifest", "chartOnVisual"))
        self.comboBox_accessMode.setItemText(6, _translate("PublicationManifest", "chemOnVisual"))
        self.comboBox_accessMode.setItemText(7, _translate("PublicationManifest", "diagramOnVisual"))
        self.comboBox_accessMode.setItemText(8, _translate("PublicationManifest", "mathOnVisual"))
        self.comboBox_accessMode.setItemText(9, _translate("PublicationManifest", "musicOnVisual"))
        self.label_accessModeSufficient.setText(_translate("PublicationManifest", "accessModeSufficient"))
        self.label_author.setText(_translate("PublicationManifest", "author"))
        self.label_cover.setText(_translate("PublicationManifest", "cover"))
        self.label_duration.setText(_translate("PublicationManifest", "duration"))
        self.label_dateModified.setText(_translate("PublicationManifest", "dateModified"))
        self.label_datePublished.setText(_translate("PublicationManifest", "datePublished"))
        self.label_id.setText(_translate("PublicationManifest", "id (canonical identifier)"))
        self.label_inLanguage.setText(_translate("PublicationManifest", "inLanguage (publication language)"))
        self.label_readBy.setText(_translate("PublicationManifest", "readBy"))
        self.label_readingProgression.setText(_translate("PublicationManifest", "readingProgression"))
        self.label_type.setText(_translate("PublicationManifest", "type"))
        self.lineEdit_type.setText(_translate("PublicationManifest", "CreativeWork"))
        self.label_url.setText(_translate("PublicationManifest", "url (address)"))
        self.comboBox.setItemText(0, _translate("PublicationManifest", "ar-SA"))
        self.comboBox.setItemText(1, _translate("PublicationManifest", "cs-CZ"))
        self.comboBox.setItemText(2, _translate("PublicationManifest", "da-DK"))
        self.comboBox.setItemText(3, _translate("PublicationManifest", "de-DE"))
        self.comboBox.setItemText(4, _translate("PublicationManifest", "el-GR"))
        self.comboBox.setItemText(5, _translate("PublicationManifest", "en-AU"))
        self.comboBox.setItemText(6, _translate("PublicationManifest", "en-GB"))
        self.comboBox.setItemText(7, _translate("PublicationManifest", "en-IE"))
        self.comboBox.setItemText(8, _translate("PublicationManifest", "en-US"))
        self.comboBox.setItemText(9, _translate("PublicationManifest", "en-ZA"))
        self.comboBox.setItemText(10, _translate("PublicationManifest", "es-ES"))
        self.comboBox.setItemText(11, _translate("PublicationManifest", "es-MX"))
        self.comboBox.setItemText(12, _translate("PublicationManifest", "fi-FI"))
        self.comboBox.setItemText(13, _translate("PublicationManifest", "fr-CA"))
        self.comboBox.setItemText(14, _translate("PublicationManifest", "fr-FR"))
        self.comboBox.setItemText(15, _translate("PublicationManifest", "he-IL"))
        self.comboBox.setItemText(16, _translate("PublicationManifest", "hi-IN"))
        self.comboBox.setItemText(17, _translate("PublicationManifest", "hu-HU"))
        self.comboBox.setItemText(18, _translate("PublicationManifest", "id-ID"))
        self.comboBox.setItemText(19, _translate("PublicationManifest", "it-IT"))
        self.comboBox.setItemText(20, _translate("PublicationManifest", "ja-JP"))
        self.comboBox.setItemText(21, _translate("PublicationManifest", "ko-KR"))
        self.comboBox.setItemText(22, _translate("PublicationManifest", "nl-BE"))
        self.comboBox.setItemText(23, _translate("PublicationManifest", "nl-NL"))
        self.comboBox.setItemText(24, _translate("PublicationManifest", "no-NO"))
        self.comboBox.setItemText(25, _translate("PublicationManifest", "pl-PL"))
        self.comboBox.setItemText(26, _translate("PublicationManifest", "pt-BR"))
        self.comboBox.setItemText(27, _translate("PublicationManifest", "pt-PT"))
        self.comboBox.setItemText(28, _translate("PublicationManifest", "ro-RO"))
        self.comboBox.setItemText(29, _translate("PublicationManifest", "ru-RU"))
        self.comboBox.setItemText(30, _translate("PublicationManifest", "sk-SK"))
        self.comboBox.setItemText(31, _translate("PublicationManifest", "sv-SE"))
        self.comboBox.setItemText(32, _translate("PublicationManifest", "th-TH"))
        self.comboBox.setItemText(33, _translate("PublicationManifest", "tr-TR"))
        self.comboBox.setItemText(34, _translate("PublicationManifest", "zh-CN"))
        self.comboBox.setItemText(35, _translate("PublicationManifest", "zh-HK"))
        self.comboBox.setItemText(36, _translate("PublicationManifest", "zh-TW"))
from checkablecombobox import CheckableComboBox