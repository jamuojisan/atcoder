import sys
from collections import deque, defaultdict
import heapq
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

# N = n_int()
# N, M = map_int()
# A = n_list()
S = input()[:-1]
T = input()[:-1]
if len(T) > len(S):
    print('No')
    exit()
i = 0
for i in range(len(S)):
    if S[i] == T[0]:
        j = 1
        while(1):
            if j == len(T):
                print('Yes')
                exit()
            if S[i + j] == T[j]:
                j += 1
            else:
                break
print('No')                 
