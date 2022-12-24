N ,M = map(int, input().split())
A = list(map(int, input().split()))

ans = {i:M for i in range(1,N+1)}

for i in range(M):
    ans[A[i]] -=1

for i in range(1,N+1):
    print(ans[i])