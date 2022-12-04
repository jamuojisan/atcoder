T = int(input())
N = int(input())

imos = [0] * (2*T + 2)
for i in range(N):
    l , r = map(int, input().split())
    imos[2*l] += 1
    imos[2*r+1] -= 1
    
S = [0]
for i in range(2*T+2):
    S.append(S[-1]+imos[i])

for i in range(1, T+1):
    print(S[2*i])