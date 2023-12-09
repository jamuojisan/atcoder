def wrap(ps):
  # ギフト包装法を使って凸包を求める。
  # 各点[x, y]をリストとして与えると凸包の各点をリストとして返す。
  qs = []
  # 最初の点
  x = [p[0] for p in ps]
  min_i = x.index(min(x))
  qs.append(ps[min_i]) # xが最小になる点をqs[0]とする。
  # 各点
  n = -1
  while True:
    n += 1
    for i in range(len(ps)):
      flag = False
      for p1 in ps:
        if qs[n] == ps[i]:
          flag = True
          break
        result = gaiseki(qs[n], ps[i], p1)
        if result > 0 : # left
          flag = True
          break
      if flag == False:
        this_i = i
    if ps[this_i] == qs[0]:
      break
    qs.append(ps[this_i])
  return qs

def gaiseki(moto, saki0, saki1):touch 
  # moto->saki0 の直線に対し saki1がどちら側にあるか
  # >0 ならば 左側 <0 ならば 右側
  x0 = saki0[0] - moto[0]
  y0 = saki0[1] - moto[1]
  x1 = saki1[0] - moto[0]
  y1 = saki1[1] - moto[1]
  gaiseki = x0 * y1 - x1 * y0
  return gaiseki
