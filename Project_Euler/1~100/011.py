S = []
for i in range(20):
    S.append(list(map(int, input().split())))

max = 1
print(S)
exit()
initial = S[0][0] * S[0][1] * S[0][2] * S[0][3]
for i in range(20):
    for j in range(17):
        print(1)