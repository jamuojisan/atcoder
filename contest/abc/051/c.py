sx, sy, tx, ty = map(int, input().split())
ans = 'U'*(ty-sy) + 'R'*(tx-sx) +'D'*(ty-sy) +'L'*(tx-sx+1) +'U'*(ty-sy +1) + 'R'*(tx-sx + 1) +'D' +'R' +'D'*(ty-sy+1) +'L'*(tx-sx+1) + 'U'
print(ans)
