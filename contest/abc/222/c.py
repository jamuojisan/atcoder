N, M = map(int, input().split())

A = [input() for _ in range(2*N)]
GCP2n = {'C':0,'G':1,'P':2}

r2p = {i:i for i in range(2*N)}
p2w = {i:0 for i in range(2*N)}
w2p = {i:set() for i in range(M+1)}

for i in range(2*N):
    w2p[0].add(i)

for i in range(M):

    for j in range(N):
        p1, p2 = r2p[2*j], r2p[2*j + 1]
        c1, c2 = A[p1][i], A[p2][i]
        c1, c2 = GCP2n[c1], GCP2n[c2]
        w1, w2 = p2w[p1], p2w[p2]

        if abs(c1-c2)==1:
            if c1 > c2:
                p2w[p1] +=1
                w2p[w1].remove(p1)
                w2p[w1+1].add(p1)
            else:
                w2p[w2].remove(p2)
                w2p[w2+1].add(p2)
                p2w[p2] +=1
        elif abs(c1-c2)==2:
            if c1 < c2:
                p2w[p1] +=1
                w2p[w1].remove(p1)
                w2p[w1+1].add(p1)
            else:
                p2w[p2] +=1
                w2p[w2].remove(p2)
                w2p[w2+1].add(p2)
    count = 0
    for w in sorted(w2p, reverse=True):
        for p in sorted(w2p[w]):
            r2p[count] = p
            count+=1

for i in range(2*N):
    print(r2p[i] + 1)
