N, Q = map(int, input().split())
A = list(map(int,input().split()))
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])

for q in range(Q):
    l, r = map(int,input().split())
    l, r= l-1, r-1
    print(S[r+1]- S[l])