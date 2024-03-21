from random import choice, random, randrange


class Tamagotchi:
    def __init__(self):

        self.__pet = None
        self.__pets_list = ['Babytchi', 'Marutchi', 'Kuchitamatchi',
                            'Mametchi', 'Ginjirotchi', 'Maskutchi',
                            'Kuchipatchi', 'Nyorotchi', 'Tarakotchi',
                            'Oyajitchi', 'Bill']
        self.__pet = ''
        self.__summon_status = False
        self.__hitpoints = 100
        self.__sickness_status = False

    def getinfo(self):
        if self.__alive():
            print(f'Питомец: {self.__pet}\n'
                  f'Уровень здоровья: {self.__hitpoints}')
        else:
            print('Питомец мертв.')

    def summon_pet(self):
        """функция для призывания питомца"""

        if self.__summon_status is False:
            self.__pet = choice(self.__pets_list)
            self.__summon_status = True

            print(f'Вам выпал питомец {self.__pet}!')

        else:
            print(f'Вы уже призвали питомца ({self.__pet})')

    def sleep(self):
        """функция для сна"""

        if self.__alive():
            print('Вы уложили питомца спать.')
            self.__restore_hp()

        else:
            print('Питомец мертв.')

    def eat(self):
        """функция для еды"""

        if self.__alive():
            print(f'{self.__pet} ест.')
            self.__restore_hp()

        else:
            print('Питомец мертв.')

    def walk(self):
        """функция для еды"""
        if self.__alive():
            print(f'Вы вывели {self.__pet} на прогулку!.')
            self.__illness_posibility()
            self.__restore_hp()

        else:
            print('Питомец мертв.')

    def play(self):
        """функция для игры с питомцем"""

        if self.__alive():
            self.__illness_posibility()
            print(f'Вы поиграли с {self.__pet}.')
            self.__restore_hp()

        else:
            print('Питомец мертв.')

    def __illness_posibility(self):
        if 0.4 < random() < 0.7:
            print(f'{self.__pet} заболел! Здоровье упало. {self.__hitpoints} -->', end=' ')

            self.__sickness_status = True
            self.__hitpoints -= randrange(20, 50)

            print(f'{self.__hitpoints}\n')

    def __restore_hp(self):
        """функция которая восстанавливает здоровье"""

        if self.__sickness_status is False:
            if self.__hitpoints < 100:
                print(f'Здоровье восстановилось! {self.__hitpoints} --> ', end=' ')
                self.__hitpoints += randrange(10, 40)

                if self.__hitpoints > 100:
                    self.__hitpoints = 100

                print(self.__hitpoints)
        else:
            self.__sickness_status = False

    def __alive(self):
        return True if self.__hitpoints > 0 else False
