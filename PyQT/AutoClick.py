import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QTextEdit

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        s_btn = QPushButton('시작', self)
        s_btn.move(500, 100)
        s_btn.setGeometry(70,70,70,70)
        
        self.setWindowTitle('AutoClick')

        self.show()

app = QApplication(sys.argv)
w = UI()
sys.exit(app.exec_())
