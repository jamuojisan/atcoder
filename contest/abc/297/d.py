import math
A, B =map(int ,input().split())
if A == B:
    print(0)
    exit()
if A<B :
    A, B =B,A
count = 0
while(1):
    diff = A- B
    if diff == 1:
        count += B
        break
    if diff//B == 0 or diff//B == 1:
        count += 1
        A = A - B
    else:    
        count += diff//B
        A = A - (diff//B)*B 
    if A < B:
        A, B = B,A
    if A ==B:
        break
print(count)