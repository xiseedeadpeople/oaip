from string import ascii_lowercase as lcase, digits, punctuation, ascii_uppercase as ucase, ascii_letters
from random import choice, choices, sample

all_symbs = ascii_letters + punctuation + digits


def passgen(length, amount):
    passwords = []

    for el in range(amount):
        x = ''
        x += choice(lcase)
        x += choice(ucase)
        x += choice(digits)
        x += choice(punctuation)
        x += ''.join(choices(all_symbs, k=length - 4))

        rpas = sample(list(x), len(x))
        passwords.append(''.join(rpas))

    return passwords


if __name__ == "__main__":
    for pwd in passgen(int(input('Введите длину: ')), int(input('Введите количество: '))):
        print(f'{pwd}')
