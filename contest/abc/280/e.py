def modinv(a, m):
    b = m
    u = 1
    v = 0
    while(b):
        t = a//b
        a -=t*b
        a,b = b,a
        u -= t*v
        u ,v = v,u
    u %= m
    if(u < 0):
        u +=m
    return u
# 与えたダメージの和がk以上になるまでに必要な攻撃回数の期待値をdp[k]
# ex. dp[0] = 0, dp[1] = 1, dp[2] = 2 - P/100
# dp[i+1] -dp[i]を考える。
# ダメージの総和がi以上になる攻撃回数とi+1になる攻撃回数は等しいか、後者が1多い
# 後者が1大きくなる確率をp[i]とすると
# dp[i+1] = dp[i] + p[i]*1

# ダメージの総和は狭義単調増加なので、
# 後者が１大きくなる　⇦⇨ ダメージの総和がちょうどiとなるタイミングがある
# ちょうどiになるタイミングが存在しない　⇦⇨ あるタイミングでダメージの総和がi-1かつその次の攻撃が２
# p[i] = 1 - p[i-1]*P/100
# p[0] =1 より、dp[N] = dp[N-1] + p[N-1] = dp[N-2] + p[N-2] + p[N-2] = ・・・ = dp[0] + \sum_{i:0->N-1} p[i] = \sum_{i:0->N-1} p[i]

# mod 998244353 については、100の逆元 100R≡1 mod 998244353 となるようなRを用いて
# p[i] ≡ 1 - p[i-1]*PR (mod 998244353) と書き直せば解ける。


N, P = map(int, input().split())
mod = 998244353
R = modinv(100,998244353)
p = [0]*(N+1)
p[0] = 1
for i in range(1,N+1):
    p[i] = 1 - p[i-1]*P*R
    p[i] %= mod

ans = 0
for i in range(N):
    ans += p[i]
    ans %= mod
print(ans)
