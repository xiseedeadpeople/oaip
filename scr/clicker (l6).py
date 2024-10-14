from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('clicker')

        self.button = QPushButton('1')
        self.button.clicked.connect(self.on_click)
        self.setCentralWidget(self.button)

    def on_click(self):
        self.button.setText(f'{int(self.button.text()) + 1}')
        self.setWindowTitle('clicker, worked')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
