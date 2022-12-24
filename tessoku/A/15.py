N = int(input())
A = list(map(int, input().split()))
B = sorted(A)

A2index= {}
index = 1 
for b in B:
    if b in A2index:
        continue
    else:
        A2index[b] = index
        index += 1


ans=[A2index[a] for a in  A]
print(*ans)