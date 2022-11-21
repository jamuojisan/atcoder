N, Q = map(int, input().split())
s = input()

c = [] # c[i] iとi+1 文字がACかどうか
for i in range(N-1):
    if s[i] == 'A' and s[i+1] == 'C':
        c.append(1)
    else:
        c.append(0)
S= [0] # 
for i in range(N-1):
    S.append(S[-1] + c[i])

for _ in range(Q):
    l ,r  = map(int, input().split())
    print(S[r-1] - S[l-1])