def main():
    vows = 'аяоёэеуюыи'
    c = 0
    for i in input():
        if i in vows:
            c += 1
    
    print(c)
    
if __name__ == '__main__':
    main()
