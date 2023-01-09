def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N = int(input())
A = [*map(int, input().split())]

if 1 in A:
    print(0)
    exit()
from collections import defaultdict
count = defaultdict(int)
for i in A:
    count[i] +=1
A = [i for i in A if count[i] == 1]

ans = 0
for i in A:
    divisor = make_divisors(i)
    divisor = divisor[1:-1]
    flg = True
    for j in divisor:
        if j in set(A):
            flg = False
            break
    if flg:
        ans  += 1
print(ans)