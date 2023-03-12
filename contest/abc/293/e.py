def mat_mul(a, b, m):
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= m
    return c

def mat_pow(x, n, m):
    y = [[0]*len(x) for _ in range(len(x))]
    
    for i in range(len(x)):
        y[i][i] = 1
    
    while(n > 0):
        if n&1:
            y = mat_mul(x,y, m)
        x = mat_mul(x,x, m)
        n >>=1
    return y
A, X, M = map(int,input().split())

if A == 1:
    print(X%M)
else:
    print( (((pow(A,X,M*(A-1)) -1)) // (A-1) )%M )
# aa = [[A,1], [0,1]]
# a_x = mat_pow(aa, X, M)
# print(a_x[0][1])
