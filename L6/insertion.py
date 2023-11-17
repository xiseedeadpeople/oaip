def main():
    l2 = [12, 5, 7, 2, 8]
    for i in range(1, len(l2)):
        x = l2[i]
        j = i

        while j > 0 and l2[j - 1] > x:
            l2[j] = l2[j - 1]
            j -= 1

        l2[j] = x

    print(l2)

if __name__ == '__main__':
    main()
