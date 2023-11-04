def main():
    c = 0
    
    while True:
        a = float(input())
        if a > 36.6:
            break
    
        else:
            if a < 0:
                c += 1
    
    print(c)
    
if __name__ == '__main__':
    main()
