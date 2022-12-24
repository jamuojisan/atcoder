n, m = map(int, input().split())
G = {}
for _ in range(m):
    u,v = map(int, input().split())
    u, v = u-1, v- 1
    if u not in G:
        G[u]=[v]
    else:
        G[u].append(v)
    if v not in G:
        G[v] = [u]
    else:
        G[v].append(u)
count = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i not in G or j not in G or k not in G:
                continue
            if  j in set(G[i]) and k in set(G[j]) and i in set(G[k]):
                count +=1
print(count)