n,m,  = map(int, input().split())
p = list(map(int,input().split()))
p = [i-1 for  i in p]
abc =[]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    abc.append([a,b,c])
S = [0]*(n+1)
for i in range(m-1):
    a, b= p[i], p[i+1]
    if a > b:
        a, b= b, a
    S[a]   +=1
    S[b]   -=1

count = [S[0]]
for i in range(1, n+1):
    count.append(count[-1] + S[i])

ans = 0
for i in range(n-1):
    k = count[i]
    a, b, c = abc[i]
    ans += min(k*a, k*b + c)

print(ans)
    
