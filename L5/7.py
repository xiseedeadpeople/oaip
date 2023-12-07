def main():
    a = {}
    
    while True:
        request_ = input()
    
        if request_ == '':
            break
    
        else:
            request_ = request_.split(': ')
            if request_[0] in a.keys():
                a[request_[0]] += int(request_[1])
    
            else:
                a[request_[0]] = int(request_[1])
    
    print(a)
    
if __name__ == '__main__':
    main()
