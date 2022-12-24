N = int(input())
A = [*map(int,input().split())]
zero = [0]*31
one = [0]*31

for a in A:
    t = bin(a)[2:].zfill(31)
    for i in range(31):
        if t[i] == '1':
            one[-i] +=1
        else:
            zero[-i] +=1

x = 0
for i in range(31):
    if zero[i] <= one[i]:
        x += 2**i
B = []
for a in A:
    B.append(a^x)

print(max(B))

