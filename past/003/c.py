a, r, n = map(int, input().split())

if a > 10 ** 9:
    print('large')
    exit()
if r == 1:
    print(a)
    exit()

ans = a
for i in range(min(30,n-1)):
    ans *= r

if ans > 10**9:
    print('large')
else:
    print(ans)
