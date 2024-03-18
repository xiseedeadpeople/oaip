def horse2():

    place = input('расположение: ')
    rank = 'abcdefgh'

    moves = [[-2, 1], [-1, 2], [1, 2], [2, 1],
             [2, -1], [1, -2], [-1, -2], [-2, -1]]

    x = rank.find(place[0]) + 1
    y = int(place[1])

    for i in moves:
        nx, ny = x + i[0], y + i[1]

        if 0 < nx < 9 and 0 < ny < 9:
            print(f'{rank[nx - 1]}{ny}')
