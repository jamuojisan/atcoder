d = int(input())
n = int(input())
m = int(input())
dlis = [0]
for _ in range(n-1):
    dlis.append(int(input()))
dlis = sorted(dlis)
takuhai = []
for _ in range(m):
    takuhai.append(int(input()))

def bsearch(loc, val):
    if dlis[loc] <= val:
        return True
    else:
        return False

ans = 0
for t in takuhai:
    ok = 0
    ng = n
    while(ng -ok >1):
        mid = (ng+ok)//2
        if bsearch(mid, t):
            ok=mid
        else:
            ng = mid
    if ok <n-1:
        ans += min(t-dlis[ok], dlis[ok+1] - t)
    else:
        ans += min(t - dlis[ok], d-t)
print(ans)