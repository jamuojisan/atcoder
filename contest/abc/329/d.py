N, M = map(int, input().split())
A = list(map(int, input().split()))

from collections import defaultdict
touhyou = [0]*N
min_tokuhyou = [10**9]*M
max_ = 0
for a in A:
    touhyou[a-1] += 1
    if touhyou[a-1] >= max_:
        max_ = touhyou[a-1]
        if a-1 < min_tokuhyou[max_-1]:
            min_tokuhyou[max_-1] = a-1
    print(min_tokuhyou[max_-1]+1)
    