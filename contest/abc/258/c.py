N ,Q = map(int,input().split())
S = input()
length = len(S)
P = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        P += x
    else:
        print(S[(x-P-1)%N])