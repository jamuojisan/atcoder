
N = int(input())
D = []
for i in range(N):
    D.append(list(map(int, input().split())))

S = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1, N+1):
        S[i][j] = D[i-1][j-1] + S[i][j-1] + S[i-1][j] - S[i-1][j-1]
ans = {}
for y in range(1,N+1):
        for x in range(1, N+1):
            if y > N or x > N:
                continue
            _ans = 0
            for i in range(N-y+1):
                for j in range(N-x+1):
                    _ans = max(_ans, S[i+y][j+x] - S[i+y][j] - S[i][j+x] + S[i][j])
            ans[(y,x)] = _ans 
Q = int(input())
for _ in range(Q):
    p = int(input())
    _ans = 0
    for y in range(1,N+1):
        for x in range(1, N+1):
            if y > N or x > N:
                continue
            if x * y > p:
                continue
            _ans = max(_ans, ans[(y,x)])
    print(_ans)
