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
    prime_list = [i for i, j in enumerate(prime) if j]

    return prime_list
N = int(input())
prime_list = sieve_of_eratosthenes(int(N**(1/3)))

ans = 0
import bisect

for i, p in enumerate(prime_list):
    index = bisect.bisect_right(prime_list,N/(p**3))
    ans += min(i,index)

print(ans)
    
