N = int(input())
A = list(map(int, input().split()))
count = [0]*(100)
for i in A:
    count[i%100] += 1
ans = 0
ans += count[0]*(count[0]-1)//2
ans += count[50]*(count[50]-1)//2

for i in range(1,50):
    ans += count[i]*count[(100-i)]
print(ans)
