import math
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
A, B = map(int, input().split())
print(prime_factorize(abs(B-A)))
exit()
if B < A:
    A, B = B, A
g = math.gcd(A,B)
diff = abs(A-B)
count = 0
if abs(B-A) == 1:
    print(min(A,B))
    exit()
elif A==B:
    print(1)
    exit()
while(1):
    g = math.gcd(A, B)
    A -= g
    B -= g
    if g == diff:
        break
    count += 1
print(count + B//diff)

    