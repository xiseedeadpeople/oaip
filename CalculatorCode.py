import flet as ft
import math
import time

# exe: pyinstaller /  pyinstaller --noconsole --onefile filename.py / try cd name

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
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value='0', color=ft.colors.WHITE, size=20)
        self.width = 450
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 20

        # noinspection PyTypeChecker
        self.content = ft.Column(
            controls=[
                ft.Row(controls=[self.result], alignment='end'),

                ft.Row(
                    controls=[
                        ExtraActionButton(text='C', button_clicked=self.button_clicked),
                        ExtraActionButton(text='x²', button_clicked=self.button_clicked),
                        ExtraActionButton(text='√', button_clicked=self.button_clicked),
                        ExtraActionButton(text='+/-', button_clicked=self.button_clicked),
                        ActionButton(text='÷', button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text='sin', button_clicked=self.button_clicked),
                        DigitButton(text='7', button_clicked=self.button_clicked),
                        DigitButton(text='8', button_clicked=self.button_clicked),
                        DigitButton(text='9', button_clicked=self.button_clicked),
                        ActionButton(text='×', button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text='cos', button_clicked=self.button_clicked),
                        DigitButton(text='4', button_clicked=self.button_clicked),
                        DigitButton(text='5', button_clicked=self.button_clicked),
                        DigitButton(text='6', button_clicked=self.button_clicked),
                        ActionButton(text='-', button_clicked=self.button_clicked),
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text='?', button_clicked=self.button_clicked),
                        DigitButton(text='1', button_clicked=self.button_clicked),
                        DigitButton(text='2', button_clicked=self.button_clicked),
                        DigitButton(text='3', button_clicked=self.button_clicked),
                        ActionButton(text='+', button_clicked=self.button_clicked)
                    ]),

                ft.Row(
                    controls=[
                        DigitButton(text='0', expand=3, button_clicked=self.button_clicked),
                        DigitButton(text='.', button_clicked=self.button_clicked),
                        ActionButton(text='=', button_clicked=self.button_clicked)
                    ])
            ])

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == 'Error' or data == 'C':
            self.result.value = '0'
            self.reset()

        elif data in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            if self.result.value == '0' or self.new_operand == True or str(self.result.value).startswith('code'):
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        if str(self.result.value).startswith('code'):
            self.result.value = '0'
            self.reset()
        else:
            if data in ('+', '-', '×', '÷'):
                self.result.value = self.calculate(self.operand1, float(self.result.value), self.operator)
                self.operator = data

                if self.result.value == 'Error':
                    self.operand1 = '0'

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
                self.result.value = self.format_number(float(self.result.value) ** 2)
                self.reset()

            # COMPLETED
            elif data in 'sin':
                self.result.value = self.format_number(math.sin(float(self.result.value)))
                self.reset()

            # COMPLETED
            elif data in 'cos':
                self.result.value = self.format_number(math.cos(float(self.result.value)))
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

            elif data in '?':
                self.result.value = f'code: github/xiseedeadpeople'

        self.update()


    @staticmethod
    def format_number(num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == '+':
            return self.format_number(operand1 + operand2)

        elif operator == '-':
            return self.format_number(operand1 - operand2)

        elif operator == '×':
            return self.format_number(operand1 * operand2)

        elif operator == '÷':
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = '+'
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    # page.window.frameless = True
    page.title = 'ahh'
    page.bgcolor = ft.colors.BLACK
    page.window.width = 475
    page.window.height = 325
    page.window.resizable = False

    calc = CalculatorApp()
    page.add(calc)
    dlg = ft.AlertDialog(
        title=ft.Text(f'3СПИ - Кайков',
        color="#FFFFFF"),
        modal=True,
        bgcolor=ft.colors.TRANSPARENT)

    page.open(dlg)
    time.sleep(1.5)
    page.close(dlg)
    page.update()


ft.app(target=main)
