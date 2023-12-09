T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    
    one = S.count('1')
    zero = S.count('0')
    if (one %2) == 1:
        print(-1)
    else:
        if one != 2:
            print(one//2)
        else:
            flg = False
            for i in range(N-1):
                if S[i] == S[i+1] == '1':
                    flg =True
            if flg and N!=3:
                print(3)
            elif flg and N==3:
                print(-1)
            else:
                print(1)