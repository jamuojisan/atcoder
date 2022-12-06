def hantei(ss,ts):
    diff = 0
    for i in range(4):
        if ss[i] != ts[i]:
            diff +=1
    if diff == 0:
        return 1
    elif diff == 1:
        return 2
    else:
        return 3
N = int(input())

ST = []
for i in range(N):
    s, t = map(str, input().split())
    ST.append([s,t])

ans = []

for i in range(10000):
    flg = True
    s = str(i).zfill(4)
    for j in range(N):
        sp,t = ST[j]
        if hantei(s,sp) != int(t):
            flg = False
    if flg:
        ans.append(s)

if len(ans) == 1:
    print(ans[0])
else:
    print('Can\'t Solve')
