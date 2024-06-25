def gears(data, n, m):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                size1 = data[i][0] / data[i][1]  # размер первой шестерёнки
                size2 = data[j][0] / data[j][1]  # размер второй шестерёнки
                if size1 == n / m and size2 == m / n:
                    return (data[i][0], data[j][0])
    return (None, None)
