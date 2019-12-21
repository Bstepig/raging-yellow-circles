# !/usr/bin/python3

# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import random


class Main(QMainWindow):
    circles = []

    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
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
            qp.setPen(QColor('yellow'))
            qp.drawEllipse(*i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
