S = []
for _ in range(100):
    S.append([int(i) for i in reversed(input())])
digit = []
for i in range(50):
    digit_val = 0
    for j in range(100):
        digit_val += S[j][i]
    digit.append(digit_val)
ans = [0] * 100
for i,j in enumerate(digit):
    count = 0
    while(j>0):
        print(i,count)
        ans[i+count] += j % 10
        j //= 10
        count +=1
for i in reversed(ans):
    print(i, end ='')
print(''.join([str(i) for i in ans[::-1][:10]] ))
print(digit)
print(ans)

        
