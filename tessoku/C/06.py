N = int(input())

print(N)
for i in range(N):
    if i+2 >N:
        print(i+1, 1)
    else:
        print(i+1, i+2)