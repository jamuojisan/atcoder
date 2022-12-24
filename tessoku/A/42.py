N, K = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = 0 
for i in range(1, 101):
    for j in range(1,101):
        _ans = 0
        for k in range(N):
            a, b = A[k], B[k]
            if i <= a <= K +i and j <= b <= K + j:
                _ans += 1
        ans = max(ans, _ans)
print(ans)

