N ,K = map(int, input().split())
S = input()

one = 0
zero = 0

for i in range(N):
    if S[i] == '1':
        one += 1
    else:
        zero += 1

if (one - K >= 0 and (one-K) %2 == 0) or (K - one) %2 == 0:
    print('Yes')
else:
    print('No')