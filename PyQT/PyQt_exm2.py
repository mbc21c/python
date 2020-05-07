import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        btn1 = QPushButton('Insert', self)
        btn1.resize(btn1.sizeHint())
        btn1.setToolTip('안녕하세요.<b>안녕하세요.</b>')
        btn1.move(20, 30)

        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('첫번째 PyQT')

        self.show()

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_())
