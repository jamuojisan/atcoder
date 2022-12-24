from sys import stdin
input = stdin.readline

def count(t):
    count_matrix = [[0]*n for _ in range(m)]
    for l in range(m):
        for p in range(n):
            if c[l][p] == t:
                count_matrix[l][p] = 1
            else:
                count_matrix[l][p] = 0
    return count_matrix

def cumlative_sum(target):
    matrix = [[0]*(n+1) for _ in range(m+1)]
    for l in range(m):
        for p in range(n):
            matrix[l+1][p+1] = matrix[l][p+1] + matrix[l+1][p] - matrix[l][p] + target[l][p]
    return matrix

m,n = map(int, input().split())
k = int(input())


c = []
for _ in range(m):
    c.append(input())
abcd = []
j = count('J')
o = count('O')
i = count('I')

J = cumlative_sum(j)
O = cumlative_sum(o)
I = cumlative_sum(i)
for _ in range(k):
    _a,_b, _c, _d = map(int, input().split())
    _a,_b,_c,_d = _a-1, _b-1, _c, _d
    print(J[_c][_d] -J[_a][_d] - J[_c][_b] + J[_a][_b], O[_c][_d] -O[_a][_d] - O[_c][_b] + O[_a][_b], I[_c][_d] -I[_a][_d] - I[_c][_b] + I[_a][_b])
