def main():
    a = int(input())
    x = []
    x.append(a)
    
    while a < 100:
    
        a = int(input())
        x.append(a)
    
    x.sort()
    print(x[-3])

if __name__ == '__main__':
    main()
