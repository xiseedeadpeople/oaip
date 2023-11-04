def main():
    ch = input()
    repeat_counter_string = 0
    repeat_counter_vr = 1
    vrem_max = []
    
    for k in range(int(input())):
        a = list(input())
    
        inds = [i for i, j in enumerate(a) if j == ch]
        inds.append(-6)
        print(inds)
    
        for el in range(len(inds) - 1): # по списку индексов
    
            if inds[el + 1] - inds[el] == 1:
                repeat_counter_vr += 1
    
            else: # если не повт
                vrem_max.append(repeat_counter_vr)
                repeat_counter_vr = 0
    
        print(vrem_max)

if __name__ == '__main__':
    main()
