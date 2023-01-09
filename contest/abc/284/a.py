import sys
from collections import defaultdict
from collections import deque
import heapq
sys.setrecursionlimit(10**7)


N = int(input())
S = [input() for _ in range(N)]
for i in reversed(range(N)):
    print(S[i])
# N, M = map(int ,input().split())
# A = [*map(int, input().split())]
# C = [[*map(int, input().split())] for _ in range(N)]
# P = [[] for _ in range(N)]
