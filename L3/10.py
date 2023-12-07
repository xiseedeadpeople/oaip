def main():
    x = ''
    while True:
        a = f'{input()} '
    
        if a != 'стоп ':
            if '!' in a:
                x += f'{a}\n'
    
            else:
                x += a
    
        else:
            break
    
    print(x)


if __name__ == '__main__':
    main()
