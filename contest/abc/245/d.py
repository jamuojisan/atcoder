N, M = map(int , input().split())
A = [*map(int,input().split())]
C = [*map(int, input().split())]

# (\sum_{k=0 -> N} A(k)x^k)(\sum_{k=0 -> M} B(k)x^k) = \sum_{l=0 -> N+M}\sum_{i=0 ->l} A(i)B(l-i)x^k 
# C(k) = \sum_{i=0 -> k}A(i)B(k-i)
# B(M) = C[N+M]//A[N]
# C(N+M-1) = B(M)A(N-1) + B(M-1)A(N) -> B(M-1)=(C[N+M-1] - B[M]A[N-1])//A[N-1]
# C(N+M-2) = B(M)A(N-2) + B(M-1)A(N-1) + B(M-2)A(N-2) -> B(M-2) = (C(N+M-2) - B(M)A(N-2) -B(M-1)A(N-1))//A(N-2)

ans = []
ans.append(C[N+M]//A[N])
for index, m in enumerate(reversed(range(M))):
    tmp = C[N+ m]
    print(index, tmp)
    for i in range(index+1):
        tmp -= ans[-i-1]*A[N-i+1]
        print(tmp)
    tmp //= A[N-index-1]
    ans.append(tmp)
print(*ans[::-1])