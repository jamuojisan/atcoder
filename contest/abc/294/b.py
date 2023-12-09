# S= input()
# N = int(input())
H, W = map(int ,input().split())
A = [list(map(int ,input().split())) for _ in range(H)]
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = [['.']*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            ans[i][j] ='.'
        else:
            ans[i][j] = s[A[i][j]-1]
            
for _ans in ans:
    print(''.join(_ans))