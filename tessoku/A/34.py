N, X, Y = map(int, input().split())


Grundy = [False]*(10**5+1)
tempre = {0, 1, 2}
for i in range(10**5+1):
    if i < min(X,Y):
        Grundy[i] = 0
    else:
        tmp = set()
        if i - X >= 0:
            tmp.add(Grundy[i-X])
        if i -Y >= 0:
            tmp.add(Grundy[i-Y])
        Grundy[i] = min(tempre - tmp)
        
A = list(map(int, input().split()))

ans = Grundy[A[0]]

for i in A[1:]:
    ans ^= Grundy[i]

if ans == 0:
    print('Second')
else:
    print('First')

