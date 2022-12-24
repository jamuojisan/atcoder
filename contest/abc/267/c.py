import itertools
n,m = map(int, input().split())
a = list(map(int, input().split()))

S = [0] + list(itertools.accumulate(a))

ans = - 10**18

s_m = 0
for i in range(m):
    s_m += (i+1)*a[i]
ans = max(s_m, ans)
for i in range(n-m):
    s_m = s_m - (S[m+i] - S[i]) +m*a[m+i]
    ans = max(s_m, ans)
print(ans)

