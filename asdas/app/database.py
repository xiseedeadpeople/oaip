import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS records (name TEXT, value TEXT)''')

    def add_record(self, record):
        self.cursor.execute('INSERT INTO records (name, value) VALUES (?, ?)', (record['name'], record['value']))
        self.conn.commit()

    def record_exists(self, record):
        self.cursor.execute('SELECT * FROM records WHERE name = ? AND value = ?', (record['name'], record['value']))
        return self.cursor.fetchone() is not None
