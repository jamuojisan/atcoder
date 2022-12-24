N ,K = map(int, input().split())
A = [*map(int, input().split())]

right = 0
ans = 0
for left in range(N):
    while(right < N and A[right]- A[left] <= K ):
        val = A[right]
        right += 1
    ans += right - left - 1
    if right == left:
        right +=1
print(ans)
        
        