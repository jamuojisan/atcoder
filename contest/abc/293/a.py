# N = int(input())
S = list(input())
# A, B =map(int, input().split())
# X = list(map(int ,input().split()))
ans = []
for i in range(len(S)//2):
    ans.append(S[2*i+1])
    ans.append(S[2*i])
print(''.join(ans))
