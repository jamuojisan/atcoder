from collections import defaultdict
Q = int(input())
record = defaultdict(int)

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        record[q[1]] =int(q[2])
    else:
        print(record[q[1]])