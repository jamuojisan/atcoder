# a, b = map(int, input().split())

# print(str(round(b/a, 3)).ljust(5, '0'))


# h,w = map(int, input().split())
# c = []
# for _ in range(h):
#     c.append(input())
# ans = [0]*w

# for i in range(h):
#     for j in range(w):
#         if c[i][j] == '#':
#             ans[j] +=1 
# for i in range(w):
#     print(ans[i], end=' ')

# n = int(input())
# a = list(map(int, input().split()))

# ans = {1:0}
# for i in range(1, n+1):
#     target = a[i-1]
#     ans[2*i] = ans[target] + 1
#     ans[2*i+1] = ans[target] + 1

# for i in range(2*n+1):
#     print(ans[(i+1)])
# G[target].append(2*i)
# G[target].append(2*i+1)
# if 2*i not in G:
#     G[2*i] = [target]
# else:
#     G[2*i].append(target)
# if 2*i+1 not in G:
#     G[2*i+1] = [target]
# else:
#     G[2*i+1].append(target)

from sys import stdin
input = stdin.readline
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
xx = []
yy = []
for i in range(1,n):
    if i % 2 == 0:
        xx.append(a[i])
    else:
        yy.append(a[i])


coordinate2num = {j: i for i, j in enumerate(range(-10**4, 10**4+1))}

dpx = [[0]*(2*(10**4)+1) for _ in range(n)]
dpy =  [[0]*(2*(10**4)+1) for _ in range(n)]

dpx[0][coordinate2num[a[0]]] = 1
dpy[0][coordinate2num[0]] = 1

for i in range(1,n):
    for j in range(2*(10**4)+1):
        if i%2 == 1:
            if dpy[i-1][j]:
                dpy[i][j + a[i]] = 1
                dpy[i][j - a[i]] = 1
            dpx[i][j] = dpx[i-1][j]
        elif i%2 == 0:
            if dpx[i-1][j]:
                dpx[i][j + a[i]] = 1
                dpx[i][j - a[i]] = 1
            dpy[i][j] = dpy[i-1][j]

if dpx[n-1][coordinate2num[x]] and dpy[n-1][coordinate2num[y]]:
    print('Yes')
else:
    print('No')


