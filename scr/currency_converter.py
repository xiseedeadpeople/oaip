from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 200)
        self.setMaximumSize(1200, 400)

        combobox1 = QComboBox()
        combobox1.addItems(['USD', 'RUB', 'EUR', 'NZD'])
        combobox1.setFixedSize(200, 50)

        combobox2 = QComboBox()
        combobox2.addItems(['RUB', 'USD', 'EUR', 'NZD'])
        combobox2.setFixedSize(200, 50)

        layout = QVBoxLayout()
        layout.addWidget(combobox1)
        layout.addWidget(combobox2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
