def main():
    q = ''
    while True:
        a = input()
    
        if a != 'стоп':
            q += a
    
        else:
            break
    
    print(eval(q))

if __name__ == '__main__':
    main()
