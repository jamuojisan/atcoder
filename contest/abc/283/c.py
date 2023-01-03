S = input()
ans = 0
i = 0

while(i<len(S)):
    if i <= len(S) -2 and S[i] == '0' and S[i+1]=='0':
        ans +=1
        i +=2
    else:
        ans +=1
        i +=1
print(ans)