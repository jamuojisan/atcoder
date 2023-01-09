
N = int(input())

ans = 10**20
for a in range(1010101):
    ok = 1010101
    ng = -1
    while(ok - ng > 1):
        mid = (ok + ng) //2
        if a*a*a + mid*(a*a) + a*(mid*mid) + mid*mid*mid >= N:
            ok = mid
        else:
            ng = mid
    ans = min(a*a*a + ok*(a*a) + a*(ok*ok) + ok*ok*ok, ans)
print(ans)
