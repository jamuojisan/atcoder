N = int(input())
A = list(map(int, input().split()))

flg = A[0]

for i in A[1:]:
    flg ^= i

if flg == 0:
    print('Second')
else:
    print('First')