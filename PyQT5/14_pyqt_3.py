# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myinterfaceTmYupj.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2 import QtWidgets
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(364, 311)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 211, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 10, 301, 191))
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        font1.setWeight(75)
        self.textEdit.setFont(font1)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("TXT", 1)
        self.comboBox.addItem("HTML", 2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 220, 181, 41))
        # self.pushButton = QPushButton(self.centralwidget)
        # self.pushButton.setObjectName(u"pushButton")
        # self.pushButton.setGeometry(QRect(220, 220, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 364, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


        self.comboBox.activated.connect(self.handleActivated)
        #self.pushButton.clicked.connect(self.check_choose)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c TXT", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c HTML", None))

        # self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi
    def handleActivated(self, index):
        if self.comboBox.itemData(index) == 2:
            self.save_click_html()
        else:
            self.save_click_txt()


    def save_click_txt(self):
        text = self.textEdit.toPlainText()
        print('txt saved')
        with open('myfile.txt', 'w') as file:
            file.write(text)

    def save_click_html(self):
        text = self.textEdit.toPlainText()
        print('html saved')
        with open('mypage.html', 'w') as myFile:
            myFile.write('<html> \n<body> \n')
            myFile.write('<br>' + text + '</br>')
            myFile.write('\n</body> \n</html>')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())