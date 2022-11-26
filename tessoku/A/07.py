D = int(input())
N = int(input())

presence = [0]*(D+1)

for q in range(N):
    l, r = map(int,input().split())
    l, r= l-1, r-1
    presence[l] +=1
    presence[r+1] -=1

S = [0]
for i in range(D+1):
    S.append(S[-1] + presence[i])
for i in range(1,D+1):
    print(S[i])