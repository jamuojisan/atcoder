n , m , q = map(int, input().split())
score = [n]*m
problem2person = {i:[] for i in range(1,m+1)}
person2problem = {i:[] for i in range(1,n+1)}
for i in range(q):

    query = list(map(int, input().split()))
    if query[0] == 1:
        ans  = 0
        for i in person2problem[query[1]]:
            ans += score[i-1]
        print(ans)
    else:
        problem2person[query[2]].append(query[1])
        person2problem[query[1]].append(query[2])
        score[query[2]-1] -=1