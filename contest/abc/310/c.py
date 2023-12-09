N = int(input())
S = [input() for _ in range(N)]

group = set()
for s in S:
    if s in group or s[::-1] in group:
        continue
    else:
        group.add(s)

print(len(group))