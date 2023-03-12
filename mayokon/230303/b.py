import sys 
sys.setrecursionlimit(10**9)
def dfs(lis, depth):
    if depth == N:
        ans.append(lis)
    for j in range(lis[-1]+1, M+1):
        dfs(lis+[j], depth+1)
    return 
N, M =map(int ,input().split())
ans = []

for i in range(1, M+1):
    dfs([i], 1)
for _ans in ans:
    print(*_ans)
