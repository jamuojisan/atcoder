# N = int(input())
# S = input()
N, M  = map(int, input().split())
# A = [*map(int, input().split())]
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if i == j:
            continue
        flg = True
        for k in range(M):
            if S[i][k] == 'o' or S[j][k] =='o':
                continue
            else:
                flg = False
        if flg:
            ans +=1

print(ans)
            