N,X,Y,Z = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
score = []
for i in range(N):
    score.append([i,A[i],B[i], A[i]+B[i]])
ans = []

score1 = sorted(score, key = lambda x: x[1],reverse=True)
for i in range(X):
    ans.append(score1[i][0]+1)

score2 = sorted(score, key = lambda x: x[2], reverse=True)
for i in range(N):
    if Y == 0:
        break
    if score2[i][0]+1 in set(ans):
        continue
    ans.append(score2[i][0]+1)
    Y -= 1

score3 = sorted(score, key = lambda x: x[3],reverse=True)

for i in range(N):
    if Z == 0:
        break
    if score3[i][0]+1 in set(ans):
        continue
    ans.append(score3[i][0]+1)
    Z -= 1
for i in sorted(ans):
    print(i)

     