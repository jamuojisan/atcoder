N, M, B = map(int, input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

sumc = sum(C)
ans = 0
for i in range(N):
    ans += (A[i]*M + sumc  + M*B)

print(ans)