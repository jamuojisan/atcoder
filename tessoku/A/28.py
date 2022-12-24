N = int(input())

num = 0
mod = 10000
for _ in range(N):
    t, a = map(str,input().split())
    if t == '+':
        num += int(a)
    elif t == '-':
        num -= int(a)
    else:
        num *= int(a)
    num %= mod
    print(num)