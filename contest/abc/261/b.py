n = int(input())
S = []
for _ in range(n):
    S.append(input())

flag = True
for i in range(n):
    for j in range(i+1,n):
        if (S[i][j] == 'W' and S[j][i] == 'L') or (S[i][j] == 'L' and S[j][i] == 'W') or (S[i][j] == 'D' and S[j][i] == 'D'):
            continue
        else:
            print('incorrect')
            exit()
print('correct')
