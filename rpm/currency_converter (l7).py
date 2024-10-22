from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton
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

d = {}
for i in allc:
    res = []

    for x in i:
        res.append(x.split())

    for el in res:
        curr = float(res[0][-1].replace(',', '.'))

        if res[0][2] != '1':  # курс валюты > чем к 1 руб /(напр. к 1000)
            curr /= float(res[0][2])

        #

        valutes.append(res[0][1])
        # amount.append(res[0][2])
        currency.append(curr)

        d[res[0][1]] = curr

valutes.sort()

print(d)

# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(400, 130)
#
#         # # # # #
#
#         self.cbox1 = QComboBox()
#         self.cbox1.addItems(valutes) # d.keys()
#         self.cbox1.setCurrentText('RUB')
#         self.cbox1.setFixedSize(190, 20)
#
#         self.cbox2 = QComboBox()
#         self.cbox2.addItems(valutes)  # d.keys()
#         self.cbox2.setCurrentText('USD')
#         self.cbox2.setFixedSize(190, 20)
#
#         self.button = QPushButton('↑↓')
#
#         self.input1 = QLineEdit()
#         self.input1.setFixedSize(190, 20)
#         # self.input1.textChanged.connect()
#
#         self.input2 = QLineEdit()
#         self.input2.setFixedSize(190, 20)
#
#         # widget.setSuffix("c") 'asd' -> 'asd$'
#
#         self.box_vals = self.cbox1.currentText(), self.cbox2.currentText()
#
#         # # # # #
#
#         layout = QGridLayout()
#         layout.addWidget(self.cbox1, 0, 0)
#         # layout.addWidget(self.button, 1, 0)
#         layout.addWidget(self.cbox2, 2, 0)
#
#         layout.addWidget(self.input1, 0, 2)
#         layout.addWidget(self.input2, 2, 2)
#
#         #
#
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#
#         # # # # #
#     def idk(self, x):
#         pass
#
#
# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# app.exec()
