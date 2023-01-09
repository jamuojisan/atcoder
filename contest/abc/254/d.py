def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n and i <=N:
        if n % i == 0:
            if n //i <= N:
                lower_divisors.append(i)
            if i != n // i and (n//i) <= N:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
N = int(input())
heihousu = []
for i in range(1,N+1):
    heihousu.append(i*i)

ans = 0
for s in heihousu:
    divisor = make_divisors(s)
    ans += len(divisor)
print(ans)