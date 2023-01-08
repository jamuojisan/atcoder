N = int(input())
A = [*map(int, input().split())]
for i in range(2001):
    if i not in set(A):
        print(i)
        exit()