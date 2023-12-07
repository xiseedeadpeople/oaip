def main():
    l1 = ['Вася', 'Саша', 'Маша', 'Толя', 'Андрей', 'Таня', 'Ира']
    request = 'Таня'

    for i in enumerate(l1):
        if i[1] == request:
            print(i[0])


if __name__ == '__main__':
    main()
