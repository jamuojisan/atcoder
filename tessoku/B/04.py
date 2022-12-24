N = input()

ans = 0
for i, j in enumerate(reversed(list(N))):
    ans += int(j) * (2** i)
print(ans)
 