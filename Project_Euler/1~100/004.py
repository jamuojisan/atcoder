mx = 0
for i in range(1,1001):
    for j in range(1, 1001):
        if list(str(i*j)) == list(str(i*j))[::-1]:
            mx = max(mx, i*j)
print(mx)