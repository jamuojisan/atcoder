import copy
H ,W, K = map(int, input().split())
C = [input() for _ in range(H)]

raw_count = 0
h_count = []
for h in range(H):
    count = 0
    for w in range(W):
        if C[h][w] == '.':
            count += 1
        else:
            raw_count += 1
    h_count.append(count)

ans = 0
for S in range(2**H):
    _ans = 0
    miss = set()
    for h in range(H):
        if (S >> h) & 1:
            miss.add(h)
            _ans += h_count[h]
    if len(miss) >K :
        continue
    if len(miss) == K:
        ans = max(_ans, ans)
        continue
    count_list = []
    for w in range(W):
        _count = 0
        for h in range(H):
            if h in miss:
                continue
            if C[h][w] == '.':
                _count += 1
        count_list.append(_count)
    count_list.sort()
    count_list.reverse()
    _ans += sum(count_list[:K-len(miss)])
    ans = max(ans, _ans)

print(ans + raw_count)