import itertools
import math
n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int , input().split())))


ans = 0
cnt = 0
for v in itertools.permutations(list(range(n)), n):
    cnt +=1
    dis = 0
    for i in range(len(v) -1 ):
        x1, y1 = xy[v[i+1]]
        x2, y2 = xy[v[i]]
        dis += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    ans += dis
print(ans/cnt)