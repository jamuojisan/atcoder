H, W = map(int ,input().split())
G = [input() for _ in range(H)]

visited = set()
y, x = 0,0
ny, nx = 0, 0
while(1):
    if (y,x) in visited:
        print(-1)
        exit()
    visited.add((y,x))
    
    if G[y][x] == 'U':
        ny -= 1
    elif G[y][x] == 'D':
        ny += 1
    elif G[y][x]== 'L':
        nx -= 1
    else:
        nx += 1
    if not(0<=ny <H and 0<=nx<W):
        print(y+1, x+1)
        exit()
    y, x= ny, nx
    

    
    
    


