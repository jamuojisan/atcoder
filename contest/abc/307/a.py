N = int(input())
A = list(map(int , input().split()))

for i in range(N):
    print(sum(A[7*i:7*(i+1)]), end =' ')
print()