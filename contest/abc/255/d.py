N, Q =map(int,input().split())
A = sorted(list(map(int, input().split())))
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])

def bsearch(var):
    
    ok = -1
    ng = len(A)
    
    while(ng -ok > 1):
        mid = (ok+ng) //2
  
        if var >= A[mid] :
            ok = mid
        else:
            ng = mid 
    return ok
        
                 
for _ in range(Q):
    x = int(input())
    rindex = bsearch(x) #X以上となるインデックス
    migi = (S[N] - S[rindex+1]) - (N-rindex-1)*x
    hidari = (rindex+1)*x - S[rindex+1]
    print(migi+hidari)
