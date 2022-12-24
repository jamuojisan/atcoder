N = int(input())
P = 1501 
field = [[0]*(P) for _ in range(P)]

for _ in range(N):
    x, y = map(int, input().split())
    x, y = x-1 ,y-1
    field[y][x] +=1

S = [[0]*(P+1) for _ in range(P+1)]
Q = int(input())

for i in range(1, P+1):
    for j in range(1, P+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] +field[i-1][j-1]


for _ in range(Q):
    a, b, c, d = map(int, input().split())
    a, b, c, d= a-1, b-1, c-1, d-1
    print(S[d+1][c+1] - S[b][c+1] - S[d+1][a] + S[b][a])


