from collections import deque
N = int(input())
A = [*map(int, input().split())]

ans = deque([A[0]])
tmp = A[0]
count = 1
count_list = deque([])
print(1)
for i in range(1,N):
    if A[i] == tmp:
        if count + 1 == A[i]:
            for _ in range(count):
                _ = ans.popleft()
            if len(count_list) != 0:
                tmp, count = count_list.popleft() 
            else:
                if i != N-1:
                    tmp = A[i+1]
                    count = 0
        else:
            ans.append(A[i])
            count += 1

    else:
        ans.appendleft(A[i])
        count_list.appendleft([tmp,count])
        tmp = A[i]
        count = 1
    print(len(ans))

