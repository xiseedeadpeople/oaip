# Базовый класс Widget (Виджет)
class Widget:
    def __init__(self, name):
        self.name = name

    def draw(self):
        raise NotImplementedError("Subclasses should implement this method")


# Класс Label (Метка)
class Label(Widget):
    def __init__(self, name, text):
        super().__init__(name)
        self.text = text

    def draw(self):
        return f"Label '{self.name}': {self.text}"


# Класс LineEdit (Однострочное поле ввода)
class LineEdit(Widget):
    def __init__(self, name):
        super().__init__(name)
        self.text = ""

    def draw(self):
        return f"LineEdit '{self.name}': {self.text}"

    def set_text(self, text):
        self.text = text


# Класс TextEdit (Многострочное поле ввода)
class TextEdit(Widget):
    def __init__(self, name):
        super().__init__(name)
        self.text = ""

    def draw(self):
        return f"TextEdit '{self.name}': {self.text}"

    def set_text(self, text):
        self.text = text


# Класс Button (Кнопка)
class Button(Widget):
    def __init__(self, name, action):
        super().__init__(name)
        self.action = action

    def draw(self):
        return f"Button '{self.name}': Click to {self.action}"


# Класс CheckBox (Флажок)
class CheckBox(Widget):
    def __init__(self, name, checked=False):
        super().__init__(name)
        self.checked = checked

    def draw(self):
        return f"CheckBox '{self.name}': {'Checked' if self.checked else 'Unchecked'}"

    def toggle(self):
        self.checked = not self.checked


# Пример использования
if __name__ == "__main__":
    # Создание различных виджетов
    label = Label("TitleLabel", "Welcome to My App")
    line_edit = LineEdit("UsernameField")
    text_edit = TextEdit("DescriptionField")
    button = Button("SubmitButton", "Submit Form")
    checkbox = CheckBox("AgreeCheckBox")

    # Изменение содержимого виджетов
    line_edit.set_text("User123")
    text_edit.set_text("This is a multiline text\nwith multiple lines.")

    # Вывод информации о каждом виджете
    print(label.draw())
    print(line_edit.draw())
    print(text_edit.draw())
    print(button.draw())
    print(checkbox.draw())

    # Имитация клика по кнопке и переключение флажка
    button.action = "Save Changes"
    checkbox.toggle()

    print(button.draw())
    print(checkbox.draw())
