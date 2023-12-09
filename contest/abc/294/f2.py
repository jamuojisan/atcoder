import heapq

def calculate_concentration(sugar, water):
    return 100 * sugar / (sugar + water)

n, m, k = map(int, input().split())

# 高橋君の砂糖水を入力し、濃度が高い順にソートする
takasugi = []
for i in range(n):
    a, b = map(int, input().split())
    takasugi.append((calculate_concentration(a, b), a, b))
takasugi.sort(reverse=True)

# 青木君の砂糖水を入力し、濃度が高い順にソートする
aoki = []
for i in range(m):
    c, d = map(int, input().split())
    aoki.append((calculate_concentration(c, d), c, d))
aoki.sort(reverse=True)

# 濃度が高い順に上位K個の高橋君の砂糖水を選ぶ
takasugi = takasugi[:k]

# 濃度が高い順に上位K個の青木君の砂糖水を選ぶ
aoki = aoki[:k]

# K番目に濃度が高い砂糖水の濃度を求める
heap = []
heapq.heappush(heap, (-takasugi[0][0]-aoki[0][0], 0, 0))
used = set((0, 0))
for i in range(k):
    ans, idx_t, idx_a = heapq.heappop(heap)
    print(-ans)
    if i == k - 1:
        break
    if idx_t + 1 < len(takasugi) and (idx_t + 1, idx_a) not in used:
        heapq.heappush(heap, (-(takasugi[idx_t+1][0]+aoki[idx_a][0]), idx_t+1, idx_a))
        used.add((idx_t+1, idx_a))
    if idx_a + 1 < len(aoki) and (idx_t, idx_a+1) not in used:
        heapq.heappush(heap, (-(takasugi[idx_t][0]+aoki[idx_a+1][0]), idx_t, idx_a+1))
        used.add((idx_t, idx_a+1))
