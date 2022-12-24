import math
a, b = map(int, input().split())
if a*b//math.gcd(a,b) > 10**18:
    print('Large')
else:
    print(a*b//math.gcd(a,b))
