N = int(input())
L = [*map(int ,input().split())]

from collections import defaultdict

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] + L[j] <=  L[k] or L[i] + L[k] <= L[j] or L[j] + L[k] <= L[i]:
                continue 
            if not(L[i] == L[j] or L[j]==L[k] or L[k] == L[i]):
                ans +=1
print(ans)
