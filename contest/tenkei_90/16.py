n = int(input())
a,b, c = map(int, input().split())

ans = 10 ** 9
for i in range(10000):
    for j in range(10000):
        if i + j > 9999:
            continue
        nokori = n - (a*i + b*j)
        if nokori  == 0:
            ans = min(ans, i + j)
        elif nokori % c ==0 and nokori > 0:
            ans = min(ans, i + j + (nokori//c))
print(ans)