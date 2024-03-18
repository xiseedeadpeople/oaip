def maximum(lst):  # 5
    if len(lst) == 1:
        return lst[0]

    else:
        return max(lst[0], maximum(lst[1:]))
