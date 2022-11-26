N, Q = map(int, input().split())

ans = [i for i in range(1,N+1)]

flg = 1
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        index, y = q[1:]
        if flg:
            ans[index-1] = y
        else:
            ans[N-index] = y
    elif q[0] == 2:
        flg = 1 - flg  
    else:
        index = q[1]
        if flg:
            print(ans[index-1])
        else:
            print(ans[N-index])
    