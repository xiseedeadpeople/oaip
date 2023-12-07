def main():
    y = {
        1_000_000 * 2800: 'Archaea',
        1_000_000 * 635: 'Proterozoic',
        1_000_000 * 300: 'Paleozoic',
        1_000_000 * 145: 'Mesozoic'
    }
    
    
    while True:
        request_ = input()
        if request_ == '':
            break
    
        else:
            if int(request_) > 1_000_000 * 4500:
                print('земли еще не существовало!')
    
            else:
                if int(request_) not in list(y.keys()):
                    if int(request_) < list(y.keys())[-1]:
                        print('Cenozoic')
    
                else:
                    for i in list(y.keys()):   # входные данные в примере неправильные, т.к. там при вводе 3 млн. выводит 'Archaea'
                        if int(request_) > i:  # и так далее, а в условии задачи - 'Archaea' - 2800 млн. лет назад
                            print(y[i])        # try 2800000001, 635000001, 300000001, 145000001
                            break

if __name__ == '__main__':
    main()
