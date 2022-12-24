# メモリ超過厳しい
B = [*map(int, input().split())]
B2index = {str(j):str(i) for i, j in enumerate(B)}
index2B = {str(i):str(j) for i, j in enumerate(B)}
N = int(input())
A = [int(input()) for _ in range(N)]
AA = []
for i in A:
    j = str(i).zfill(9)
    tmp = []
    for k in range(len(j)):
        tmp.append(B2index[j[k]])
    AA.append(''.join(tmp))
AA = sorted(AA)
del A
ans = []
for i in AA:
    tmp = []
    for k in range(len(i)):
        tmp.append(index2B[i[k]])
    tmp2 = ''.join(tmp)
    zeroindex = 0
    while(zeroindex < 9 and tmp2[zeroindex] == '0'):
        zeroindex += 1
    
    ans.append(''.join(tmp2[zeroindex:]))
for i in ans:
    print(i)
