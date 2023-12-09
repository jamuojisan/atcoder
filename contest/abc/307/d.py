N = int(input())
S = input()
from collections import deque
left = deque()
right = deque()

for i in range(N):
    if S[N - 1 - i] == '(':
        left.append(N-1-i)
    if S[N-i-1] == ')':
        right.append(N-i-1)
print(left, right)
flg = True
if len(left) >0:
    l = left.popleft()
else:
    flg =False
if  len(right) >0:
    r = right.popleft()
else:
    flg = False
done = '1'*N
while(flg):
    if r > l:
        print(l,r)
        done = done[:l] + '0'*(r-l+1) + done[r+1:] 
        if len(left) > 0 and len(right) >0:
            l = left.popleft()
            r = right.popleft()
        else:
            break
    else:
        if len(left)>0:
            l = left.popleft()
        else:
            break
print(done)
for d, i in enumerate(list(done)):
    if int(i):
        print(S[d], end='')
print()
        
        
            

