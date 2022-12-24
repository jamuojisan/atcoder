N,H, W = map(int, input().split())
A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)
C = A + B
s = C[0]
for i in C[1:]:
    s ^= i

if s == 0:
    print('Second')
else:
    print('First')

