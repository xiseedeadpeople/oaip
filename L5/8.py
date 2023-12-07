def main():
    a = input().split()
    res = []
    for i in a:
        d = {
            'digits': '0',
            'units': '0',
            'zeros': '0',
        }
        r = bin(int(i))[2::]
    
        d['digits'] = len(r)
        d['units'] = r.count('1')
        d['zeros'] = r.count('0')
    
        res.append(d)
    
    print(res)

if __name__ == '__main__':
    main()
