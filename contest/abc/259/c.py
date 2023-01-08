def ran_assyuku(s):
    rta = []
    tmp = s[0]
    count = 1
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            rta.append((tmp,count))
            count = 1
            tmp = s[i]
        if i == len(s) -1:
            rta.append((tmp, count))
    return rta



S = input()
T = input()
SS = ran_assyuku(S)
TT = ran_assyuku(T)
if len(SS) != len(TT):
    print('No')
else:
    for i in range(len(SS)):
        s, cs = SS[i]
        t, ct = TT[i]
        if s != t:
            print('No')
            exit()
        if cs == ct:
            continue
        else:
            if cs == 1 or cs > ct:
                print('No')
                exit()
    print('Yes')
