Q = int(input())
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

    return prime
N = 10**5
A = sieve_of_eratosthenes(N)

B = []
for i in range(N+1):
    if (i+1) % 2 != 0 and i %2 ==0:
        B.append(0)
        continue 
    if A[i] and A[(i+1)//2]:
        B.append(1)
    else:
        B.append(0)

S = [0]
for i in range(N+1):
    S.append(S[-1] + B[i])

for _ in range(Q):
    l ,r = map(int, input().split())
    print(S[r+1] - S[l])
