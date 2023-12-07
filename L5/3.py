def main():
    numbers = set('0123456789')
    am = set(input())
    print(*am.symmetric_difference(numbers), sep=' ')
    
if __name__ == '__main__':
    main()
