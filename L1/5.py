def main():
    a = input()
    if len(a) > 2:
        print(a[:len(a) // 2][-1]) if len(a) % 2 == 0 else print(a[:(len(a) + 1) // 2][-1])
    else:
        print(a[-1])

if __name__ == "__main__":
    main()
