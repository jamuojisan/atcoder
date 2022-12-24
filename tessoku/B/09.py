N = int(input())
P = 1502 
imosu = [[0]*(P+1) for _ in range(P+1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    imosu[c][d] += 1
    imosu[a][b] += 1
    imosu[c][b] -= 1
    imosu[a][d] -= 1

S = [[0]*(P+2) for _ in range(P+2)]

for i in range(1, P+2):
    for j in range(1, P+2):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + imosu[i-1][j-1]

ans = 0
for i in range(P+2):
    for j in range(P+2):
        if S[i][j] >= 1:
            ans += 1
print(ans)
