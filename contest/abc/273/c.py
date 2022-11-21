n = int(input())
a = list(map(int, input().split()))
b = sorted(list(set(a)))
ans = {i: 0 for i in range(n)}
for i in range(n):
    val = a[i]
    ok = len(b)
    ng = -1
    
    while(ok - ng > 1):
        mid = (ok + ng)//2
        if b[mid] > val:
            ok = mid
        else:
            ng = mid
    ans[len(b)-ok] +=1
    
for i in range(n):
    print(ans[i])