N = int(input())
S = input()

kakko = 0
ans = list(S)
for i in range(N):
    if S[i] == '\"':
        kakko += 1
    else:
        if kakko %2 == 1:
            continue
        else:
            if S[i] ==',':
                ans[i] = '.'
    
print(''.join(ans))    
    