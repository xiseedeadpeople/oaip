# from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QGridLayout, QPushButton
# import sys
#
#
# # self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>
#
#
# class TextEditDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         try:
#             self.setWindowTitle("QTextEdit")
#             self.setFixedSize(500, 300)
#
#             # TextEditWindow
#             self.textEdit = QTextEdit()
#             self.textEdit.setFixedSize(200, 100)
#
#             # Buttons
#             self.btnPress1 = QPushButton("Button 1")
#             self.btnPress1.setFixedSize(100, 50)
#
#             self.btnPress2 = QPushButton("Button 2")
#             self.btnPress1.setFixedSize(100, 50)
#
#             self.btnPress3 = QPushButton("Button 3")
#             self.btnPress1.setFixedSize(100, 50)
#
#             # pass
#             layout = QGridLayout()
#             layout.addWidget(self.textEdit, 1, 1)
#             layout.addWidget(self.btnPress1, 0, 0)
#             layout.addWidget(self.btnPress2, 1, 0)
#             layout.addWidget(self.btnPress3, 2, 0)
#             self.setLayout(layout)
#
#             self.btnPress1.clicked.connect(self.btnPress1_Clicked)
#             self.btnPress2.clicked.connect(self.btnPress2_Clicked)
#             self.btnPress3.clicked.connect(self.btnPress3_Clicked)
#
#         except Exception as e:
#             print(f'Error: {e}!')
#
#     def btnPress1_Clicked(self):
#         try:
#             self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")
#
#         except Exception as e:
#             print(f'Error: {e}!')
#
#     def btnPress2_Clicked(self):
#         try:
#             self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")
#
#         except Exception as e:
#             print(f'Error: {e}!')
#
#     def btnPress3_Clicked(self):
#         try:
#             self.textEdit.setPlainText("asasds")
#
#         except Exception as e:
#             print(f'Error: {e}!')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = TextEditDemo()
#     win.show()
#     sys.exit(app.exec())

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QColor,
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
