def main():
    l1 = [int(input()) for i in range(int(input()))]
    l2 = []
    
    for el in range(len(l1)):
    for j in range(len(l1) - el):
        l2.append(l1[el] - l1[j])
    
    print(sorted(list(set(l2))))

if __name__ == "__main__":
    main()
