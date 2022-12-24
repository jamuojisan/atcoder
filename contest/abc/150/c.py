import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))


for i, v in enumerate(itertools.permutations(list(range(1, n+1)), n)):
    if list(v) == p:
        x = i
    if list(v) == q:
        y = i
        
print(abs(x-y))
        