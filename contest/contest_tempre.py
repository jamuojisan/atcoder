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

N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

dp = [[10**9]*(M+1) for _ in range(N+1)]
for i in range(M+1):
    dp[0][i] = 0

for n in range(1, N+1):
    dis = D[n-1]
    for m in range(M+1):
        if n > m:
            continue
        c = C[m-1]
        dp[n][m] = min(dp[n][m], dp[n-1][m-1] + c*dis, dp[n][m-1])
ans = 10 ** 9
for i in range(M+1):
    ans = min(ans, dp[N][i])      

print(ans)

