N ,M , T = map(int, input().split())
A = [*map(int, input().split())]
X2Y = {}
for i in range(M):
    x, y = map(int, input().split())
    X2Y[x] = y


flg = True
for i in range(N-1):
    if T - A[i] > 0:
        T -= A[i]
    else:
        flg = False
        break
    if i+2 in X2Y:
        T += X2Y[i+2]
if flg:
    print('Yes')
else:
    print('No')
