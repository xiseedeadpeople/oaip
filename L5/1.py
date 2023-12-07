def main():
    b = [input() for i in range(int(input()))]
    print(len(set(''.join(b))))

if __name__ == '__main__':
    main()
