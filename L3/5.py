def main():
    while True:
    a = int(input())
    if a != 0:
        if a % 3 == 0 and a % 7 == 0:
            print('Караул!')
            break
    
        elif a % 3 == 0 or a % 7 == 0:
            print(type(a))
    
        else:
            print(a)

    else:
        break

if __name__ == '__main__':
    main()
