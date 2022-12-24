n = int(input())
a = []

for i in range(n-1):
    _list = list(map(int, input().split()))
    a.append([0] * (i+1) + _list)

def has_bit(n, i):
    return (n & (1 << i) > 0 )

ALL = 2 ** n
happy = [0] * ALL

for N  in range(ALL):
    for i in range(n):
        for j in range(i+1, n):
            if has_bit(N, i) and has_bit(N, j):
                happy[N] += a[i][j]

ans = -10 **12


for n1 in range(ALL):
    for n2 in range(ALL):
        if n1 & n2 >0:
            continue
        
        n3 = ALL -1 - (n1|n2)
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])

print(ans)
        