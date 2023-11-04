def main():
    x = []

    while True:
        a = int(input())
        if -1000 < a < 1000:
            x.append(a)
        else:
            break
    
    x.sort()
    print(x[-2])

if __name__ == '__main__':
    main()
