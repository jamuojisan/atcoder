N ,A, B = map(int, input().split())
from math import gcd
ans = N*(N+1)//2
if A == 1 or B ==1:
    ans = 0
else:
    for i in range(1, N//A+1):
        ans -= A*i
    for i in range(1, N//B +1):
        ans -= B*i
    L = A*B//(gcd(A,B))
    for i in range(1,N//(L)+1):
        ans += L*i
print(ans)