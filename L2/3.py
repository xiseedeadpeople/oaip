def main():
    a, b, c = input(), input(), input()
    if f'{a}{b}{c}' == '123' or f'{a}{b}{c}' == 'раздватри':
        print('ГОРИ')
    
    else:
        print('НЕ ГОРИ')

if __name__ == "__main__":
    main()
