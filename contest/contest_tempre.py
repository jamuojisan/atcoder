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
def judge(val):
    for i in range(N):
        h, s, _ = HS[i]
        if h + s*i > val:
            return False
    return True


K, A, B = map(int, input().split())
