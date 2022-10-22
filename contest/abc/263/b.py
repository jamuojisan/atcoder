n = int(input())
a = list(map(int, input().split()))

cnt = 0
parent = 1
for i in range(n-1):
    if a[i] == parent:
        cnt +=1
        parent  = 2+i
print(cnt)