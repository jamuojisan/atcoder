import sys
sys.setrecursionlimit(10**7)
def dfs(val, depth):
    if depth == N:
        if val == 0:
            print('Found')
            exit()
        else:
            return 
    for j in range(K):
        dfs(val^T[depth][j], depth+1)
    
N, K = map(int ,input().split())
T = [[*map(int, input().split())] for _ in range(N)]
for i in range(K):
    dfs(0, 0)

print('Nothing')