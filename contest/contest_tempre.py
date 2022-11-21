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

H, W, N, h, w = map_int()

A = [list(map(int, input().split())) for _ in range(H)]

count = [[[0]]]

for i in range(H):
    for j in range(W):
        count[A[i][j]] += 1


ans = []
for i in range(H-h+1):
    _ans = []
    for j in range(W-w+1):
        bcount = defaultdict(int)
        B= np.ravel(A[i:i+h,j:j+w])
        for b in B:
            bcount[b] +=1
        __ans = len(set(count.keys()) - set(bcount.keys()))

        for b in (set(count.keys()) & set(bcount.keys())):
            if count[b] > bcount[b]:
                __ans+=1

        _ans.append(__ans)
        
    ans.append(_ans)
for i in range(H-h+1):
    print(*ans[i])
        