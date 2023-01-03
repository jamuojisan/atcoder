N = int(input())
A = [*map(int, input().split())]
Q = int(input())

for _ in range(Q):
    query = list(map(int ,input().split()))
    if len(query) == 3:
        _ , k, x = query
        A[k-1] = x
    else:
        _ , k = query
        print(A[k-1])
