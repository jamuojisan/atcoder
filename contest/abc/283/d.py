S = input()
ball = set()

for i in range(len(S)):
    if S[i] =='(':
        continue
    elif S[i] ==')':
        ball = set()
    else:
        if S[i] in ball:
            print('No')
            exit()
        else:
            ball.add(S[i])
print('Yes')