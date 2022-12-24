from collections import deque
N, X = map(int, input().split())
A = list(input())

X = X-1
q = deque([X])
while(len(q)):
    v = q.popleft()
    A[v] = '@'
    if v +1 < N and A[v+1] == '.':
        q.append(v+1)
    if v-1 >=0 and A[v-1] == '.':
        q.append(v-1)
print(''.join(A))