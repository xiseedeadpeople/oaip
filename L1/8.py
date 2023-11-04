def main():
    some_list = [str(i) for i in range(1, 9)]
    
    some_list.append('9') # добавить
    some_list.remove('1') # удалить
    
    srez_sm = some_list[2:5] # срез
    
    reversed_sm = some_list[::-1] # перевертыш 1
    some_list.reverse() # перевертыш 2 x1
    some_list.reverse() # перевертыш 2 x2
    
    dv = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    for i in range(len(dv)):
        print(f'{i + 1}: ',end=' ')
        for j in dv[i]:
            print(j, end=' ')
        print()
    
    some_list.clear()
    dv.clear()

if __name__ == "__main__":
    main()
