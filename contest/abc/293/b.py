N= int(input())
A = list(map(int ,input().split()))
ans = []
done = [True]*N
for j, i in enumerate(A):
    if done[j]:
        done[i-1] = False
for i, f in enumerate(done):
    if f:
        ans.append(i+1)

print(len(ans))
print(*ans)
    