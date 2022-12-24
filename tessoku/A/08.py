H, W= map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

S = [[0]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + X[i-1][j-1]

Q = int(input())
for q in range(Q):
    a, b, c, d = map(int, input().split())
    a,b,c,d = a-1, b-1, c-1, d-1
    print(S[c+1][d+1] - S[c+1][b] - S[a][d+1] + S[a][b])