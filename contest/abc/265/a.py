x, y, n = map(int, input().split())

ans = 10 ** 9
for i in range(101):
    for j in range(34):
        if i + 3*j != n:
            continue
        ans = min(ans, x*i + y*j)
print(ans)