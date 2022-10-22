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
q = int(input())
table = sieve_of_eratosthenes(10**5+1)
prime_table = set()
for i in range(10**5+1):
    if table[i]:
        prime_table.add(i)

for _ in range(q):
    l,r = map(int,input().split())
    ans = 0
    for i in range(l, r+1):
        if i in prime_table and ((i+1)//2) in prime_table:
            ans +=1
    print(ans)
