# !/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.A = QtWidgets.QPushButton(self.centralwidget)
        self.A.setGeometry(QtCore.QRect(140, 130, 75, 23))
        self.A.setObjectName("A")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 361, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.A.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.A.setText(_translate("MainWindow", "Пуск"))


class Main(QMainWindow, Ui_MainWindow):
    circles = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("""
        QMainWindow {
        background: #fff;
        }
        """)
        self.A.clicked.connect(self.generate_circles)
        self.show()

    def paintEvent(self, event):
        qp = QPainter(self.frame)
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def generate_circles(self):
        count = 10
        self.circles = []
        for i in range(count):
            diameter = random.randint(5, 50)
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            self.circles.append((x, y, diameter, diameter))
        self.update()

    def draw(self, qp):
        for i in self.circles:
            qp.setPen(QColor(f'#{str(hex(random.randint(0, 255 ** 3)))[2:]}'))
            qp.drawEllipse(*i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
