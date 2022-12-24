n ,m, q = map(int, input().split())
lr = []
for _ in range(m):
    l, r = map(int, input().split())
    lr.append([l,r])
cnt = [0] # cmt[l][r] = 区間[l,r]の列車の台数


