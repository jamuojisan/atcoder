import math
import random
import copy
N = int(input())
XY = [[*map(int, input().split())] for _ in range(N)]

dist = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    x1, y1 = XY[i]
    for j in range(N):
        if i == j:
            continue
        x2, y2 = XY[j]
        dist[i+1][j+1] = math.sqrt((x1-x2)**2 + (y1-y2)**2)
ans = [1]
score = 0
for _ in range(N-1):
    v = ans[-1]
    mn = 10**9
    nv = -1
    for i in range(1,N+1):
        if i in set(ans):
            continue
        if mn > dist[v][i]:
            mn = dist[v][i]
            nv = i
    ans.append(nv)
    score += mn
score += dist[ans[-1]][1]
ans.append(1)
# ここまで、貪欲法
#山登り法 + 焼きなまし法
for i in range(2*10**5):
    l = random.randint(1, N)
    r = random.randint(1, N)
    if l > r:
        l , r = r, l
    new_ans = ans[:l] +ans[l:r][::-1] + ans[r:]

    new_score = 0
    for i in range(N):
        new_score += dist[ans[i]][new_ans[i+1]]
    # T = 30.00 - 28.00*i/(2*10**5) # 焼きなまし温度。回数が増すにつれて、温度が下がるように設計。
    # P = math.exp(min(0, (score - new_score)/T))
    # if random.random() < P:
    if new_score <= score:
        ans =  new_ans[::]
        score = new_score

for i in ans:
    print(i)


