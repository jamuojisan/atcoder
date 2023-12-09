N = int(input())
S = [input() for _ in range(N)]
def check_kaibun(s):
    flg = True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
        
        
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if check_kaibun(S[i]+S[j]):
            print('Yes')
            exit()
print('No')