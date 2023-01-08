import sys
sys.setrecursionlimit(10**7)
def dfs(val, depth):
    if depth == N:
        print('Yes')
        exit()
    if abs(val - A[depth]) <= K:
        dfs(A[depth], depth+1)
    if abs(val - B[depth]) <= K:
        dfs(B[depth], depth+1)
    return 

N ,K = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]


dfs(A[0], 1)
dfs(B[0], 1)
print('No')