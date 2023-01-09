N ,D = map(int ,input().split())
XY = [[*map(int, input().split())] for _  in range(N)]
ans  = 0
for i in range(N):
    if D*D >= XY[i][0]**2 + XY[i][1]**2:
        ans += 1
        
print(ans)