n, m = map(int, input().split())

def dfs(A):
    if len(A) == n:
        print(*A)
        return
    
    if len(A) == 0:
        start = 1
    else:
        start = A[-1] + 1
    for i in range(start, m+1):
        dfs(A + [i])

dfs([])    

