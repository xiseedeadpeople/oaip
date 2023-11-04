def main():
    s = set()
    s1 = set('raze')
    
    s.update('wwrz', '21')
    s.add('3')
    
    s_union = s.union(s1)
    s_union.pop()
    s_isctn = s.intersection(s1)
    s_symdif = s.symmetric_difference(s1)
    
    print(s_union, s_isctn, s_symdif)

if __name__ == '__main__':
    main()
