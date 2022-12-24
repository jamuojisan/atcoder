N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b = map(int, input().split())
    if a +b > 0:
        A.append(a+b)
    if a - b > 0:
        B.append(a -b)
    if -a + b > 0:
        C.append(-a + b)
    if -a -b > 0 :
        D.append(-a-b)
print(max(map(sum, [A,B,C,D])))