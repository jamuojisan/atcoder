n , k = map(int, input().split())
a = list(map(int,input().split()))

ok = n
ng = -1

while(ok - ng > 1):
    mid = (ng + ok) // 2
    if a[mid] >= k:
        ok = mid
    else:
        ng = mid
if ok == n:
    print(-1)
else:
    print(ok)