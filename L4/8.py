def main():
    phone = input()
    
    for i in phone:
        if i not in '123456789+':
            print('Неправильный номер телефона!')
            break

if __name__ == '__main__':
    main()
