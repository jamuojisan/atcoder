N , P = map(int, input().split())
A = [*map(int, input().split())]

ans = 0
for i in A:
    if i < P:
        ans += 1

print(ans)
