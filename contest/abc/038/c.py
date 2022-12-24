N = int(input())
S = [*map(int, input().split())]

ans = 0
right = 0
for left in range(N):
    while(right + 1< N and S[right] < S[right + 1]):
        right += 1
    ans += right - left + 1
    
    if left == right:
        right += 1
print(ans)
        
