from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, \
    QMessageBox, QLineEdit, QHBoxLayout, QComboBox
from app.addDataWin import AddDataWin
from database.scripts.db import Data


class ViewDataWin(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Data("database/service_center.db")
        self.initUI()
        self.load_data()
        self.show()

    def initUI(self):
        self.setWindowTitle("Выборки из базы данных")
        self.setGeometry(100, 100, 1500, 500)
        self.query_label = QLabel("Выберите выборку:")
        self.query_combo = QComboBox()
        self.query_combo.addItem("Все заказы", "all_orders")
        self.query_combo.addItem("Статус заказа", "status")
        self.query_combo.addItem("Исполнитель", "surname")
        self.query_combo.addItem("Вид работы", "work")
        self.query_combo.addItem("Дата", "acceptance_date")
        self.filter = QLineEdit()
        self.filter.setPlaceholderText('Введите фильтр')
        self.table = QTableWidget()
        self.back_button = QPushButton("Назад")
        self.del_entry = QPushButton("Удалить")
        self.edit_entry = QPushButton("Изменить")
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        main_l.addWidget(self.query_label)
        main_l.addWidget(self.query_combo)
        main_l.addWidget(self.filter)
        main_l.addWidget(self.table)
        h_l1.addWidget(self.del_entry)
        h_l1.addWidget(self.edit_entry)
        h_l1.addWidget(self.back_button)
        main_l.addLayout(h_l1)
        self.setLayout(main_l)
        self.filter.textChanged.connect(self.load_data)
        self.query_combo.currentIndexChanged.connect(self.load_data)
        self.back_button.clicked.connect(self.go_back)
        self.del_entry.clicked.connect(self.delite_order)
        self.edit_entry.clicked.connect(self.edit_orders)

    def load_data(self):
        query_type = self.query_combo.currentData()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)
        if query_type == "all_orders":
            self.load_orders()
        elif query_type == "status":
            self.load_orders('status')
        elif query_type == "surname":
            self.load_orders('surname')
        elif query_type == "work":
            self.load_orders('work')
        elif query_type == "acceptance_date":
            self.load_orders('acceptance_date')

    def load_orders(self, column=None):
        self.db.get_all_orders(column, self.filter.text().capitalize())
        if type(self.db.data) is list:
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(
                ['ID заказа', 'Тип работы', 'Описание', 'Дата принятия', 'Клиент', 'Исполнитель', 'Статус'])
            self.table.setRowCount(len(self.db.data))
            for row_idx, row_data in enumerate(self.db.data):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        else:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные: {self.db.data}")

    def delite_order(self):
        if self.table.selectedItems():
            confirmation_dialog = QMessageBox()
            confirmation_dialog.setWindowTitle("Подтверждение удаления")
            confirmation_dialog.setText(f"Вы уверены, что хотите удалить запись:"
                                        f"\n{self.table.item(self.table.currentRow(), 2).text()}?")
            confirmation_dialog.setIcon(QMessageBox.Icon.Warning)
            confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirmation_dialog.setDefaultButton(QMessageBox.StandardButton.No)
            user_response = confirmation_dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                QMessageBox.information(self, "Инфо", self.db.delete_order(id_order=self.table.item(
                    self.table.currentRow(), 0).text()))
                self.load_data()

    def edit_orders(self):
        self.win_a = AddDataWin([self.table.item(self.table.selectedItems()[0].row(), col).text() for col in range(self.table.columnCount())])
        self.win_a.destroyed.connect(self.load_data)
        self.win_a.show()

    def go_back(self):
        self.close()
