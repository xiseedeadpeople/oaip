def groundhog_day(data):
    if len(data) < 2:
        return (0, 0)

    for i in range(1, len(data)):
        differences = 0
        diff_indices = []
        for j in range(len(data[i])):
            if data[i][j] != data[i-1][j]:
                differences += 1
                diff_indices.append(j)
                if differences > 2:
                    return (i, *diff_indices)
    
    return (0, 0)
