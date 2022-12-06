import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**7)
def n_int():
    return int(input())

def n_str():
    return input()


def map_int():
    return map(int, input().split())

def n_list():
    return list(map(int, input().split()))

def n_lislis(n):
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    return a

N ,P = map(int, input().split())

mod = 998244353
ans = 0
for i in range(N+1):
    if 2*i> N + 1:
        continue
    ans += P * 2*i
     # ans %= mod
    if 2*i == N:
        continue

    ans += (100-P)*(N - 2*i)
    # ans %= mod
print(ans)
    