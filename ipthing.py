from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from bs4 import BeautifulSoup  # pip install requests lxml bs4
import requests
import sys


# https://ip-api.com/#xxx.xx.xx.x 213.87.96.9

# url = 'https://ip-api.com/'

# responce = requests.get(url).text
# soup = BeautifulSoup(responce, 'lxml')
# nouns = soup.findAll('span')
# print(nouns)
# # allc = [[i.text] for i in nouns][1::]
