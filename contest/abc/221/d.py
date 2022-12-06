from collections import defaultdict
N = int(input())

imosu = defaultdict(int)

for _ in range(N):
    a, b = map(int, input().split())
    imosu[a] +=1
    imosu[a+b] -= 1

days = sorted(imosu)

S = [0]
for i, j in enumerate(days):
    S.append(S[-1] + imosu[j])

ans = {i:0 for i in range(N+1)}
for i in range(len(days)-1):
    person = S[i+1]
    day = days[i+1] - days[i]
    ans[person] += day
_ans = []
for i in range(1,N+1):
    _ans.append(ans[i])
print(*_ans)

