def main():
    summ = input('Введите сумму:\n')

    for i in range(len(summ)):
        print(f'{summ[::-1][i]} - по 1{"0" * i}')

if __name__ == "__main__":
    main()
