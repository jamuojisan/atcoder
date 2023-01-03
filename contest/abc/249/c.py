N , K = map(int, input().split())
S = [input() for _ in range(N)]
syurui = {}
for i in range(N):
    syurui[i] = set(list(S[i]))
ans = 0
for n in range(2**N):
    select = []
    for i in range(N):
        if n & (1 << i):
            select.append(i)
    count = {s:0 for s in 'abcdefghijklmnopqrstuvwxyz'}
    for i in select:
        for j in syurui[i]:
            count[j] +=1
    _c = 0
    for i in count:
        if count[i] == K:
            _c +=1
    ans = max(ans, _c)
print(ans)