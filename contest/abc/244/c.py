N = int(input())
ans = set([i for i in range(1, 2*N+2)])

while(1):
    _ans = ans.pop()
    print(_ans, flush=True)
    if len(ans) == 0:
        print(0, flush=True)
        exit()
    l = int(input())
    ans.remove(l)
    