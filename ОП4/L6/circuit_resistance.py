def circuit_resistance(*resistances, connection='serial', conductivity=False):
    if connection == 'serial':
        total_resistance = sum(resistances)
    elif connection == 'parallel':
        if any(r == 0 for r in resistances):
            return float('inf') if conductivity else 0.0
        total_resistance = 1 / sum(1 / r for r in resistances)
    else:
        raise ValueError("Unknown connection type. Should be 'serial' or 'parallel'.")
    
    if conductivity:
        if total_resistance == 0:
            return float('inf')
        else:
            return round(1 / total_resistance, 4)
    else:
        return round(total_resistance, 4)
