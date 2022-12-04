def f(x):
    return x**3 + x
N = int(input())

ok = 0
ng = 100

while(abs(ng-ok)>0.000000001):
    mid = (ok+ng)/2
    if f(mid) <= N:
        ok = mid
    else:
        ng = mid

print(ok)

