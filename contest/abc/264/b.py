R, C = map(int, input().split())
R, C = R-8, C-8
if abs(R) == abs(C):
    if abs(R) %2==0:
        print('white')
    else:
        print('black')
else:
    if max(abs(R), abs(C)) %2 == 0:
        print('white')
    else:
        print('black') 