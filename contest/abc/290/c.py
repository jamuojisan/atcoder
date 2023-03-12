N, K = map(int, input().split())
A = set(list(map(int, input().split())))
A = sorted(A)
count = 0
for i, j in enumerate(A[:K]):
    if i == j:
        count += 1
        continue
    else:
        print(i)
        exit()
print(count)