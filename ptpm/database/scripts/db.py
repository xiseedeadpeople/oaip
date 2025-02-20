import sqlite3


class Data:
    _instance = None

    def __new__(cls, filename):
        if cls._instance is None:
            cls._instance = super(Data, cls).__new__(cls)
            cls.data = []
            cls._instance.filename = filename
            cls.connect()
        return cls._instance

    @staticmethod
    def connect():
        Data._instance.db = sqlite3.connect(Data._instance.filename)
        Data._instance.cur = Data._instance.db.cursor()

    def get_all_orders(self, column, fltr):
        try:
            if column is not None:
                request = f"SELECT * FROM orders_with_filter WHERE {column} like ?"
                self.data = self.cur.execute(request, (f'%{fltr}%',)).fetchall()
            else:
                request = f"SELECT * FROM orders_with_filter"
                self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e

    def add_order(self, **kwargs):
        try:
            sqlite_insert_query = """
                INSERT INTO Orders (type_of_work, description, acceptance_date, customer, executor, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            data = (kwargs['type_of_work'], kwargs['description'], kwargs['acceptance_date'],
                    kwargs['customer'], kwargs['executor'], kwargs['status'])
            self.cur.execute(sqlite_insert_query, data)
            self.db.commit()
            return "Запись добавлена"
        except sqlite3.Error as e:
            return f"Ошибка добавления: {e}"

    def update_order(self, **kwargs):
        try:
            sqlite_update_query = """ UPDATE Orders
                SET type_of_work = ?, description = ?, acceptance_date = ?, 
                    customer = ?, executor = ?, status = ? WHERE id_order = ?"""
            data = (kwargs['type_of_work'], kwargs['description'], kwargs['acceptance_date'],
                    kwargs['customer'], kwargs['executor'], kwargs['status'], kwargs['id_order'])
            self.cur.execute(sqlite_update_query, data)
            self.db.commit()
            return "Запись обновлена"
        except sqlite3.Error as e:
            return f"Ошибка обновления: {e}"

    def delete_order(self, **kwargs):
        try:
            sqlite_delete_query = "DELETE FROM Orders WHERE id_order = ?"
            data = (kwargs['id_order'],)
            self.cur.execute(sqlite_delete_query, data)
            self.db.commit()
            return "Запись удалена"
        except sqlite3.Error as e:
            return f"Ошибка удаления: {e}"

    def get_work_types(self):
        try:
            request = "SELECT id_work, work FROM Works"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e

    def get_executors(self):
        try:
            request = "SELECT id_employee, surname FROM Employees"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e

    def get_statuses(self):
        try:
            request = "SELECT id_status, status FROM Statuses"
            self.data = self.cur.execute(request).fetchall()
        except sqlite3.Error as e:
            self.data = e
