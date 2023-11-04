from string import ascii_uppercase as alph

def main():
    print(f'Английский алфавит: {alph}')
    a = int(input())
    
    if a > len(alph):
        a -= ((a // 26) * 26)
        print(alph[a:a + 4], end='')
    
    elif 23 < a < 27:
        print(f'{alph[a::]}{alph[0:4-len(alph[a::])]}')
    
    elif 0 >= a >= -3:
        pass
    
    else:
        a -= 1
        print(alph[a:a+4], end='')

if __name__ == "__main__":
    main()
