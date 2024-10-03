from abc import ABC, abstractmethod


class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass


class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = "Меч"

    def attack(self):
        print(f"{self.name} атакует с помощью {self.weapon} мощным ударом!")


class Mage(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.spell = "Огненный шар"

    def attack(self):
        print(f"{self.name} использует заклинание {self.spell}, нанося магический урон!")


class Archer(GameCharacter):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = "Лук"

    def attack(self):
        print(f"{self.name} стреляет из {self.weapon}, нанося урон на расстоянии!")


class CharacterFactory:
    @staticmethod
    def create_character(character_type, name):
        if character_type.lower() == "воин":
            return Warrior(name)
        elif character_type.lower() == "маг":
            return Mage(name)
        elif character_type.lower() == "лучник":
            return Archer(name)
        else:
            raise ValueError(f"Неизвестный тип персонажа: {character_type}")


def main():
    print("Добро пожаловать в игру!")
    name = input("Введите имя вашего персонажа: ")

    print("Выберите класс персонажа:")
    print("1. Воин")
    print("2. Маг")
    print("3. Лучник")

    choice = input("Введите номер класса (1-3): ")

    if choice == "1":
        character_type = "воин"
    elif choice == "2":
        character_type = "маг"
    elif choice == "3":
        character_type = "лучник"
    else:
        print("Неверный выбор. Попробуйте снова.")
        return

    try:
        character = CharacterFactory.create_character(character_type, name)
        print(f"\nВы выбрали {character_type.capitalize()}а по имени {character.name}!")
        character.attack()
    except ValueError as e:
        print(e)
