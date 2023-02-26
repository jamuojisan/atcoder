from time import time
import sys
from collections import deque


# 定数たち：入力は捨ててglobalに定義
N: int = 100
K: int = 8
H: int = 50
W: int = 50
T: int = 2500
INF: int = 10000

TIME_LIMIT = 3900
START = time()

di = (0, -1, 0, 1)
dj = (-1, 0, 1, 0)
dir = "LURD"

# 関数
def eprint(*args, **kwargs):
    """標準エラー出力に出力するprint"""
    print(*args, file=sys.stderr, **kwargs)


def getTime():
    return (time() - START) * 1000


def find_start_pos(map_id: int, Maps: list):
    if map_start_pos[map_id] != None:
        return map_start_pos[map_id]

    for i in range(H):
        for j in range(W):
            if Maps[map_id][i][j] == "@":
                map_start_pos[map_id] = (i, j)
                return (i, j)
    eprint("Start position is not found.")
    return (-1, -1)


def bfs(map_id):
    score = 0
    dist = [[-1] * W for _ in range(H)]
    x, y = find_start_pos(map_id, _Maps)
    dist[x][y] = 0
    que = deque([(x, y)])
    for dx, dy in zip(di, dj):
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[nx][ny] != -1:
            continue
        if _Maps[map_id][nx][ny] in "x#":
            continue
        dist[nx][ny] = dist[x][y] + 1
        score += 1
    return score


class state:
    def __init__(
        self,
        subScore: int,
        totalScore: int,
        XY: list,
        history: str,
        used: list,
        previous: int,
    ):
        self.subScore = subScore  # 1回の行動の評価値
        self.totalScore = totalScore  # 今までの行動の評価値の合計
        self.XY = XY  # 各マップにおける座標(x,y)
        self.history = history  # 今までの行動履歴
        self.used = used  # 各マップにおける訪問済みのセル（高速化のため、x*50+yの整数をbit管理）
        self.previous = previous  # １つ前の行動を0~3で表現

    def debug(self):
        eprint(self.subScore, self.totalScore, self.history)


# ビームサーチを行う関数
def beam_search(XY):
    WIDTH = 160
    used = [0] * K
    beams = [state(0, 0, XY, "", used, -1)]

    # ビームサーチ
    for i in range(T):
        next_beam = []
        for beam in beams:
            for d in range(4):
                # 来た方向には戻らない
                if beam.previous == (d + 2) % 4:
                    continue
                score = 0
                _XY = beam.XY[:]
                _used = beam.used[:]
                isWall = False
                for map_id in range(K):
                    cx, cy = beam.XY[map_id]
                    # 　現在地が地雷か壁だとスキップ
                    if Maps[map_id][cx][cy] in "x#":
                        continue
                    nx = cx + di[d]
                    ny = cy + dj[d]
                    # 　移動先が盤面外だとスキップ
                    if not (0 <= nx < H and 0 <= ny < W):
                        continue
                    np = Maps[map_id][nx][ny]
                    bit = nx * H + ny
                    if np == "#":
                        isWall = True
                    elif np == "x":
                        score -= INF
                        _XY[map_id] = (nx, ny)
                        _used[map_id] |= 1 << bit
                    elif np == "o" and not ((_used[map_id] >> bit) & 1):
                        score += 100
                        _XY[map_id] = (nx, ny)
                        _used[map_id] |= 1 << bit
                    else:
                        score += 10
                        _XY[map_id] = (nx, ny)
                        _used[map_id] |= 1 << bit
                next_beam.append(
                    state(
                        score,
                        beam.totalScore + score,
                        _XY,
                        beam.history + dir[d],
                        _used,
                        d,
                    )
                )

        next_beam.sort(key=lambda s: -1 * s.totalScore)
        beams = next_beam[:WIDTH]

    return beams[0].history


# インプット
_ = input()
_Maps = [[input() for _ in range(H)] for _ in range(N)]

map_start_pos = [None] * N
cand = []
for i in range(N):
    score = bfs(i)
    cand.append((score, i))
cand.sort(reverse=1)
XY = [None] * K
Maps = [None] * K
choiced_map = [i for _, i in cand[:K]]
for i, map_id in enumerate(choiced_map):
    XY[i] = find_start_pos(map_id, _Maps)
    Maps[i] = [j[:] for j in _Maps[map_id]]


output = beam_search(XY)


# アウトプット
print(*choiced_map)
print("".join(output))
print(getTime(), file=sys.stderr)
