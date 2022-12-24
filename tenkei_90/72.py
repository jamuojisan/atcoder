def dfs(sy, sx):
    

h, w = map(int, input().split())

c = []
for _ in range(h):
    c.append(input())


for i in range(h):
    for j in range(w):
        sy = i
        sx = j
        if c[sy][sx] == '#':
            continue
        ans = max(ans, dfs(sy,sx))
print(ans)

