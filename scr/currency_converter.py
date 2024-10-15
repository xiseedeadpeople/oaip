from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from bs4 import BeautifulSoup  # pip install requests lxml bs4
import requests
import sys


url = 'https://www.cbr.ru/currency_base/daily/'

responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
nouns = soup.findAll('tr')

allc = [[i.text] for i in nouns][1::]
valutes, amount, currency = ['RUB'], [], []

# too gross cycle
for i in allc:
    res = []

    for x in i:
        res.append(x.split())

    for el in res:
        valutes.append(res[0][1])
        amount.append(res[0][2])
        currency.append(res[0][-1])

valutes.sort()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 200)
        self.setMaximumSize(1200, 400)

        # # # # #

        self.cbox1 = QComboBox()
        self.cbox1.addItems(valutes)
        self.cbox1.setCurrentText('RUB')
        self.cbox1.setFixedSize(200, 50)

        self.cbox2 = QComboBox()
        self.cbox2.addItems(valutes)
        self.cbox2.setCurrentText('USD')
        self.cbox2.setFixedSize(200, 50)

        # # # # #

        self.button = QPushButton('1')
        self.button.setFixedSize(20, 20)

        # widget.setSuffix("c") 'asd' -> 'asd$'

        self.box_vals = self.cbox1.currentText(), self.cbox2.currentText()

        # # # # #

        layout = QVBoxLayout()
        layout.addWidget(self.cbox1)
        layout.addWidget(self.cbox2)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # # # # #


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
