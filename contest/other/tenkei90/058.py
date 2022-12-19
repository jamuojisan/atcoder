N, K = map(int, input().split())

mod = 10**5
while(len(str(N)) >= 1 and K>=1):
    N = N +  sum([int(i) for i in list(str(N))])
    N %= mod
    K -= 1
    print(N,K)
print(N)

