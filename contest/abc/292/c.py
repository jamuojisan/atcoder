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
ans = 0

for i in range(1, N):
    j = N - i
    div_i = make_divisors(i)
    div_j = make_divisors(j)
    ans += (len(div_i) * len(div_j))
print(ans)
    