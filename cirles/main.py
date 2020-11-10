import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.test = None

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.test = True
        self.update()

    def paintEvent(self, event):
        if self.test:
            qp = QPainter()
            qp.begin(self)
            self.draw_cirlce(qp)
    
    def draw_cirlce(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.radius = randint(0, self.height())
        self.x, self.y = randint(0, self.width()), randint(0, self.height())
        qp.drawEllipse(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.test = None


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())