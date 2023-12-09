N = int(input())
A = list(map(int, input().split()))

A = sorted(set(A))[:-1]
print(A[-1])