def fib(a, b):
    global ans
    if (a+ b) % 2 == 0:
        ans += a+b
    if a + b > 4000000:
        print(ans)
    else:
        fib(b, a+b)

ans = 2
fib(1, 2)