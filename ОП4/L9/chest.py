class CreateChest:

    def __init__(self, pos: tuple, status: str, content: str):
        self.status = status
        self.content = content
        self.pos = pos

    def drag(self, x: int, y: int):
        """ функция для перемещения сундука """

        self.pos += (x, y)
        print(f'вы переместили сундук. его новая позиция: {x}, {y}')

    def interact(self):
        """ функция для открытия/закрытия сундука """

        if self.status == 'closed':
            print(f'вы открыли сундук. вы нашли в нем: {self.content}')

        if self.status == 'opened':
            print('вы закрыли сундук.')

        chest.status_switch()

    def loot(self):
        """ функция для того чтобы ограбить сундук """

        if self.status == 'closed':
            print('сначала откройте сундук!')

        elif self.status == 'opened':
            print(f'вы забрали содержимое: {self.content}')

    def status_switch(self):
        """ функция для обновления статуса сундука (отркрыт, закрыт) """
        if self.status == 'closed':
            self.status = 'opened'

        else:
            self.status = 'closed'


chest = CreateChest((0, 0), 'closed', '123 золотых монеты')
chest.drag(2, 3)

print()

chest.interact()
chest.interact()

print()

chest.loot()

print()

chest.interact()
chest.loot()
