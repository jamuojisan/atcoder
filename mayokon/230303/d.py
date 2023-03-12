
N = int(input())
information = {}
for i in range(N):
    k = int(input())
    information[i] = []
    for j in range(k):
        x, y = map(int ,input().split())
        x -= 1
        information[i].append((x,y))

ans = 0
for n in range(2**N):
    honest = {}
    c = 0
    for i in range(N):
        if 1 & (n>>i):
            honest[i] = 1
            c += 1 
        else:
            honest[i] = 0
    flg = True
    for i in range(N):
        if honest[i]:
            honest_flg = 1
        else:
            honest_flg = 0
        if honest_flg == 0:
            continue
        for x, y in information[i]:
            if honest[x] == y:
                continue
            else:
                flg = False
                break
    if flg:
        if c > ans:
            ans = c
print(ans) 
    