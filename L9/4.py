def main():
    try:
        a = int(input())
        b = int(input())
        print(2 / 0)
    
    except (ZeroDivisionError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
