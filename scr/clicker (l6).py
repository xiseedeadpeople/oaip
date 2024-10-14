from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 200)
        self.setMaximumSize(1200, 400)

        self.cbox1 = QComboBox()
        self.cbox1.addItems(['USD', 'RUB', 'EUR', 'NZD'])
        self.cbox1.setFixedSize(200, 50)

        self.cbox2 = QComboBox()
        self.cbox2.addItems(['RUB', 'USD', 'EUR', 'NZD'])
        self.cbox2.setFixedSize(200, 50)

        self.box_vals = self.cbox1.currentText(), self.cbox2.currentText()
        self.cbox1.currentIndexChanged.connect(lambda: self.change_similiars(self.cbox1.currentText()))

        layout = QVBoxLayout()
        layout.addWidget(self.cbox1)
        layout.addWidget(self.cbox2)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    def change_similiars(self, value):

        if self.cbox1.currentText() == self.cbox2.currentText():
            self.cbox1.setCurrentText(self.box_vals[0])
            self.cbox2.setCurrentText(self.box_vals[1])




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

