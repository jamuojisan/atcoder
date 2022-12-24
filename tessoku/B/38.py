N = int(input())
S = input()

# < を考えた時の下限値
streak1 = 1
ret1 = [0] * (N)
ret1[0] = 1
for i in range(N-1):
    if S[i] == 'A':
        streak1 += 1 
    else:
        streak1 = 1
    ret1[i+1] = streak1
# > を考えた時の下限値
streak2 = 1
ret2 = [0] * (N)
ret2[N-1] = 1
for i in reversed(range(N-1)):
    if S[i] == 'B':
        streak2 += 1 
    else:
        streak2 = 1
    ret2[i] = streak2


ans = 0
for i in range(N):
    ans += max(ret1[i], ret2[i])
print(ans)