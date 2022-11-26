def hash_val(l , r):
    return (H[r] - powB[r-l+1]*H[l-1])%mod

def Pow(n, k):
    ans = 1
    while k:
        if n % 2:
            ans = (ans * n ) % mod
        n = (n *n) %mod
        k >>= 1
    return ans
s2i = {j: i for i ,j in enumerate(list('abcdefghijklmnopqrstuvwxyz'))}
mod = 10 ** 9 +7

N, Q = map(int, input().split())
S = input()
H = [0]
B = 100
powB = [1]
for i in range(N):
    powB.append(powB[-1]* 100 %mod)



for i in range(N):
    H.append((B*H[-1] + s2i[S[i]])%mod)

for i in range(Q):
    a, b, c, d = map(int, input().split())

    if hash_val(a, b) == hash_val(c, d):
        print('Yes')
    else:
        print('No') 

