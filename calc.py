from flet import (
    app, Page, Container, Column, Row, AlertDialog, Text,
    TextField, colors, border_radius, ElevatedButton, TextAlign, TextStyle
)
from flet_core import ThemeMode
# exe: pyinstaller /  pyinstaller --noconsole --onefile filename.py / try cd name


def main(page: Page):
    page.title = "normal ahh calc"
    page.theme_mode = ThemeMode.DARK
    page.horizontal_alignment = page.vertical_alignment = 'center'
    page.window.height, page.window.width = 400, 400

    # page.window.on_event = page.window.close()
    # page.window.resizable = False

    # def app_exit(e):
    #     page.window.close()

    result = TextField(
        hint_text='0', text_size=20,
        color='white', text_align=TextAlign.RIGHT,
        hint_style=TextStyle(
            color=colors.WHITE, size=20
        ),
        read_only=True
    )

    def button_click(e):
        if e.control.text == "=":
            try:
                result.value = str(eval(result.value))

            except Exception as e:
                result.value = f'Error: {e}'

        elif e.control.text == "C":
            result.value = ""

        elif e.control.text == "√":
            if result.value.startswith('-'):
                result.value = 'nah number must be positive'

            else:
                result.value = f'{float(result.value)**0.5}'

        # pass
        else:
            result.value += e.control.text
        result.update()

    def question_click(e):
        dlg = AlertDialog(title=Text(f'github/xiseedeadpeople', size=20, color="pink600"), bgcolor=colors.BLACK)
        page.open(dlg)

    button_row0 = Row(
        [
            ElevatedButton(text='C', expand=1, on_click=button_click,
                           bgcolor=colors.GREY, color=colors.BLACK),

            ElevatedButton(text='%', expand=1, on_click=button_click,
                           bgcolor=colors.GREY, color=colors.BLACK),

            ElevatedButton(text='√', expand=1, on_click=button_click,
                           bgcolor=colors.GREY, color=colors.BLACK),

            ElevatedButton(text='/', expand=1, on_click=button_click,
                           bgcolor=colors.ORANGE, color=colors.WHITE),
        ]
    )

    button_row1 = Row(
        [
            ElevatedButton(text='7', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='8', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='9', expand=1, color=colors.WHITE, on_click=button_click),

            ElevatedButton(text='*', expand=1, on_click=button_click,
                           bgcolor=colors.ORANGE, color=colors.WHITE),
        ]
    )

    button_row2 = Row(
        [
            ElevatedButton(text='4', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='5', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='6', expand=1, color=colors.WHITE, on_click=button_click),

            ElevatedButton(text='-', expand=1, on_click=button_click,
                           bgcolor=colors.ORANGE, color=colors.WHITE),
        ]
    )
    button_row3 = Row(
        [
            ElevatedButton(text='1', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='2', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='3', expand=1, color=colors.WHITE, on_click=button_click),

            ElevatedButton(text='+', expand=1, on_click=button_click,
                           bgcolor=colors.ORANGE, color=colors.WHITE),
        ]
    )

    button_row4 = Row(
        [
            ElevatedButton(text='?', expand=1,
                           color=colors.WHITE24, bgcolor=colors.TRANSPARENT, on_click=question_click),

            ElevatedButton(text='0', expand=1, color=colors.WHITE, on_click=button_click),
            ElevatedButton(text='.', expand=1, color=colors.WHITE, on_click=button_click),

            ElevatedButton(text='=', expand=1, on_click=button_click,
                           bgcolor=colors.ORANGE, color=colors.WHITE)
        ]
    )

    container = Container(
        width=350, padding=20,
        bgcolor=colors.BLACK, border_radius=border_radius.all(20),
        content=Column([
            result, button_row0, button_row1,
            button_row2, button_row3, button_row4
        ]))

    page.add(container)


if __name__ == '__main__':
    app(target=main)
