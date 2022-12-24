n = int(input())
c = [[0]*7 for _ in range(7)]
import numpy as np
for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    c[y1][x1] +=1
    c[y2+1][x2+1] +=1
    c[y1][x2+1] -=1
    c[y2+1][x1] -=1
c = np.array(c)
print(c)
ans = [[0]*7 for _ in range(7)]
for i in range(7):
    for j in range(1,7):
        ans[i][j] = (ans[i][j-1] + c[i][j-1]) 

for i in range(7):
    for j in range(1,7):
        ans[j][i] = (ans[j-1][i] + c[j-1][i])

ans = np.array(ans)
print(ans)
for k in range(1,n+1):
    _ans = ans[ans==k]
    print(_ans)
    exit()
