N = int(input())
A = sorted([*map(int, input().split())])
countl = [0]
countr = [N-1]
val = A[0]
_countl=0
_countr=0
for i in range(N):
    if val < A[i]:
        val = A[i]
        countl.append(countl[-1]+_countl)
        _countl = 1
        _countr = -1
        countr.append(countr[-1]+_countr)
    else:
        _countl += 1
        _countr -= 1
        countl.append(countl[-1])
        countr.append(countr[-1])
print(countl)
print(countr)

