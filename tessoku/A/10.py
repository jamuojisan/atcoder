N = int(input())
A = list(map(int, input().split()))
D = int(input())

L=[0] # S[i] is max_{j <= i} A[j]
for i in range(N):
    L.append(max(L[-1], A[i]))
R=[0]
for i in range(N):
    R.append(max(R[-1], A[N-1-i]))

for i in range(D):
    l, r= map(int, input().split())
    l,r = l-1, r-1
    print(max(L[l], R[N-r-1]))

