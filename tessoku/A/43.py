N, L = map(int, input().split())

ans = 0
for _ in range(N):
    a, b = map(str, input().split())
    a = int(a)
    if b == 'E':
        ans = max(ans, L-a)
    else:
        ans = max(ans, a)
print(ans)