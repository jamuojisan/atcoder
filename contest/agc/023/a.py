N = int(input())
A =list(map(int,input().split()))
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])
from collections import defaultdict
count = defaultdict(int)

for i in S:
    count[i] +=1

ans = 0
for i in count:
    if count[i] >1:
        ans += count[i]*(count[i]-1)//2
print(ans)