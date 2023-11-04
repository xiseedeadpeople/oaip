def main():
    year = int(input())
    print('да') if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else print('нет')

if __name__ == '__main__':
    main()
