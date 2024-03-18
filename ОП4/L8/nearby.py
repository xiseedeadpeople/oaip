def nearby(data, places=4):
    return list(filter(lambda x: '0' * places in x, data))
