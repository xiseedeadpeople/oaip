def main():
    l1 = [12, 5, 7, 2, 8]

    for i in range(len(l1) - 1):
        for j in range(len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                l1[j], l1[j + 1] = l1[j + 1], l1[j]


    print(l1)

if __name__ == '__main__':
    main()
