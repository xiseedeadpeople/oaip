def main():
    b = []
    while True:
        a = input()
    
        if a == 'стоп':
            break

        else:
            b.append(a)
    
    
    print(min(b, key=len)) if len(b) > 0 else print(0)

if __name__ == '__main__':
    main()
