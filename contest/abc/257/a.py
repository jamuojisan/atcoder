n , x = map(int, input().split())
string ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvrxyz'
ans = ''
for i in string:
    s = ''.join([i]*n)
    ans+=(s)
print(ans[x-1])