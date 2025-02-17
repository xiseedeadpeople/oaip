from behave import given, when, then
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QListView, QLabel
from app.database import Database

@given('I have opened the application')
def step_impl(context):
    context.app = QApplication([])
    context.main_window = QMainWindow()
    context.main_window.show()

@given('I have records in the database')
def step_impl(context):
    context.db = Database()
    context.db.add_record({"name": "Test", "value": "Data"})

@when('I enter valid data into the form')
def step_impl(context):
    context.main_window.findChild(QPushButton, "AddButton").click()

@when('I enter invalid data into the form')
def step_impl(context):
    context.main_window.findChild(QPushButton, "AddButton").click()

@then('the new record should be added to the database')
def step_impl(context):
    assert context.db.record_exists({"name": "Test", "value": "Data"})

@then('I should see all the records listed')
def step_impl(context):
    records = context.main_window.findChild(QListView, "RecordsList").model()
    assert len(records) > 0

@then('I should see an error message')
def step_impl(context):
    error_message = context.main_window.findChild(QLabel, "ErrorMessage").text()
    assert "Invalid data" in error_message
