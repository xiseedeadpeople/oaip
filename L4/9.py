def main():
    pasw = input()
    a = ''
    for i in pasw:
        if i in 'аяоёэеуюыи':
            a += '0'
        else:
            a += '1'
    
    print(a)
    
if __name__ == '__main__':
    main()
