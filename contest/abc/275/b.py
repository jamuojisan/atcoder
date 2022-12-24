a, b,c, d, e, f = map(int, input().split())
mod =  998244353

ans = (((a *b) % mod ) *c ) %  mod  -  (((d *e) % mod ) *f ) %  mod
ans %= mod 
print(ans) 