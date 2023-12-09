N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x); Y.append(y)

X.sort();Y.sort()

ans = 0

if N %2== 1:
    for i in range(N):
        ans += abs(X[i] - X[N//2]) + abs(Y[i] - Y[N//2])
else:
    x, y= (X[N//2] + X[N//2 -1])//2, (Y[N//2] + Y[N//2 -1])//2
    for i in range(N):
        ans += abs(X[i] - x) + abs(Y[i] - y)
print(ans)