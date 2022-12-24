n  = int(input())
S  = input()

w = [0]
e = [0]
for i in S:
    if i == 'W':
        w.append(w[-1] + 1)
        e.append(e[-1])
    else:
        e.append(e[-1] + 1)
        w.append(w[-1])
ans  = 4* (10**5)

for i in range(n):
    ans = min(ans, (w[i] - w[0]) + (e[n] - e[i+1]))
print(ans) 
        
