N, X = map(int, input().split())
A = sorted(map(int, input().split()))

ok = 0
ng = N
while(ng-ok > 1):
    mid = (ok + ng)//2
    if X >= A[mid]:
        ok = mid
    else:
        ng = mid

print(ok +1)