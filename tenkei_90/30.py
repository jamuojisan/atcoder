import math
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    sosu_list = [i for i, j in enumerate(prime) if j ]
    return sosu_list
N, K = map(int, input().split())
from collections import defaultdict
count_s = defaultdict(int)
sosu = sieve_of_eratosthenes(N)
for j in sosu:
    count = 1
    while(count*j <=N):
        count_s[j*count] +=1
        count +=1
ans = 0
print(sosu)
for i in range(N+1):
    if count_s[i] >= K:
        ans +=1
print(ans)