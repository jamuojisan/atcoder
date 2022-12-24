import numpy as np
n , l , r = map(int, input().split())
a = np.array(list(map(int, input().split())))

S = [0]
s = 0
for i in a:
    s += i
    S.append(s)
min_val = -10**18
index = -1

for i in range(n):
    sub_sum = S[i+1]
    val = (i+1)*l
    if sub_sum - val > min_val:
        min_val = sub_sum - val
        index = i+1
if min_val < 0:
    a[:index-1] = l

print(a)
S = [0]
s = 0
for i in a:
    s += i
    S.append(s)
min_val = -10**18
index = -1

for i in range(n):
    sub_sum = S[n] - S[n-i-1]
    val = (i+1)*r
    print('s',sub_sum, val)
    if sub_sum - val > min_val:
        min_val = sub_sum - val
        index = n-i+1
    print('m',min_val)
print(min_val)
if min_val > 0:
    print(index)
    a[index-2:n] = r

print(a)
print(sum(a))

