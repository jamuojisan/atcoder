N = int(input())
A = [*map(int,input().split())]
from collections import defaultdict
count = defaultdict(int)


for i in A:
    count[i] += 1

ans = 0
for i in range(1,2*(10**5)+1):
    for j in range(1,2*(10**5)//i+1):
        ans += count[i]*count[j]*count[i*j]
print(ans)
    