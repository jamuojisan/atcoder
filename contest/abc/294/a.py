# S= input()
N = int(input())
# N, M = map(int ,input().split())
A = list(map(int ,input().split()))

ans = []
for i in A:
    if i%2 == 0:
        ans.append(i)
print(*ans)