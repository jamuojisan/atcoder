N = int(input())
A = [*map(int, input().split())]

ans = 0
right = 0
val1 = 0
val2 = 0
for left in range(N):
    while(right< N and val1+A[right] == val2^A[right]):
        val1 += A[right]
        val2 ^= A[right]
        right += 1
         
    ans += right - left

    if left == right:
        right += 1
    else:
        val1 -= A[left]
        val2 ^= A[left]
        
print(ans)
        
