def main():
    p = False
    w = []
    for g in [i for i in range(1, 10001)]:
        for x in range(2, g - 1):
            if g % x != 0:
                p = True
            else:
                p = False
                break
        if p is True:
            w.append(g)

    print(sum(w))

if __name__ == "__main__":
    main()
