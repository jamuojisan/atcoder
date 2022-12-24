def judge(val):
    # スコアvalで達成できるかどうか
    length = 0
    count = 0
    for i in range(N):
        if i == 0:
            length += A[0]
        else:
            length += A[i]  - A[i-1] 
        if length >= val:
            count += 1
            length = 0
        if count == K:
            if L - A[i] >= val:
                return True
            else:
                return False
    return False
    
N ,L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

ok = 0
ng = L
while(ng  -ok > 1):
    mid = (ok + ng) //2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)