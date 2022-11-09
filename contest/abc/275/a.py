import numpy as np
n = int(input())
h = np.array(list(map(int, input().split())))
ans = np.argmax(h)
print(ans + 1)


