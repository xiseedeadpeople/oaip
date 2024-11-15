import flet as ft
import math

# TODO: добавить снизу 'by @xiseedeadpeople - github', ...

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK


class CalculatorApp(ft.Container):
    # application's root control (i.e. "view") containing all other controls
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=20)
        self.width = 450
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment="end"),

                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC", button_clicked=self.button_clicked),
                        ExtraActionButton(text="x²", button_clicked=self.button_clicked),
                        ExtraActionButton(text="√", button_clicked=self.button_clicked),
                        ExtraActionButton(text="+/-", button_clicked=self.button_clicked),
                        ActionButton(text="÷", button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text="sin", button_clicked=self.button_clicked),
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="×", button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text="cos", button_clicked=self.button_clicked),
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text="tg", button_clicked=self.button_clicked),
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text="ctg", button_clicked=self.button_clicked),
                        DigitButton(text="0", expand=2, button_clicked=self.button_clicked),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked)
                    ])
            ])

    def button_clicked(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ('+', '-', '×', '÷'):
            self.result.value = self.calculate(self.operand1, float(self.result.value), self.operator)
            self.operator = data

            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)

            self.new_operand = True

        # COMPLETED
        elif data in '√':
            if str(self.result.value)[0] == '-':
                self.result.value = 'Error'

            else:
                self.result.value = self.format_number(float(self.result.value) ** 0.5)
                self.reset()

        # COMPLETED
        elif data in 'x²':
            self.result.value = int(self.result.value) ** 2
            self.reset()

        # COMPLETED
        elif data in 'ctg':
            try:
                self.result.value = 1 / math.tan(int(self.result.value))
                self.reset()

            except RuntimeError:
                self.result.value = 'Error'

            except ZeroDivisionError:
                self.result.value = 'Error'

        # COMPLETED
        elif data in 'tg':
            self.result.value = math.tan(int(self.result.value))
            self.reset()

        # COMPLETED
        elif data in 'sin':
            self.result.value = math.sin(int(self.result.value))
            self.reset()

        # COMPLETED
        elif data in 'cos':
            self.result.value = math.cos(int(self.result.value))
            self.reset()

        # COMPLETED
        elif data in '+/-':
            if float(self.result.value) > 0:
                self.result.value = '-' + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(self.format_number(abs(float(self.result.value))))

        # COMPLETED
        elif data in '=':
            self.result.value = self.calculate(self.operand1, float(self.result.value), self.operator)
            self.reset()

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "×":
            return self.format_number(operand1 * operand2)

        elif operator == "÷":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


ft.app(target=main)


# exe: pyinstaller /  pyinstaller --noconsole --onefile filename.py / try cd name
# TODO: exceptions / turn into exe / 'RuntimeError: Event loop is closed' / . . .


# def main(page: Page):
#     page.title = "normal ahh calc"
#     page.theme_mode = ThemeMode.DARK
#     page.horizontal_alignment = page.vertical_alignment = 'center'
#     page.window.height, page.window.width = 400, 400
#
#     # page.window.on_event = page.window.close()
#     # page.window.resizable = False
#
#     # def app_exit(e):
#     #     page.window.close()
#
#     result = TextField(
#         hint_text='0', text_size=20,
#         color='white', text_align=TextAlign.RIGHT,
#         hint_style=TextStyle(
#             color=colors.WHITE, size=20
#         ),
#         read_only=True
#     )
#
#     def button_click(e):
#         if e.control.text == "=":
#             try:
#                 result.value = str(eval(result.value))
#
#             except Exception as e:
#                 result.value = f'Error: {e}'
#
#         elif e.control.text == "C":
#             result.value = ""
#
#         elif e.control.text == "√":
#             if result.value.startswith('-'):
#                 result.value = 'nah number must be positive'
#
#             else:
#                 result.value = f'{float(result.value) ** 0.5}'
#
#         # pass
#         else:
#             result.value += e.control.text
#         result.update()
#
#     def question_click(e):
#         dlg = AlertDialog(title=Text(f'github/xiseedeadpeople', size=20, color="pink600"), bgcolor=colors.BLACK)
#         page.open(dlg)
#
#     button_row0 = Row(
#         [
#             ElevatedButton(text='C', expand=1, on_click=button_click,
#                            bgcolor=colors.GREY, color=colors.BLACK),
#
#             ElevatedButton(text='%', expand=1, on_click=button_click,
#                            bgcolor=colors.GREY, color=colors.BLACK),
#
#             ElevatedButton(text='√', expand=1, on_click=button_click,
#                            bgcolor=colors.GREY, color=colors.BLACK),
#
#             ElevatedButton(text='/', expand=1, on_click=button_click,
#                            bgcolor=colors.ORANGE, color=colors.WHITE),
#         ]
#     )
#
#     button_row1 = Row(
#         [
#             ElevatedButton(text='7', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='8', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='9', expand=1, color=colors.WHITE, on_click=button_click),
#
#             ElevatedButton(text='*', expand=1, on_click=button_click,
#                            bgcolor=colors.ORANGE, color=colors.WHITE),
#         ]
#     )
#
#     button_row2 = Row(
#         [
#             ElevatedButton(text='4', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='5', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='6', expand=1, color=colors.WHITE, on_click=button_click),
#
#             ElevatedButton(text='-', expand=1, on_click=button_click,
#                            bgcolor=colors.ORANGE, color=colors.WHITE),
#         ]
#     )
#     button_row3 = Row(
#         [
#             ElevatedButton(text='1', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='2', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='3', expand=1, color=colors.WHITE, on_click=button_click),
#
#             ElevatedButton(text='+', expand=1, on_click=button_click,
#                            bgcolor=colors.ORANGE, color=colors.WHITE),
#         ]
#     )
#
#     button_row4 = Row(
#         [
#             ElevatedButton(text='?', expand=1,
#                            color=colors.WHITE24, bgcolor=colors.TRANSPARENT, on_click=question_click),
#
#             ElevatedButton(text='0', expand=1, color=colors.WHITE, on_click=button_click),
#             ElevatedButton(text='.', expand=1, color=colors.WHITE, on_click=button_click),
#
#             ElevatedButton(text='=', expand=1, on_click=button_click,
#                            bgcolor=colors.ORANGE, color=colors.WHITE)
#         ]
#     )
#
#     container = Container(
#         width=350, padding=20,
#         bgcolor=colors.BLACK, border_radius=border_radius.all(20),
#         content=Column([
#             result, button_row0, button_row1,
#             button_row2, button_row3, button_row4
#         ]))
#
#     page.add(container)


# if __name__ == '__main__':
#     app(target=main)
