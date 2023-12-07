def main():
    b = [input() for i in range((int(input())))]
    for i in range(int(input())):
        print(b[i % len(b)])

if __name__ == '__main__':
    main()
