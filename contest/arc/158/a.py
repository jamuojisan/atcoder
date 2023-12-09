import math
def ext_euclid(a, b):
    xs = a, 1, 0
    ys = b, 0, 1
    while ys[0] != 0:
        q, z = divmod(xs[0], ys[0])
        xs, ys = ys, (z, xs[1] - q * ys[1], xs[2] - q * ys[2])
    return xs

T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    if (x+y+z) %3 != 0:
        print(-1)
    else:
        k = (x+y+z)//3
        mx = x+y+z
        val = 0
        while(1):
            s = val
            zz = k + 5*val
            if zz >= mx:
                break
            val += 1
        print(val)
