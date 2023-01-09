N ,K = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
mx = max(A)
index = []
for i in range(N):
    if mx == A[i]:
        index.append(i+1)

for i in index:
    if i in B:
        print('Yes')
        exit()

print('No')