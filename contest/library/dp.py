# ! DPコンテスト

# ! G（最長長さ。有向グラフに関するDP）
# from collections import defaultdict
# import sys
# sys.setrecursionlimit(10**7)
# n, m = map(int, input().split())
# G = defaultdict(list)
# indeg = [0]*n
# for _ in range(m):
#     x, y = map(int, input().split())
#     x, y = x-1, y-1
#     G[x].append(y)
#     indeg[y] += 1

# done = [False] * n
# length = [0] * n

# def dfs(i):
#     if done[i]:
#         return length[i]
    
    
#     for j in G[i]:
#         length[i] = max(length[i], dfs(j) + 1)
#     done[i] = True
#     return length[i]

# for i in range(n):
#     if indeg[i] == 0:
#         dfs(i)

# print(max(length))

# ! 巡回セールスマン問題
n = int(input())
dis = []

for _ in range(n):
    dis.append(list(map(int, input().split())))

inf = 10 ** 20
dp = [[inf]*(n) for _ in range(2**n)] # dp[n][i] すでに訪れた都市の集合nがあって、最後にいる都市がiのときの合計コストの最小値
dp[0][0] = 0 # 最初の出発地は都市0

for n in range(2**N):
    # iからjへの遷移をしらべる
    for i in range(N):
        for j in range(N):
            # iに未訪問ならスキップ
            if n != 0 and not n &(1<<i):
                continue
            # jを訪問済みならスキップ
            if  n & (1 << j) or i == j:
                continue
            dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i] + dis[i][j])

print(dp[2**n-1][0])

# 尺取り法

N, K = map(int ,input().split())
A = [*map(int, input().split())]
right = 0
ans = 0
count  = {}
f = set()
for left in range(N):
    while(right < N  and  ( (A[right] not in f and (len(f) +1 <= K)) or (A[right] in f))) :
        if A[right] in count:
            count[A[right]] += 1
        else:
            count[A[right]] = 1
        f.add(A[right])
        right += 1
    ans = max(right-left, ans)
    if right == left:
        right +=1
    else:
        if A[left] in f:
            count[A[left]] -= 1
            if count[A[left]] == 0:
                f.remove(A[left])
    if right == N:
        break
print(ans)