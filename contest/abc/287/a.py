N = int(input())
S = [input() for _ in range(N)]

c = 0
for i in range(N):
    if S[i] == 'For':
        c += 1

if c > N//2:
    print('Yes')
else:
    print('No')
    