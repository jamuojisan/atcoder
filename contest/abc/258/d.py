import math
N,X = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b  = map(int, input().split())
    A.append(a)
    B.append(b)

S =[0]
for i in range(N):
    S.append(S[-1] + A[i] + B[i])

ans = 10**20
for i in range(1,N+1):
    if X-i <0 :
        break 
    ans = min(ans, S[i] + (X-i)*B[i-1])
print(ans)