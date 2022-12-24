N = int(input())
A = [int(input()) for _ in range(N)]
A2index = {}
cnt = 0
for i in sorted(set(A)):
    A2index[i] = cnt
    cnt +=1

B = [A2index[i] for i in A]

for i in B:
    print(i)