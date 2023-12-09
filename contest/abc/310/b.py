N, M= map(int , input().split())
PCF = []
for _ in range(N):
    _PCF = [*map(int, input().split())]
    PCF.append(_PCF)

for i in range(N):
    set_i = set(PCF[i][2:])
    for j in range(N):
        if i == j:
            continue
        if PCF[i][0] < PCF[j][0]:
            continue
        set_j = set(PCF[j][2:])
        
        if not set_i.issubset(set_j):
            continue
        elif (PCF[i][0] > PCF[j][0]) or len(set_i) < len(set(PCF[j][2:])):
            print('Yes')
            exit()
print('No')
            
            