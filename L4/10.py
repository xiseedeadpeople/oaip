def main():
    message = 'ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ' \
              'ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??'
    
    res = ''
    for i in range(len(message) - 1):
        if message[i] != message[i + 1]:
            res += message[i]
    
    if message[-1] != res[-1]:
        res += message[-1]
    
    print(res)

if __name__ == '__main__':
    main()
