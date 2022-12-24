# 約数列挙
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
itr = 1
val = 0
while(1):
    val += itr
    if len(make_divisors(val)) > 500:
        print(val)
        exit()
    itr +=1 