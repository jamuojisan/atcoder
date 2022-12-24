n = int(input())
s = [0] * (10**6 +3)

for _ in range(n):
    a, b = map(int, input().split())
    s[a] +=1
    s[b+1] -=1
ans = [s[0]]
for i in range(1,10**6 +3):
    ans.append(s[i] + ans[-1])

print(max(ans))