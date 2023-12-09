def nim_sum(stones):
    nim_sum = 0
    for stone in stones:
        nim_sum ^= stone
    return nim_sum

def can_win(stones, L, R):
    if nim_sum(stones) == 0:
        # 先手太郎君が最初から勝利している場合
        return False
    for i in range(len(stones)):
        for j in range(L, R+1):
            if stones[i] >= j and nim_sum(stones[:i] + [stones[i]-j] + stones[i+1:]) == 0:
                # 先手太郎君がこの手を打てば勝利できる場合
                return True
    # どの山を選んでも相手が勝利できる場合
    return False



N, L, R = map(int, input().split())
A = list(map(int, input().split()))

if can_win(A, L ,R):
    print('First')
else:
    print('Second')