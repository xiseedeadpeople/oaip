import pytest
import sqlite3

class TestUserDatabase:

    @pytest.fixture
    def setup_connection(self):
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE people (user_id INTEGER PRIMARY KEY, full_name TEXT, user_age INTEGER)''')
        connection.commit()
        yield connection
        connection.close()

    def test_insert_record(self, setup_connection):
        cursor = setup_connection.cursor()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Ваня', 33)")
        setup_connection.commit()
        cursor.execute("SELECT * FROM people WHERE full_name='Ваня'")
        result = cursor.fetchone()
        assert result is not None

    def test_update_record(self, setup_connection):
        cursor = setup_connection.cursor()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Дима', 24)")
        setup_connection.commit()
        cursor.execute("UPDATE people SET user_age=41 WHERE full_name='Дима'")
        setup_connection.commit()
        cursor.execute("SELECT user_age FROM people WHERE full_name='Дима'")
        result = cursor.fetchone()
        assert result[0] == 25

    def test_delete_record(self, setup_connection):
        cursor = setup_connection.cursor()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Дима', 24),"
                       "('Кирилл', 21), ('Андрей', 18)")
        setup_connection.commit()
        cursor.execute("DELETE FROM people WHERE full_name = 'Андрей'")
        setup_connection.commit()
        cursor.execute("SELECT * FROM people")
        result = cursor.fetchall()
        assert len(result) == 2

    def test_select_all_records(self, setup_connection):
        # Добавление нескольких записей и выборка всех записей из базы
        cursor = setup_connection.cursor()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Дима', 24)")
        setup_connection.commit()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Кирилл', 24)")
        setup_connection.commit()
        cursor.execute("INSERT INTO people (full_name, user_age) VALUES ('Дима', 24)")
        setup_connection.commit()
        cursor.execute("SELECT * FROM people")
        result = cursor.fetchall()
        assert len(result) == 3
