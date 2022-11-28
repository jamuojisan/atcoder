N = int(input())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(S[-1] + A[i])
Q = int(input())
for _ in range(Q):
    l , r= map(int, input().split())
    l ,r = l-1, r-1
    if (r-l +1) - (S[r+1] - S[l]) < (S[r+1] - S[l]) :
        print('win')
    elif  (r-l +1) - (S[r+1] - S[l]) > (S[r+1] - S[l]):
        print('lose')
    else:
        print('draw')
    