class Button:
    def __init__(self, label, action):
        self.label = label  # текст на кнопке
        self.action = action  # действие, которое выполняется при нажатии

    def click(self):
        """Нажатие на кнопку."""
        print(f"Выполняется действие: {self.action}")

    def change_label(self, new_label):
        """Изменение текста на кнопке."""
        self.label = new_label
        print(f"Текст кнопки изменен на: {self.label}")

    def disable(self):
        """Отключение кнопки."""
        print("Кнопка отключена.")

    def enable(self):
        """Включение кнопки."""
        print("Кнопка включена.")
