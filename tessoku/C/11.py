
def getnum(border):
    num = 0
    for i in range(N):
        num += A[i]//border
    return num
    

N ,K = map(int,input().split())
A = [*map(int,input().split())]

ok = 10**9
ng = 0

for i in range(60):
    mid = (ok+ng)/2
    if getnum(mid) <K:
        ok = mid
    else:
        ng = mid

ans = []
for i in range(N):
    ans.append(int(A[i]//ng))
print(*ans)

