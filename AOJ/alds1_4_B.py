n = int(input())
s = sorted(list(map(int, input().split())))
q = int(input())
t = list(map(int, input().split()))


def bserch(loc, val):
    if val >= s[loc]:
        return True
    else:
        return False


ans = 0
for i in t:
    ok = 0
    ng = n
    while(ng-ok > 1):
        mid = (ok + ng) //2
        if bserch(mid, i):
            ok = mid
        else:
            ng = mid
    if s[ok] == i:
        ans +=1
print(ans)