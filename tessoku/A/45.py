N ,C = map(str,input().split())
N = int(N)
A = input()

score = 0
for i in range(N):
    if A[i] =='W':
        score += 0
    elif A[i] == 'B':
        score += 1
    else:
        score += 2

if score%3 == 0:
    ans = 'W'
elif score%3 ==1 :
    ans = 'B'
else:
    ans = 'R'

if ans == C:
    print('Yes')
else:
    print('No')
