Q = int(input())
table = set()
for i in range(Q):
    q,x=map(int, input().split())
    if q == 1 :
        table |= {x}
    elif q == 2 :
        table -= {x}
    else:
        print(min([l for l in table if l>=x] or [-1]))