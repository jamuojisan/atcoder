import sys
sys.setrecursionlimit(10**7)
n = int(input())
child = [[] for _ in range(n)]

for i in range(n-1):
    i = i + 1
    boss = int(input())
    boss = boss - 1
    child[boss].append(i)


def dfs(i):
    if len(child[i]) == 0:
        return 1
    else:
        buka = []
        for j in child[i]:
            buka.append(dfs(j))
        return max(buka) + min(buka) + 1

print(dfs(0))