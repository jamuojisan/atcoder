D = int(input())
X = int(input())
A = [int(input()) for _ in range(D-1)]
B =[X]
for i in A:
    B.append(B[-1] + i)

Q = int (input())
for i in range(Q):
    s ,t = map(int, input().split())
    s, t = s-1, t-1
    if B[s] == B[t]:
        print('Same')
    elif B[s] > B[t]:
        print(s+1)
    else:
        print(t+1)
