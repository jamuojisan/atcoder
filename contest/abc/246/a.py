x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

from collections import defaultdict
countx = defaultdict(int)
county = defaultdict(int)
for x, y in [[x1, y1], [x2,y2], [x3, y3]]:
    countx[x] += 1
    county[y] += 1
for i in countx:
    if countx[i] == 1:
        ansx = i
for i in county:
    if county[i] == 1:
        ansy = i
print(ansx, ansy)