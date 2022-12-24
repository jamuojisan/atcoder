t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
S = input()
if S[0] in t and S[-1] in t and '100000' <= S[1:-1] <= '999999':
    print('Yes')
else:
    print('No')
    