N = int(input())
A = [*map(int ,input().split())]
B = [*map(int ,input().split())]
x, y = 0, 0
common = set(A) & set(B)
for i in range(N):
    if not (A[i] in common and B[i] in common):
        continue
    if A[i] == B[i]:
        x += 1
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if  A[i] == B[j] and A[i] in common:
            y += 1
            
print(x)
print(y)
