def main():
    b = float(input())
    c = 0
    
    c = 1 if b > 36.6 else print(0)
    
    while b < 36.6:
        b = float(input())
        if b < 0:
            c += 1
    
    print(c)
    
if __name__ == '__main__':
    main()
