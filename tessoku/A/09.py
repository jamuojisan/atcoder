H, W, N= map(int, input().split())
snow = [[0]*(W+1) for _ in range(H+1)]


for i in range(N):
    a, b, c, d = map(int, input().split())
    a,b,c,d = a-1, b-1, c-1, d-1
    snow[a][b] +=1
    snow[c+1][d+1] +=1
    snow[a][d+1] -=1
    snow[c+1][b] -=1

S = [[0]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + snow[i-1][j-1]

for i in range(1,H+1):
    print(*S[i][1:])