N, X, Y = map(int, input().split())

A = list(map(int, input().split()))

Grundy = [0, 0, 1, 1, 2]
Xor = 0
for i in range(N):
    Xor ^= Grundy[A[i] % 5]
    
        


if Xor == 0:
    print('Second')
else:
    print('First')

