N =int(input())
S = [input() for _ in range(N)]
from collections import defaultdict
count = defaultdict(int)
for i in S:
    count[i] +=1
AC = 'AC'
WA = 'WA'
TLE = 'TLE'
RE ='RE'
print(f'AC x {count[AC]}')
print(f'WA x {count[WA]}')
print(f'TLE x {count[TLE]}')
print(f'RE x {count[RE]}')

