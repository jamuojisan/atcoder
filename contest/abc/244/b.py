N = int(input())
T = input()
y = 0
x = 0
dd = [[0,1], [-1,0], [0,-1], [1, 0]]
d = 0
for i in range(N):
    t = T[i]
    if t == 'S':
        y, x = y + dd[d%4][0] , x + dd[d%4][1]
    else:
        d += 1
print(x , y)

