def main():
    a = [2, 123, 12, 665, 9, 3, 6]
    a.sort()
    
    request_ = int(input())
    
    middle = len(a) // 2
    lowest = 0
    highest = len(a) - 1
    
    while a[middle] != request_ and lowest <= highest:
        if request_ > a[middle]:
            lowest = middle + 1
        else:
            high = middle - 1
        middle = (lowest + highest) // 2
    
    if lowest > highest:
        print('В списке числа нет')
    else:
        print(f'нашел: {middle}')

if __name__ == '__main__':
    main()
