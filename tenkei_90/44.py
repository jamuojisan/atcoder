n,q = map(int, input().split())
a = list(map(int, input().split()))

indent = 0

for _ in range(q):
    t, x, y = map(int, input().split())
    x = x -indent -1 
    y = y-indent -1 
    if t == 1:
        a[x], a[y] = a[y], a[x]
    elif t == 2:
        indent += 1
        indent %= n
    else:
        print(a[x])


    

