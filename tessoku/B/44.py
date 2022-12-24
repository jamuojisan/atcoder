N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
gyou = [i for i in range(N)]
Q = int(input())
for _ in range(Q):
    q, x, y = map(int ,input().split())
    x, y = x-1, y-1
    if q == 1:
        gyou[x], gyou[y] = gyou[y], gyou[x]
    else:
        x = gyou[x]
        print(A[x][y])
