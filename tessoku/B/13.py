N ,K = map(int, input().split())
A = [*map(int, input().split())]

right = 0
ans = 0
val = 0
for left in range(N):
    while(right < N and val + A[right]<= K ):
        val += A[right]
        right += 1
    ans += right - left
    if right == left:
        right +=1
    else:
        val -= A[left]
print(ans)