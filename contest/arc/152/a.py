N , L = map(int , input().split())
A = list(map(int, input().split()))
two_index = -1

for i, j in enumerate(A):
    if j == 2:
        two_index = i

if two_index == -1:
    print('Yes')
    exit()
nexty =1
for i in range(two_index):
    if A[i] == 1:
        nexty +=2
    else:
        nexty += 3
    
if nexty > L-1:
    print('No')
else:
    print('Yes')