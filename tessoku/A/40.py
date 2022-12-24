
# ! 階乗
def factorial(k):
    x = 1
    for i in range(k):
        x = x*(k-i)
    return x
# ! mod 組み合わせ
def ncr(n,r):
    bunsi = factorial(n)
    bunbo1 = factorial(n-r)
    bunbo2 = factorial(r)
    
    bunbo = bunbo1*bunbo2 
    return bunsi //bunbo

N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict
count = defaultdict(int)

for i in A:
    count[i] += 1
ans = 0
for i in count:
    if count[i] < 3:
        continue
    ans += ncr(count[i], 3)
print(ans)





