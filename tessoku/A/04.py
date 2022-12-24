N = int(input())
ans = ''
for i in range(10):
    if N & (1 << i):
        ans += '1'
    else:
        ans += '0'
print(ans[::-1])