def future(*mass, **const):
    global VIN
    sum_mass = sum(mass)
    if VIN < sum_mass:
        return "ACCELERATION"
    elif VIN > sum_mass:
        return "DECELERATION"
    else:
        return "UNCHANGED"
