n = int(input())
a = list(map(int, input().split()))

b = [0]
for i in a:
    b.append(b[-1]+i)

for k in range(1,n+1):
    ans = 0
    for i in range(n-k+1):
        ans = max(ans, b[i+k] -b[i])
    print(ans)