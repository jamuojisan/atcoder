N, X, Y = map(int ,input().split())
r2c = {i:0 for i in range(1,N+1)}
b2c = {i:0 for i in range(1,N+1)}
r2c[N] = 1

while(N>1):
    b2c[N] += r2c[N]*X
    r2c[N-1] += r2c[N]
    r2c[N] = 0
    r2c[N-1] += b2c[N]
    b2c[N-1] += b2c[N]*Y
    b2c[N] = 0
    N -= 1
print(b2c[1])

