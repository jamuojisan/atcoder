N = int(input())
ans = []
for i in range(N):
    _ans = [0]*(i+1)
    for j in range(i+1):
        if j == 0 or j == i:
            _ans[j] = 1
        else:
            _ans[j] = ans[-1][j-1] + ans[-1][j]
    ans.append(_ans)
for _ans in ans:
    print(*_ans)