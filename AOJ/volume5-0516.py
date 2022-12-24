while(1):
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        exit()
    
    a= [int(input()) for _ in range(N)]
    
    S=[0]
    for i in range(N):
        S.append(S[-1] + a[i])
    
    ans = 0
    for i in range(N-K):
        if S[i+K] -S[i] > ans:
            ans = S[i+K] -S[i]
    print(ans)
    