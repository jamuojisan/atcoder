N = int(input())
S = input()

b =0
r =0
_b = 0
_r = 0
for i in range(N):
    if S[i] == 'B':
        _b +=1
        r = max(r,_r)
        _r = 0
    else:
        _r += 1
        b = max(b, _b)
        _b = 0
b = max(_b, b)
r = max(_r, r)
if b >=3 or r >=3:
    print('Yes')
else:
    print('No') 
