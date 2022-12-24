S = []

for _ in range(9):
    S.append(input())

pone = []

for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            pone.append([i,j])

for i, j in pone:
    for k, l in pone:
        