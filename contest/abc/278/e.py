H, W, N, h, w= map(int, input().split())
A =[list(map(int, input().split())) for _ in range(H)]

count = [[[0]*(N+1) for _ in range(W+1)] for _ in range(H+1)] # i,jまでのkの数

for i in range(1, H+1):
    for j in range(1, W+1):
        for k in range(1, N+1):
            k = A[i-1][j-1]
            count[i][j][k] = count[i-1][j][k] + count[i][j-1][k] - count[i][j][j] 
ans = []
for i in range(H-h+1):
    _ans = []
    for j in range(W-w +1):
        __ans = 0
        for k in range(1,N+1):
            if (count[i+h][j+w][k] - count[i][j+w][k] - count[i+h][j][k] + count[i][j][k] > 1):
                __ans += 1
        _ans.append(__ans)
    ans.append(_ans)

for i in range(H-h+1):
    print(*ans[i])

for i in range(count)
        