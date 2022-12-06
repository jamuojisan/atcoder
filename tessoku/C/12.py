def devide(val):
    num = 0
    for 


N, M, K = map(int, input().split())
AB=[[*map(int,input().split())] for _ in range(M)]
dp = [[0]*(N+1) for _ in range(K+1)] # dp[k][i]: ｋ章までの割り当てがｋ章の最後のページがｊのときの最大値

for k in range(1, K+1):
    for i in range(1, N+1):
