N = int(input())
A = [*map(int, input().split())]

right = 0
ans = 0
f = set()
for left in range(N):
    while(right < N and  A[right] not in f ):
        f.add(A[right])
        right += 1
    ans = max(len(f), ans)
    if right == left:
        right +=1
    else:
        f.remove(A[left])

print(ans)