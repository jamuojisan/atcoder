n = int(input())
s = list(input())
w = list(map(int, input().split()))
ws = sorted([[_w,_s] for _w, _s in zip(w, s)])
import copy

ans = 0
for i in range(n):
    _s = int(s[i])
    ans += _s

anns = copy.copy(ans)
for i in range(n):
    _w, _s = ws[i]
    if  _s == '0':
        ans += 1
    else:
        ans -= 1
    if(i < n-1):
        if(ws[i][0] != ws[i+1][0]): 
            anns = max(anns, ans)
    else:
        anns = max(anns, ans)
        
print(anns)

