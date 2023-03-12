N, K = map(int, input().split())
S = input()

T = ''
count = 0
for i, s in enumerate(S):
    if s == 'o' and count <K:
        T += 'o'
        count +=1
    else:
        T+='x'

print(T)
        