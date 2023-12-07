def main():
    res = []
    enc = 0
    resu = []
    while True:
        a = int(input())
    
        if a == 0:
            break
    
        else:
            enc += 1
            res.append(a)
    
    for i in res:
        if i % enc == 0:
            resu.append(i)
    
    print(resu)


if __name__ == '__main__':
    main()
