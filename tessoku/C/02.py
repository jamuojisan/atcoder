N = int(input())
A = [*map(int ,input().split())]

ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        ans = max(ans, A[i]+A[j])
print(ans)