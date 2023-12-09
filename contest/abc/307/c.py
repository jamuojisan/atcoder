def search_edge_black(C, H, W):
    
    leftmin = 100
    rightmax = 0
    upmin = 100
    downmax = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                leftmin = min(leftmin,j)
                rightmax = max(rightmax, j)
                upmin = min(upmin, i)
                downmax = max(downmax, i)
    return leftmin,rightmax, upmin,downmax
    

Ha, Wa = map(int, input().split())
A = [[*(map(int, input().split()))]  for _ in range(Ha)]

Hb, Wb = map(int, input().split())
B = [[*(map(int, input().split()))]  for _ in range(Hb)]

Hx, Wx = map(int, input().split())
X = [[*(map(int, input().split()))]  for _ in range(Hx)]


aleftmin, arightmax, aupmin, adownmax = search_edge_black(A, Ha, Wa)
bleftmin, brightmax, bupmin, bdownmax = search_edge_black(B, Hb, Wb)
xleftmin, xrightmax, xupmin, xdownmax = search_edge_black(X, Hx, Wx)

sample = ['.'*(xrightmax-xleftmin) for _ in range(xdownmax-xupmin)]
for i in range()
