def vows(s):  # 3
    if not s:
        return 0

    elif s[0].lower() in 'aeiou':
        return 1 + vows(s[1:])

    else:
        return vows(s[1:])
