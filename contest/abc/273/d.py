h,w, y0,x0 = map(int, input().split())
y0,x0 = y0-1, x0-1
n = int(input())
rc = []
from  collections import defaultdict
y_kabe = defaultdict(list)
x_kabe = defaultdict(list)
for _ in range(n):
    y, x = map(int,input().split())
    y, x = y-1 ,x-1
    y_kabe[y].append(x)
    x_kabe[x].append(y)

for i in range(n):
    if i in y_kabe:
        y_kabe[i].sort()
    if i in x_kabe:
        x_kabe[i].sort()


def binary_serch(lis, val, muki):
    if muki == 'l':
        ok = 0
        ng = len(lis)
    else:
        ok = len(lis)
        ng = 0
    while(abs(ok-ng) >1):
        mid = (ok+ng) //2
        if muki == 'l':
            if lis[mid] <= val:
                ok = mid
            else:
                ng = mid
        else:
            if lis[mid] >= val:
                ok = mid
            else:
                ng = mid

    return ok

q = int(input())
for i in range(q):
    d, l = map(str,input().split())
    l = int(l)
    if d == 'L' or d== 'R':
        if y0 in y_kabe: #入っていれば壁の有無を確認する必要あり
            if d == 'L':
                ind = binary_serch(y_kabe[y0],x0, 'l')
                x0  = y_kabe[y0][ind]+1
            else:
                ind = binary_serch(y_kabe[y0],x0, 'u')
                if ind >= len(y_kabe[y0]):
                    x0 = min(w-1, x0+l)
                else: 
                    x0 = y_kabe[y0][ind]- 1               
        else:
            if d == 'L':
                x0 = max(0, x0-l)
            else:
                x0 = min(w-1, x0+l) 
    else:
        if x0 in x_kabe: # 入ってれば壁の有無を確認する必要あり 
            if d == 'D':
                ind = binary_serch(x_kabe[x0],y0,'u')
                if ind >= len(x_kabe[x0]):
                    y0 = min(h-1, y0+l)
                else:
                    y0  = x_kabe[x0][ind]-1
            else:
                ind = binary_serch(x_kabe[x0],y0, 'l')
                y0 = x_kabe[x0][ind]+1               
        else:
            if d == 'D':
                y0 = min(h-1, y0+l) 
            else:
                y0 = max(0, y0-l)
    print(y0+1, x0+1)
        