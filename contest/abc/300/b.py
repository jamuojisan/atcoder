H ,W = map(int ,input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        
        #確認部
        flg = True
        for k in range(H):
            for l in range(W):
                if A[(k+i)%H][((l+j)%W)] != B[k][l]:
                    flg =False
                    break
        if flg:
            print('Yes')
            exit()

print('No')
                
        
