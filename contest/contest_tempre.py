import sys
from collections import deque, defaultdict

input = sys.stdin.readline
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

N = n_int()
ans = []
for i in range(1,N):
    print('?', i, i+1)
    print()
    m = input()
    ans.append(m)
for i in range(1, N+1):
    if i not in set(ans):
        ans.append(i)
print('!', *ans)
exit()

        