def gears(a, n, m):
    first = {}
    second = {}

    for i in a:
        for j in i:
            if j > 0:
                if j % n == 0:
                    rn = j // n

                    if rn not in first:
                        if rn in second:
                            return j, second[rn]
                        first[rn] = j
                        
                if j % m == 0:
                    rm = j // m

                    if rm not in second:
                        if rm in first:
                            return first[rm], j

                        second[rm] = j

    return None, None
