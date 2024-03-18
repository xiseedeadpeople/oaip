def future(*mass, **const):

    VIN = 3
    CountConst = 1

    for key, value in const.items():
        CountConst *= float(value)
    sum_of_masses = sum(mass) * CountConst

    if sum_of_masses > VIN:
        return 'ACCELERATION'
    
    elif sum_of_masses < VIN:
        return 'DECELERATION'

    return 'UNCHANGED'
