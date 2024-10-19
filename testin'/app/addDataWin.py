from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QLineEdit, QTextEdit, QMessageBox, QLabel
from database.scripts.db import Data
from PyQt6.QtGui import QIcon


class AddDataWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.db = Data("database/service_center.db")
        self.data = data
        self.initUI()
        if data:
            self.upload_editable_data()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/computer.ico'))
        self.setWindowTitle("Добавить новый заказ")
        self.setGeometry(100, 100, 400, 700)
        self.work_label = QLabel("Тип работы:")
        self.work_input = QComboBox()
        self.load_work_types()
        self.description_label = QLabel("Описание работы:")
        self.description_input = QTextEdit()
        self.acceptance_date_label = QLabel("Дата принятия (YYYY-MM-DD):")
        self.acceptance_date_input = QLineEdit()
        self.customer_label = QLabel("Клиент:")
        self.customer_input = QLineEdit()
        self.executor_label = QLabel("Исполнитель:")
        self.executor_input = QComboBox()
        self.load_executors()
        self.status_label = QLabel("Статус:")
        self.status_input = QComboBox()
        self.load_statuses()
        self.add_button = QPushButton("Добавить заказ")
        layout = QVBoxLayout()
        layout.addWidget(self.work_label)
        layout.addWidget(self.work_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.acceptance_date_label)
        layout.addWidget(self.acceptance_date_input)
        layout.addWidget(self.customer_label)
        layout.addWidget(self.customer_input)
        layout.addWidget(self.executor_label)
        layout.addWidget(self.executor_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)
        layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_order)


        self.setLayout(layout)

    def upload_editable_data(self):
        self.work_input.setCurrentText(self.data[1])
        self.description_input.setText(self.data[2])
        self.acceptance_date_input.setText(self.data[4])
        self.customer_input.setText(self.data[3])
        self.executor_input.setCurrentText(self.data[-2])
        self.status_input.setCurrentText(self.data[-1])

    def load_work_types(self):
        self.work_input.clear()
        self.db.get_work_types()
        for id_work, work in self.db.data:
            self.work_input.addItem(work, id_work)

    def load_executors(self):
        self.executor_input.clear()
        self.db.get_executors()
        for id_employee, employee in self.db.data:
            self.executor_input.addItem(employee, id_employee)

    def load_statuses(self):
        self.status_input.clear()
        self.db.get_statuses()
        for id_status, status in self.db.data:
            self.status_input.addItem(status, id_status)

    def add_order(self):
        type_of_work = self.work_input.currentData()
        description = self.description_input.toPlainText()
        customer = self.customer_input.text()
        acceptance_date = self.acceptance_date_input.text()
        executor = self.executor_input.currentData()
        status = self.status_input.currentData()
        if self.data:
            id_order = self.data[0]
            answer = self.db.update_order(type_of_work=type_of_work, description=description,
                                          acceptance_date=acceptance_date, customer=customer,
                                          executor=executor, status=status, id_order=id_order)
        else:
            answer = self.db.add_order(type_of_work=type_of_work, description=description,
                                       acceptance_date=acceptance_date, customer=customer,
                                       executor=executor, status=status)
        QMessageBox.information(self, "Инфо", answer)
        self.close()
