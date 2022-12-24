N , K = map(int, input().split())
S = [int(input()) for _ in range(N)]

if 0 in S:
    print(len(S))
    exit()

ans = 0
right = 0
val = 1
for left in range(N):
    while(right < N and val*S[right] <= K):
        val *= S[right]
        right += 1
    ans = max(ans, right - left)
    
    if left == right:
        right += 1
    else:
        val //= S[left]
print(ans)
        
