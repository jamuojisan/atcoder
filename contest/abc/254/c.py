N, K = map(int, input().split())
A = [*map(int, input().split())]
B = [[] for _ in range(K)]
for i in range(N):
    B[i%K].append(A[i])

B = [sorted(b) for b in B]
ans = []
count = -1
for i in range(N):
    amari = (i %K)
    if amari == 0:
        count +=1
    ans.append(B[amari][count])

flg = True
for i in range(N-1):
    if ans[i] > ans[i+1]:
        flg = False
if flg:
    print('Yes')
else:
    print('No')


