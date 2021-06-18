# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WordCodify.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(493, 123)
        MainWindow.setCursor(QCursor(Qt.IBeamCursor))
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: qconicalgradient(cx:0.488636, cy:0.511, angle:317.5, stop:0.0568182 rgba(2, 163, 146, 252), stop:0.698864 rgba(0, 186, 151, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 471, 106))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 63 italic 10pt \"Segoe UI\";\n"
"color: rgb(19, 41, 61)")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setIndent(0)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 63 italic 10pt \"Segoe UI\";\n"
"color:rgb(19, 41, 61)")

        self.horizontalLayout.addWidget(self.label)

        self.inputWord = QLineEdit(self.verticalLayoutWidget)
        self.inputWord.setObjectName(u"inputWord")

        self.horizontalLayout.addWidget(self.inputWord)

        self.btnGen = QPushButton(self.verticalLayoutWidget)
        self.btnGen.setObjectName(u"btnGen")
        self.btnGen.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btnGen)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.showNewPass = QLabel(self.verticalLayoutWidget)
        self.showNewPass.setObjectName(u"showNewPass")
        self.showNewPass.setMouseTracking(False)
        self.showNewPass.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color:rgb(19, 41, 61)")
        self.showNewPass.setAlignment(Qt.AlignCenter)
        self.showNewPass.setWordWrap(False)
        self.showNewPass.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.showNewPass)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WordCodify", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Letters outside this range will not be used</p><p align=\"center\">A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 # $ % &amp;</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter word to encrypt", None))
        self.btnGen.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.showNewPass.setText("")
    # retranslateUi

