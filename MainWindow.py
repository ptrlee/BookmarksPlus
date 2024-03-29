# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from Bookspace import BookspacesData
import subprocess
import sys

from PyQt5.QtWidgets import *
import CreateBookspace

scripts_path = Path(os.path.dirname(os.path.realpath(__file__)) + '/scripts')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.createBookspaceWindows = []
        self.windows = []
        self.allScriptsListed = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBookspaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.addBookspaceButton.setGeometry(QtCore.QRect(300, 450, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBookspaceButton.setFont(font)
        self.addBookspaceButton.setIconSize(QtCore.QSize(16, 16))
        self.addBookspaceButton.setObjectName("addBookspaceButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 430, 821, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(-5, 51, 811, 391))
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setObjectName("listWidget")

        self.listWidget.itemDoubleClicked.connect(self.runBookspace)
        self.addBookspaces(self.listWidget)
        self.addBookspaceButton.clicked.connect(self.createNewBookspaceWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFILE = QtWidgets.QMenu(self.menubar)
        self.menuFILE.setObjectName("menuFILE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Bookspace = QtWidgets.QAction(MainWindow)
        self.actionNew_Bookspace.setObjectName("actionNew_Bookspace")
        self.actionNew_Bookspace.triggered.connect(self.createNewBookspaceWindow)
        self.menuFILE.addAction(self.actionNew_Bookspace)
        self.menubar.addAction(self.menuFILE.menuAction())

        MainWindow.setWindowIcon(QtGui.QIcon(join(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'icon.png')))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def addBookspaces(self, listWidget):
        self.allScriptsListed.clear()
        self.listWidget.clear()
        onlyfiles = [f for f in listdir(scripts_path) if isfile(join(scripts_path, f))]
        for file in onlyfiles:
            self.addBookspaceToListWidget(listWidget, file)

    def addBookspaceToListWidget(self, listWidget, filename):
        lWItem = QtWidgets.QListWidgetItem()
        bookspace = QtWidgets.QWidget()
        bookspaceText = QtWidgets.QLabel(filename.replace('.py', ' '))
        bookpaceButton = QtWidgets.QPushButton("DELETE")
        bookpaceButton.clicked.connect(lambda: self.deleteBookspace(filename))
        widgetLayout = QtWidgets.QHBoxLayout()
        widgetLayout.addWidget(bookspaceText)
        widgetLayout.addWidget(bookpaceButton, alignment=QtCore.Qt.AlignRight)
        widgetLayout.addStretch()
        bookspace.setLayout(widgetLayout)
        lWItem.setSizeHint(bookspace.sizeHint())

        listWidget.addItem(lWItem)
        listWidget.setItemWidget(lWItem, bookspace)

        self.allScriptsListed.append((lWItem, filename))

    def runBookspace(self, item):
        for tuple in self.allScriptsListed:
            if item == tuple[0]:
                subprocess.Popen([sys.executable, join(scripts_path, tuple[1])])
                return
        errorMessage = QtWidgets.QErrorMessage()
        self.windows.append(errorMessage)
        errorMessage.showMessage('Bookspace not found. Perhaps it was deleted?')

    def deleteBookspace(self, filename):
        filepath = join(scripts_path, filename)
        BookspacesData.delete_bookspace(filename[:-3])
        # os.remove(filepath)
        self.listWidget.clear()
        self.addBookspaces(self.listWidget)


    def createNewBookspaceWindow(self):
        createBookspaceWindow = CreateBookspace.CreateBookspace(self)
        self.createBookspaceWindows.append(createBookspaceWindow)
        createBookspaceWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bookmarks Plus!"))
        self.addBookspaceButton.setText(_translate("MainWindow", "Add Bookspace"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffaa00;\">SELECT A BOOKSPACE!</span></p></body></html>"))
        self.menuFILE.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Bookspace.setText(_translate("MainWindow", "New Bookspace"))
        self.actionNew_Bookspace.setStatusTip(_translate("MainWindow", "Create a new bookspace"))


if __name__ == "__main__":
    try:
        os.mkdir(scripts_path)
    except FileExistsError:
        print('/scripts folder already exists, continuing')
        pass

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.activateWindow()
    sys.exit(app.exec_())