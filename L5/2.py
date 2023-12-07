def main():
    b = [set(input()) for x in range(3)]
    print(*set(b[0].intersection(b[1]).union(b[1].intersection(b[2]), b[0].intersection(b[2]))), sep='')

if __name__ == '__main__':
    main()
