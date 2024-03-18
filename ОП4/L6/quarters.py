def quarters(d):

    q = {
        'I': 0,
        'II': 0,
        'III': 0,
        'IV': 0
    }

    for i in d:

        if i[0] > 0 and i[1] > 0:  # I
            q['I'] += 1

        elif i[0] < 0 < i[1]:  # II
            q['II'] += 1

        elif i[0] < 0 and i[1] < 0:  # III
            q['III'] += 1

        elif i[0] > 0 > i[1]:  # IV
            q['IV'] += 1

    return q
