import sys 
sys.setrecursionlimit(10**7)
n = int(input())

length = len(str(n))
keta = []
for i in range(60):
    if n & (1 << i):
         keta.append(1)
    else:
        keta.append(0)
ans = []


def dfs(val, depth):
    if depth == 60:
        ans.append(val)
        return
    if keta[depth] == 1:
        dfs(val+2**(depth), depth+1)
    dfs(val, depth+1)

dfs(0, 0)   
for i in sorted(ans):
    print(i)