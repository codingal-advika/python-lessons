def palid(r):
    e = len(r)
    s = 0
    while s<e:
        if(r[s] != r[e]):
            return False
        s = s+1
        e = e-1
        return True
    r = (1,2,3,3,2,1)
    if (palid(r)):
        print('This is flip-flop')
    else:
        print('This is not fip-flop')

palid()