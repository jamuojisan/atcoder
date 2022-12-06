import sys
sys.setrecursionlimit(10**7)
def dfs(val):
    
    if len(val) == 10:
        ans.add(val)
        return
    else:
        dfs(val+'4')
        dfs(val+'7')


N = int(input())
ans = set()
dfs('4')
dfs('7')

print(sorted(ans)[N-1])