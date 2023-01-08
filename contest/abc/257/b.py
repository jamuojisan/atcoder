N,K,Q =map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

loc2koma = {i:-1 for i in range(N)}
for i in A:
    loc2koma[i-1] = 1

for i in L:
    i -= 1
    

    