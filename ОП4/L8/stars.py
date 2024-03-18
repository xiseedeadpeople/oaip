def stars():
    a = input('inp: ').split()
    print(*list(map(lambda x: x.rjust(len(sorted(a, key=len)[-1]), '*'), a)), sep='\n')
