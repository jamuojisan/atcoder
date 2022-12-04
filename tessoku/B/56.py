mod = 2147483647

# 文字列の l～r 番目を前から読んだ時のハッシュ値を返す関数
def GetHashLeft(l: int, r: int) -> int:
	val = H[r] - powB[r - l + 1] * H[l - 1]
	return val % mod

# 文字列の l～r 番目を後ろから読んだ時のハッシュ値を返す関数
def GetHashRight(l: int, r: int) -> int:
	l, r = N + 1 - r, N + 1 - l
	val = IH[r] - powB[r - l + 1] * IH[l - 1]
	return val % mod

def hash_val(l , r, H):
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
IS = S[::-1]
H = [0]
IH = [0]
B = 100
powB = [1]
for i in range(N):
    powB.append(powB[-1]* 100 %mod)



for i in range(N):
    H.append((B*H[-1] + s2i[S[i]])%mod)
    IH.append((B*IH[-1] + s2i[IS[i]])%mod)
for i in range(Q):
    l, r = map(int, input().split())

    if GetHashLeft(l, r) == GetHashRight(l, r):
        print('Yes')
    else:
        print('No') 

