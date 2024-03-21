class CreateButton:

    def __init__(self, pos: tuple, color: tuple, url: str):
        self.color = color
        self.pos = pos
        self.url = url

    def getinfo(self):
        print(f'позиция: {self.pos}\n'
              f'цвет: {self.color}\n'
              f'ссылка: {self.url}')

    def drag(self, x: int, y: int):
        """ функция для перемещения кнопки """

        self.pos = (x, y)
        print(f'вы переместили кнопку. новая позиция: {x}, {y}')

    def set_color(self, new_color):
        """ функция для перекрашивания кнопки """

        self.color = new_color
        print(f'вы перекрасили кнопку: {new_color}')

    def set_url(self, new_url):
        """ функция для вставления ссылки в кнопку """

        self.url = new_url
        print(f'вы вставили новую ссылку: {new_url}')
    
