def template(a, b, c):
    p = a + b + c
    
    print(f'периметр: {p}')
    print(f'площадь: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')
    print(f'равнобедренный: {"да" if a == b or b == c or a == c else "нет"}')
    print(f'равносторонний: {"да" if a == b and b == c else "нет"}')
