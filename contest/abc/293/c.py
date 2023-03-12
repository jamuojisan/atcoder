import sys
sys.setrecursionlimit(10**9)
def dfs(y,x, visitlist):
    global ans
    if y == H-1 and x == W-1:

        ans += 1
        return
    for dy, dx in [[1,0], [0,1]]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0<= nx < W and A[ny][nx] not in visitlist:
            dfs(ny, nx, visitlist | {A[ny][nx]})


H, W = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(H)]

ans = 0
dfs(0,0, {A[0][0]})
print(ans)
