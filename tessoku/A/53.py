import heapq
Q = int(input())
q = []

for i in range(Q):
    query = input().split()
    if query[0] == '1':
        heapq.heappush(q,int(query[1]))
    elif query[0] == '2':
        print(q[0])
    else:
        _ = heapq.heappop(q)