import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime

is_prime_list = sieve_of_eratosthenes(10**7)
prime_list = []

for i, j in enumerate(is_prime_list):
    if i >= 2000000:
        break
    if j :
        prime_list.append(i)

print(sum(prime_list))
