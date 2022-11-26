N, K = map(int, input().split())
A = list(map(int, input().split()))

ok = 10**9
ng = 0

while(ok -ng > 1):
    mid = (ok+ng)//2
    maisu = 0
    for i in A:
        maisu += (mid//i)
    if maisu >= K:
        ok = mid
    else:
        ng = mid

print(ok)

