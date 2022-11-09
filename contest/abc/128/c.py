n, m = map(int, input().split())
s = []
for _ in range(m):
    _s = map(int, input().split())[1:]
    s.append(_s)
p = map(int, input().split())

ans = 0
for i in range(2**n):
    