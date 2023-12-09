N, A, B = map(int ,input().split())
C = [*map(int, input().split())]

c = A+B
for i in range(N):
    if c == C[i]:
        print(i+1)