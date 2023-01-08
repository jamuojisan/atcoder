N = int(input())
A = [*map(int, input().split())]
ans = 0
same = 0
diff = set()
for i, j in enumerate(A):
    if i+1 == j:
        same += 1
        continue
    if A[j-1] == i+1:
        if i+1 < j:
            diff.add((i+1, j))
        else:
            diff.add((j, i+1))

print((same*same - same)//2 + len(diff))
