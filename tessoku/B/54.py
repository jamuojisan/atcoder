from collections import defaultdict
N = int(input())
count = defaultdict(int)
for _ in range(N):
    n = int(input())
    count[n] += 1
ans = 0
for i in count:
    ans += count[i]*(count[i]-1)//2

print(ans)
