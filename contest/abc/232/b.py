alphabet = 'abcdefghijklmnopqrstuvwxyz'

S = input()
T = input()
if len(S) != len(T):
    print('No')
    exit()
a2i = {s:i for i, s in enumerate(list(alphabet))}
dis = [[0]*(26) for i in range(26)]
for i in range(26):
    for j in range(26):
        dis[i][j] = (i-j)%26
flg = True
d = dis[a2i[S[0]]][a2i[T[0]]] 
for i in range(1, len(S)):
    s, t  =S[i], T[i]
    if d != dis[a2i[s]][a2i[t]]:
        print('No')
        exit()
print('Yes')
    
