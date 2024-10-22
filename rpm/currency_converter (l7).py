from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from bs4 import BeautifulSoup  # pip install requests lxml bs4
import requests, sys


url = 'https://www.cbr.ru/currency_base/daily/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'lxml')
nouns = soup.findAll('tr')[1:]

#  сurrncy
d = {'RUB': 1.0}
for i in nouns:
    each_column = i.text.split()
    currency = each_column[1]  # валюта
    course = float(each_column[-1].replace(',', '.'))

    if each_column[2] != '1':  # есил курс валюты > чем к 1 руб /(напр. 1 валюта к 100руб)
        course /= float(each_column[2])

    d[currency] = course



class MainWindow(QMainWindow):
    """ можно еще добавть обозначения валют (¥€$), их названия + UI """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('damm')
        self.setFixedSize(400, 130)


        self.cbox1 = QComboBox()
        self.cbox1.addItems(sorted(d.keys()))
        self.cbox1.setCurrentText('USD')
        self.cbox1.setFixedSize(190, 20)

        self.cbox2 = QComboBox()
        self.cbox2.addItems(sorted(d.keys()))
        self.cbox2.setCurrentText('RUB')
        self.cbox2.setFixedSize(190, 20)

        self.button = QPushButton('↑↓')
        self.button.setFixedSize(190, 20)
        self.button.clicked.connect(self.swap_currencies)

        self.top_field = QLineEdit()
        self.top_field.setFixedSize(190, 20)
        self.top_field.setText(f'{d["RUB"]}')

        self.bottom_field = QLineEdit()
        self.bottom_field.setFixedSize(190, 20)


        self.top_field.textChanged.connect(self.convert_currency_from_top_field)
        self.bottom_field.textChanged.connect(self.convert_currency_from_bottom_field)

        self.cbox1.currentIndexChanged.connect(self.update_conversion)
        self.cbox2.currentIndexChanged.connect(self.update_conversion)


        layout = QGridLayout()
        layout.addWidget(self.cbox1, 0, 0)
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.cbox2, 2, 0)

        layout.addWidget(self.top_field, 0, 2)
        layout.addWidget(self.bottom_field, 2, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.update_conversion()

    def update_conversion(self):
        self.convert_currency_from_top_field()
        self.convert_currency_from_bottom_field()

    def convert_currency_from_top_field(self):
        try:
            amount = float(self.top_field.text())
            from_currency = self.cbox1.currentText()
            to_currency = self.cbox2.currentText()

            converted_amount = amount * d[from_currency] / d[to_currency]
            self.bottom_field.blockSignals(True)
            self.bottom_field.setText(f'{converted_amount:.2f}')
            self.bottom_field.blockSignals(False)

        except ValueError:
            self.bottom_field.setText('')

    def convert_currency_from_bottom_field(self):
        try:
            amount = float(self.bottom_field.text())
            from_currency = self.cbox2.currentText()
            to_currency = self.cbox1.currentText()

            # Пересчитываем сумму в первую валюту
            converted_amount = amount * d[from_currency] / d[to_currency]
            self.top_field.blockSignals(True)
            self.top_field.setText(f'{converted_amount:.2f}')
            self.top_field.blockSignals(False)

        except ValueError:
            self.top_field.setText('')

    def swap_currencies(self):
        """
        кароч можно поменять в from-, to- currency '..cbox1..' и '..cbox2..' местами,
        в таком случае сами валюты перестанут меняться местами, но они будут
        не совсем верно конвертироваться: напр. сверху - 100₽, снизу - 1$, при нажатии
        получится так, что снизу - 100$, а сверху - 10000₽, и так далее
        /
        по хорошему, надо изменит ь так, чтобы прыгало только верхнее число.
        """
        from_currency = self.cbox1.currentText()  #
        to_currency = self.cbox2.currentText()  #
        amount = float(self.top_field.text())
        converted_amount = amount * d[from_currency] / d[to_currency]

        self.cbox1.setCurrentText(to_currency)
        self.cbox2.setCurrentText(from_currency)

        self.top_field.setText(f'{converted_amount:.2f}')
        self.update_conversion()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
