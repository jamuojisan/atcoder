# pypyじゃないと通らない
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

import itertools
k = int(input())
yakusu_list = sorted(make_divisors(k))
ans = 0
for i in range(len(yakusu_list)):
    for j in range(i,len(yakusu_list)):
        a = yakusu_list[i]
        b = yakusu_list[j]
        if k % (a*b) == 0 and (k//(a*b)) >=b:
            ans += 1

print(ans)