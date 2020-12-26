import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from random import randint
import math
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.h = randint(1, 500)
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(250 - self.h // 2, 250 - self.h // 2, self.h, self.h)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
