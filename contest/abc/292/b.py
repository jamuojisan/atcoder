N , Q = map(int, input().split())
card = {i:0 for i in range(N)}

for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        card[x-1] = min(2, card[x-1] + 1)
    elif q == 2:
        card[x-1] = 2
    else:
        if card[x-1] == 2:
            print('Yes')
        else:
            print('No')