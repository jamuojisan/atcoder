
while(1):
    n = int(input())
    if n == 0:
        exit()
    S = [0]*(3600*24+1)
    for _ in range(n):
        f ,e = map(str, input().split())
        h1, m1 ,s1 = int(f[:2]), int(f[3:5]), int(f[6:8])
        time1 = h1*3600 + m1*60 + s1        
        h2, m2 ,s2 = int(e[:2]), int(e[3:5]), int(e[6:8])
        time2 = h2*3600 + m2*60 + s2
        S[time1] +=1
        S[time2] -=1
    
    ans = [S[0]]
    for i in range(1,3600*24+1):
        ans.append(ans[-1] + S[i])
    
    print(max(ans))        
