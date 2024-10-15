from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('clicker')
        self.setMinimumSize(300, 100)
        self.setMaximumSize(600, 200)

        self.button = QPushButton('1')
        self.button.clicked.connect(self.on_click)
        self.setCentralWidget(self.button)

    def on_click(self):
        self.button.setText(f'{int(self.button.text()) + 1}')
        self.setWindowTitle('clicker!')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
