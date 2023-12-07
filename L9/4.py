def main():
    try:
        a = int(input())
        b = int(input())
        print(2 / 0)
    
    except ZeroDivisionError:
        print('ZeroDivErr!')
    
    except ValueError:
        print('ValueErr!')


if __name__ == "__main__":
    main()
