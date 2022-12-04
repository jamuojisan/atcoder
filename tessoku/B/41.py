X,Y = map(int,input().split())

ans = [[X,Y]]
while(X >= 2 or Y>=2):
    if X>Y:
        X = X-Y
    else:
        Y = Y-X
    ans.append([X,Y])
if len(ans) == 1:
    print(0)
    exit()
ans.reverse()
print(len(ans)-1)
for x,y in ans[1:]:
    print(x, y)
    

