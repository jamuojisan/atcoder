from collections import deque
S = input()
q = deque()
N = len(S)
ans = []
for i in range(N):
    if len(q) and S[i] == ')':
        _,index = q.pop()
        ans.append([index+1,i+1])
    else:
        q.append([S[i], i])

for a, b in ans:
    print(a,b)

