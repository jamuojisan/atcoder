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

X, Y = map(int, input().split())
A, B = X -2015, Y - 2015

for i in sorted(set(make_divisors(A)) & set(make_divisors(B))):
    print(i)
