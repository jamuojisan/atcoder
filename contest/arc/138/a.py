import heapq
N ,K = map(int, input().split())
A = [*map(int, input().split())]
B = A[:K]
C = A[K:]
C = [-i for i in C]
ans = 0
initial_score = sum(B)
score = sum(B)

heapq.heapify(B)
heapq.heapify(C)
print(C)
while(len(C)):
    if score > initial_score + 1:
        print(ans)
        exit()
    mn = heapq.heappop(B)
    mx = heapq.heappop(C)
    heapq.heappush(B, -mx)
    score += (-mx - mn)
    ans +=1
print(-1)