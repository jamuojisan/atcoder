from collections import defaultdict
n ,x = map(int, input().split())
A = []
B = []
for i in range(n):
    if i % 2 == 0:
        A.append(int(input()))
    else:
        B.append(int(input()))

dic = defaultdict(int)

for i in range(2**(len(B))):
    s = 0
    for j in range(len(B)):
        if i & (1 << j):
            s += B[j]
    dic[s] += 1

ans = 0

for i in range(2**(len(A))):
    s = 0
    for j in range(len(A)):
        if i & (1 << j):
            s += A[j]
    if (x - s) in dic:
        ans += dic[x-s] 

print(ans)