from bs4 import BeautifulSoup  # pip install requests lxml bs4
import requests
from random import choice

url = 'https://kupidonia.ru/spisok/spisok-suschestvitelnyh-russkogo-jazyka'

responce = requests.get(url).text
soup = BeautifulSoup(responce, 'lxml')
nouns = soup.findAll('div', class_='position_title')

# # все слова
# for item in nouns:
#     print(item.text.strip())


def hangman():
    print('Игра начинается! ... все слова на букву а, из за чего игра становится труднее ...')

    length = choice([i for i in range(5, 8)])

    while True:
        word = choice(nouns).text.strip()
        if len(word) != length:
            word = choice(nouns).text
        else:
            # print(f'{word}: {length}')
            break

    vowels = 'ауоыиэёеяю'
    turns = 3

    # game cycle
    while turns > 0:
        missed = 0

        for letter in word:

            if letter in vowels:
                print(letter, end=' ')

            else:
                print('_', end=' ')
                missed += 1

        if missed == 0:
            print('\nТы выиграл!')
            break

        guess = input()
        vowels += guess

        if guess not in word:
            turns -= 1
            print(f'Не угадал.')
            print(f'Осталось попыток: {turns}')

            if turns < 3:
                print(f'{20 * " "}__________________\n{20 * " "}|         |')
            if turns < 2:
                print(f'{20 * " "}|         O\n{20 * " "}|        /|\\')
            if turns < 1:
                print(f'{20 * " "}|         |\n{20 * " "}|        / \\\n{20 * " "}__________________')

            if turns == 0: print(f'Это слово: {word}')


if __name__ == "__main__":
    ans = 'да'
    while ans == 'да':
        hangman()
        ans = input('хотите сыграть снова? (да/нет): ')
