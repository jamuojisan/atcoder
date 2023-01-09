class round: # 一回の操作を表す構造体
    def __init__(self, p, q, r):
        self.p = p
        self.q = q
        self.r = r

class State:
    def __init__(self, N):
        self.score = 0 # 暫定スコア
        self.x = [0]*N # 配列
        self.lastmove = '?' #最後の動き 初期状態では'?'に
        self.lastpos = -1 # Beam[i-1][どこ]から遷移したか. 初期状態では-1に



def BeamSearch(N, T, rounds):
    # ２次元配列beamを用意し、0手目の状態を設定
    WIDTH = 300
    beam = [[] for _ in range(T+1)]
    beam[0].append(State(N))
    
    # ビームサーチ
    import copy
    for i in range(T):
        candidate = []
        for j in range(len(beam[i])):
            # 操作Aの場合
            sousa_a = copy.deepcopy(beam[i][j])
            sousa_a.lastmove = 'A'
            sousa_a.lastpos = j
            sousa_a.x[rounds[i].p] += 1
            sousa_a.x[rounds[i].q] += 1
            sousa_a.x[rounds[i].r] += 1
            sousa_a.score += sousa_a.x.count(0) # sousa_a.xに含まれる0の個数をカウント
            
            # 操作Bの場合
            sousa_b = copy.deepcopy(beam[i][j])
            sousa_b.lastmove = 'B'
            sousa_b.lastpos = j
            sousa_b.x[rounds[i].p] -= 1
            sousa_b.x[rounds[i].q] -= 1
            sousa_b.x[rounds[i].r] -= 1
            sousa_b.score += sousa_a.x.count(0) # sousa_a.xに含まれる0の個数をカウント
            
            # 候補に追加
            candidate.append(sousa_a)
            candidate.append(sousa_b)
        # ソートして、beam[i+1]の結果を計算する
        candidate.sort(key=lambda s: -s.score)
        beam[i+1] = copy.deepcopy(candidate[:WIDTH]) #多くとも candidateの上位WIDTH件記録する
    # ビームサーチの復元
    current_place = 0
    answer = [None] * T
    for i in range(T, 0, -1):
        answer[i-1] = beam[i][current_place].lastmove
        current_place = beam[i][current_place].lastpos
    return answer
    


# 入力
T = int(input())
rounds = [None]*T
for i in range(T):
    p, q, r = map(int, input().split())
    rounds[i] = round(p-1, q-1, r-1)

answer = BeamSearch(20, T, rounds)

# 出力
for c in answer:
    print(c)
    