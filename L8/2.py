def main():
    l1 = input().split(';')
    l2 = [i.split(',') for i in l1]

    for rows in range(len(l2)):
        for el in range(len(l2[rows])):

            if el + 1 == len(l2[rows]):
                print()

            else:
                if int(l2[rows][el]) >= 1000000000:
                    print(l2[rows][el], end=' ')


if __name__ == "__main__":
    main()
