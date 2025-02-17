from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test App")
        self.setGeometry(100, 100, 800, 600)

        self.add_button = QPushButton("Add", self)
        self.add_button.setObjectName("AddButton")
        self.add_button.clicked.connect(self.add_record)

    def add_record(self):
        print("Record added")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
