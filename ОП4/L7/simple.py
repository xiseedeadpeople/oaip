def simple(n, div=None):  # 4
    if div is None:
        div = n - 1

    while div >= 2:
        if n % div == 0:
            return 'число не простое'
        else:
            return simple(n, div-1)
    else:
        return 'число простое'
