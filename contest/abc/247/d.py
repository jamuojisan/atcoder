from collections import deque
Q = int(input())

ans  = deque([])
nokori = 0
y = 0
for  _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1:]
        ans.append([x,c])
    else:
        c = query[1]
        if nokori -c >=0:
            print(y*c)
            nokori -= c
        else:
            total = y*nokori
            c -= nokori
            while(c>0):
                y, d = ans.popleft()
                if d >= c:
                    total += y*c
                    nokori = d-c
                    c = 0
                else:
                    total += y*d
                    c -= d
            print(total) 
