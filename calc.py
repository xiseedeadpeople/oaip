from flet import (
    app, Page, Container, Text, colors, border_radius, ElevatedButton, Row, Column)

from flet_core import ThemeMode


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

'''
C   √   S/C ÷
7   8   9   ×
4   5   6   -
1   2   3   +
?   0   .   =
'''


class CalcButton(ElevatedButton):
    def __init__(self, text, click_button, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = click_button
        self.data = text


class DigitButton(CalcButton):
    def __init__(self, text, click_button, expand=1):
        CalcButton.__init__(self, text, click_button, expand)
        self.bgcolor = colors.WHITE24
        self.color = colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, click_button):
        CalcButton.__init__(self, text, click_button)
        self.bgcolor = colors.ORANGE
        self.color = colors.WHITE


class ExtraActionButton(CalcButton):
    def __init__(self, text, click_button):
        CalcButton.__init__(self, text, click_button)
        self.bgcolor = colors.BLUE_GREY_100
        self.color = colors.BLACK


class CalcuApp(Container):
    def __init__(self):
        super().__init__()
        self.input_await = True
        self.operator = "+"
        self.operand1 = 0
        self.box = Text(value="0", color=colors.WHITE, size=20)  # box - input field

        self.width = 350
        self.bgcolor = colors.BLACK
        self.border_radius = border_radius.all(20)
        self.padding = 20

        self.result = Text(value="0", color=colors.WHITE, size=20)
        self.width = 350
        self.bgcolor = colors.BLACK
        self.border_radius = border_radius.all(20)
        self.padding = 20
        self.content = Column(
            controls=[
                Row(controls=[self.result]),

                Row(controls=[
                    ExtraActionButton(text="AC", click_button=self.click_button),
                    ExtraActionButton(text="+/-", click_button=self.click_button),
                    ExtraActionButton(text="%", click_button=self.click_button),
                    ActionButton(text="/", click_button=self.click_button)]),

                Row(controls=[
                    DigitButton(text="7", click_button=self.click_button),
                    DigitButton(text="8", click_button=self.click_button),
                    DigitButton(text="9", click_button=self.click_button),
                    ActionButton(text="*", click_button=self.click_button)]),

                Row(controls=[
                    DigitButton(text="4", click_button=self.click_button),
                    DigitButton(text="5", click_button=self.click_button),
                    DigitButton(text="6", click_button=self.click_button),
                    ActionButton(text="-", click_button=self.click_button)]),

                Row(controls=[
                    DigitButton(text="1", click_button=self.click_button),
                    DigitButton(text="2", click_button=self.click_button),
                    DigitButton(text="3", click_button=self.click_button),
                    ActionButton(text="+", click_button=self.click_button),
                    ]),

                Row(controls=[
                    DigitButton(text="0", expand=2, click_button=self.click_button),
                    DigitButton(text=".", click_button=self.click_button),
                    ActionButton(text="=", click_button=self.click_button)])
            ]
        )

    def click_button(self, e):
        current_button = e.control.data   # currently pressed button

        if self.box.value == 'Error' or current_button == 'C':  # if Error or C in box ??
            self.box.value = '0'
            self.reset()

        elif current_button in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            if self.box.value == '0' or self.input_await is True:
                self.box.value = current_button
                self.input_await = False

            else:
                # self.box.value = self.box.value + current_button
                self.box.value = 'CHECK LINE 164!'

        elif current_button in ('+', '-', '*', '/'):
            self.box.value = (self.calculate(self.operand1, float(self.box.value), self.operator))
            self.operator = current_button

            if self.box.value == 'Error':
                self.operand1 = '0'
            else:
                self.operand1 = float(self.box.value)
            self.input_await = True

        elif current_button in '=':
            self.box.value = (self.calculate(self.operand1, float(self.box.value), self.operator))
            self.reset()

        elif current_button in "%":
            self.box.value = float(self.box.value) / 100
            self.reset()

        elif current_button in "...":
            pass

        self.update()

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.input_await = True

    def calculate(self, operand1, o2, operator):
        pass

    def format_number(self, num):
        """formatting output, example: '1.0' -> '1'"""
        if num % 1 == 0:
            return int(num)
        else:
            return num
