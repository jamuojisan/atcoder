import sys
sys.setrecursionlimit(10**7)
def dfs(y, x, dy, dx, count, depth):
    if depth == 6:
        print('Yes')
        exit()
    if not(0<= x < N and 0<= y < N):
        return
    if S[y][x] == '.':
        count += 1
    if count > 2:
        return 
    dfs(y+dy, x+dx, dy, dx, count, depth+1)

N = int(input())
S = [input() for _ in range(N)]

for y in range(N):
    for x in range(N):
        for dy, dx in [[0,1], [1,0], [1,1], [-1, 1]]:
            visited = set()
            dfs(y, x, dy, dx, 0, 0)
print('No')