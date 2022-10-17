# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myinterfacexacLls.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import random

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
        MainWindow.resize(293, 427)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 210, 221, 61))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 330, 221, 51))
        self.pushButton_2.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 50, 231, 51))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.lineEdit.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 211, 41))
        self.label_2.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 270, 221, 61))
        self.pushButton_3.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 0, 231, 41))
        self.label_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 293, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_2.clicked.connect(self.exitFunc)
        self.pushButton.clicked.connect(self.click_rand)
        self.pushButton_3.clicked.connect(self.inpWord)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0430\u043d\u0434\u043e\u043c\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.label_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423 \u0442\u0435\u0431\u044f \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c 4 \u043f\u043e\u043f\u044b\u0442\u043a\u0438", None))
    # retranslateUi

    def exitFunc(self):
        exit(0)




    def inpWord(self):

        global rus, eng, k
        var = self.lineEdit.text()
        if self.label_3.update != "":
            if var.isalpha():
                if k != 0:
                    if var == dictionary[rus]:
                        self.label_2.setText("Ответ правильный!")
                        k = 3
                    else:
                        self.label_3.setText("У тебя есть " + str(k) + " попытки:")
                        self.label_2.setText("Ответ неправильный!")
                        k -= 1
                else:
                    self.label_3.setText("Попыток не осталось!")

            else:
                self.label_3.setText("Ошибка ввода! Введите заново!")
        else:
            self.label_3.setText("Вы не зарандомили!")

    def click_rand(self):
        global rus, eng
        rus, eng = random.choice(list(dictionary.items()))
        self.label_2.setText(rus)
        self.label_3.setText('У вас осталось 4 попытки')

dictionary = {"яблоко": "apple",
              "абрикос": "apricot",
              "апельсин": "orange",
              "груша": "pear",
              "лайм": "lime",
              "мандарин": "tangerine",
              "персик": "peach",
              "дыня": "melon",
              "лимон": "lemon",
              "папайя": "papaya",
              }
k = 4
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
