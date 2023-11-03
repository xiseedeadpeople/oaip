def main():
    amount = int(input())
    print('\n'.join([f'{str(i)}: {input()}' for i in range(1, amount + 1)]))

if __name__ == '__main__':
    main()
