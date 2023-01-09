X, N =map(int ,input().split())
P = [*map(int, input().split())]

for i in range(100):
    if X-i in set(P) and  X+i in set(P):
        continue
    elif X-i in set(P):
        print(X+i)
        exit()
    elif X+i in set(P):
        print(X-i)
        exit()
    else:
        print(X-i)
        exit()