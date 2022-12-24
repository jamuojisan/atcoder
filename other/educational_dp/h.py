H ,W = map(int, input().split())
A = [input() for _ in range(H)]

dp = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = 1

mod = 10**9 + 7
for i in range(1, H+1):
    for j in range(1, W+1):
        if A[i-1][j-1] != '.':
            continue
        for di, dj in [[1, 0], [0, 1]]:
            ni, nj = i + di, j + dj
            if ni-1 < H and nj-1 < W and A[ni-1][nj-1] == '.':
                dp[ni][nj] += dp[i][j]
                dp[ni][nj] %= mod

print(dp[H][W])