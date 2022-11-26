from collections import deque
Q = int(input())
q = deque()

for i in range(Q):
    query = input()
    if query[0] == '1':
        q.append(query[2:])
    elif query[0] == '2':
        print(q[0])
    else:
        _ = q.popleft()