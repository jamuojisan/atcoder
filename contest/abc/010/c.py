xa, ya, xb, yb, t, v = map(int, input().split())
n = int(input())
import math
G1 =[[] for _ in range(n)]
G2 =[[] for _ in range(n)]
for _ in range(n):
    x, y = map(int, input().split())
    a_dis = math.sqrt((x-xa)**2 + (y-ya)**2)
    b_dis = math.sqrt((x-xb)**2 + (y-yb)**2)
    if a_dis + b_dis <= t*v:
        print('YES')
        exit()
print('NO')