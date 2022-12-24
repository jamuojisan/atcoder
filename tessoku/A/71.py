N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 0
for a, b in zip(A, reversed(B)):
    ans += a*b
print(ans)    
