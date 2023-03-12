x, y =map(int,input().split())
import math


def f1(s):
    return  x/(math.cos(s*math.pi/180) + math.cos((120-s)*math.pi/180))

def f2(s):
    return  y/(math.cos(s*math.pi/180) + math.cos((120-s)*math.pi/180))
 
#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(l<=r)
fr = 0.00000001
to = 179.99999
 
while(to - fr>1):
    mid = (fr +to)//2
    if f1(mid) - f1(mid-1) < 0:
        fr = mid
    else:
        to = mid

fr2 = 0.00000001
to2 = 179.99999
 
while(to2 - fr2>1):
    mid = (fr2 +to2)//2
    if f2(mid) - f2(mid-1) < 0:
        fr2 = mid
    else:
        to2 = mid
print(max(x/(math.sin(15*math.pi/180) + 1/math.sqrt(2)), y/(math.sin(15*math.pi/180) + 1/math.sqrt(2)), f1(fr), f2(fr2)))