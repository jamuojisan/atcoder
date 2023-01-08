import sys 
sys.setrecursionlimit(10**7)
def dfs(y,x,dy, dx,val,depth,):
    y += dy
    x += dx
    y %= N
    x %= N
    val += A[y][x]
    if depth == N-1:
        ans.append(int(val))
        return
    dfs(y, x,dy, dx, val, depth+1) 

N = int(input())
A = [input() for _ in range(N)]

ans = []

for i in range(N):
    for j in range(N):
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, 1], [-1, -1], [-1,1]]:
            dfs(i,j,dy, dx, '', 0)
print(max(ans))