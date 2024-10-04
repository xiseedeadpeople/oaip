from abc import ABC, abstractmethod


class Char(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass


class Warrior(Char):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = 'меч'

    def attack(self):
        print(f'{self.name} атакует с помощью {self.weapon}, нанося сокрушительный урон!')


class Mage(Char):
    def __init__(self, name):
        super().__init__(name)
        self.spell = 'молния'

    def attack(self):
        print(f'{self.name} использует заклинание {self.spell}, нанося магический урон!')


class Archer(Char):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = 'лук'

    def attack(self):
        print(f'{self.name} стреляет из {self.weapon}, нанося урон на расстоянии!')


class CharFactory:
    @staticmethod
    def create_char(char_type, char_name):
        if char_type == 'воин':
            return Warrior(char_name)

        elif char_type == 'маг':
            return Mage(char_name)

        elif char_type == 'лучник':
            return Archer(char_name)

        else:
            raise ValueError(f'такого класса нет: {char_type}')


name_ = input('имя героя: ')
class_ = input('класс героя(маг/воин/лучник): ')

character = CharFactory.create_char(class_, name_)
character.attack()
