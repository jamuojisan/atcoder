import sys
from collections import defaultdict
from collections import deque
import heapq
sys.setrecursionlimit(10**7)
T = int(input())

for i in range(T):
    N = int(input())
    A = [*map(int, input().split())]
    count = 0
    for i in range(N):
        if A[i] %2 != 0:
            count +=1
    print(count)

