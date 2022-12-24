N, M  = map(int, input().split())
if abs(N-M) >1:
    print(0)
    exit()
mod = 10**9 + 7
zanm = M
zann = N
ans1 = 1
for i in range(N+M):
    if i%2==0:
        ans1 *= zanm
        ans1 %= mod
        zanm -=1
    else:
        ans1 *= zann
        ans1 %= mod
        zann -=1

zanm = M
zann = N
ans2 = 1
for i in range(N+M):
    if i%2==0:
        ans2 *= zann
        ans2 %= mod
        zann -=1
    else:
        ans2 *= zanm
        ans2 %= mod
        zanm -=1

print((ans1 + ans2)%mod)