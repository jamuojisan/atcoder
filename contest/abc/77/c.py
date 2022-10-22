n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))

def judge(loc, val, z):
    if z[loc] <= val:
        return True
    else:
        return False


def bserch(val, type):
    ok = 0
    ng = n
    while(ng -ok > 1):
        mid = (ng+ok)//2
        
        if type == 'a':
            if judge(mid, val,a):
                ok=mid
            else:
                ng = mid
        else:
            if judge(mid, val,c):
                ok = mid
            else:
                ng = mid
    print( ok )
    if type  == 'c':
        if ok == 0:
            if c[ok] > val:
                return n
            else:
                return n-1
        else:
            return max(n-ok-1, 0)
    else:
        if a[ok] == val:
            return max(ok,0)
        else:
            return max(ok+1,0)

ans = 0
for i in b:
    a_kosu = bserch(i, 'a')
    c_kosu = bserch(i, 'c')
    ans += a_kosu*c_kosu
print(ans)