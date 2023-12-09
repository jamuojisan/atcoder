N , M, V = map(int, input().split())
A = [[ i*M + (j+1) for j in range(M)] for i in range(N)]

count = 0
S = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + A[i][j]
        if S[i+1][j+1] == V:
            count += 1
print(count)