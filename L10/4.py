from random import choice

a = ['Да', 'Нет', 'Скорее всего да',
     'Возможно', 'Скорее всего нет',
     'Имеются перспективы', 'Вопрос задан неверно']


if __name__ == "__main__":
    input('Задай же свой вопрос: ')
    print(f'Магический шар считает, что: {choice(a)}')
