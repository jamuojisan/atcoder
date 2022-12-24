n = int(input())
a = list(map(int, input().split()))

even = []
odd = []

for i in range(n):
    if a[i] %2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
even.sort()
odd.sort()

if len(even) <2 and len(odd) < 2:
    print(-1)
elif len(even) < 2:
    print(odd[-1] + odd[-2])
elif len(odd) < 2:
    print(even[-1] + even[-2])
else:
    print(max(even[-1] + even[-2], odd[-1] + odd[-2]))
    
