N = int(input())
LR = []
for _ in range(N):
    l,r = map(int, input().split())
    LR.append([l,r])
LR = sorted(LR, key=lambda x: x[1])
endtime = LR[0][1]
count = 1
for  i in range(1,N):
    s,e = LR[i]
    if endtime <= s:
        endtime = e
        count +=1
print(count)
