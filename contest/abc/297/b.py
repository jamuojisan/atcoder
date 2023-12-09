# N= int(input())
S= input()
# N , D = map(int ,input().split())
# T = list(map(int,input().split()))

b = []
k = []
r = []
for i in range(8):
    if S[i] == 'B':
        b.append(i+1)
    elif S[i] == 'R':
        r.append(i)
    elif S[i] =='K':
        k.append(i)
if b[0] %2 == b[1] %2:
    print('No')
    exit()

if r[0] < k[0] < r[1] or r[1] <k[0] <r[0]:
    print('Yes')
else:
    print('No')