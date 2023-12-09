tempre = 'atcoder'
def count_moji(s):
    from collections import defaultdict
    count = defaultdict(int)
    for _s in s:
        count[_s] += 1
    return count
S = input()
T = input()
c_T = count_moji(list(T))

for s in sorted(list(S), reverse=True):
    if s in c_T and c_T[s] > 0:
        c_T[s] -= 1
    elif ((s not in c_T) or (c_T[s] == 0)) and s != '@':
        if s in tempre and c_T['@'] > 0:
            c_T['@'] -= 1
        else:
            print('No')
            exit()
    elif s == '@':
        flg = True
        for _s in list(tempre):
            if _s in c_T and c_T[_s] > 0:
                c_T[_s] -= 1
                flg = False
                break
        if flg:
            if c_T['@'] > 0:
                c_T['@'] -= 1
                flg = False
        if flg:
            print('No')
            exit()
    else:
        print('No')
        exit()
print('Yes')
            
        
    