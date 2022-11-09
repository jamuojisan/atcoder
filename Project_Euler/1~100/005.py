ans = [1]

for i in range(1,21):
    for j in ans:
        if (i % j) == 0:
            i //= j
    ans.append(i)

_ans = 1
for i in ans:
    _ans *= i
print(_ans)
        