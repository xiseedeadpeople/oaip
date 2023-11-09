def main():
    ch = input()
    repcounter = 1
    streakreps = []
    mxinstrngs = []

    for k in range(int(input())):
        a = list(input())

        inds = [i for i, j in enumerate(a) if j == ch]
        inds.append(-6)

        for el in range(len(inds) - 1): # по списку индексов

            if inds[el + 1] - inds[el] == 1:
                repcounter += 1

            else: # если не повт
                streakreps.append(repcounter)
                repcounter = 1


        mxinstrngs.append(max(streakreps))
        streakreps = []

    print(max(mxinstrngs))

if __name__ == '__main__':
    main()
