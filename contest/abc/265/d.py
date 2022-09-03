def bsearch(x, mid, val):
    if S[mid] - S[x] <= val:
        return True
    else:
        return False


def calc_loc(x, val):
    if x == -1 or x == n:
        return -1
    low = x + 1
    up = n + 1
    while(up -low > 1):
        mid = (up + low)//2
        if bsearch(x, mid, val):
            low = mid
        else:
            up = mid
    if S[low] - S[x] == val:
        return low
    else:
        return -1

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

S = [0]
s = 0
for i in a:
    s += i
    S.append(s)

for i in range(n):
    y = calc_loc(i,p)
    z = calc_loc(y,q)
    w = calc_loc(z,r)
    if w != -1:
        print('Yes')
        exit()

print('No')
