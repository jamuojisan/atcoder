x1, x2, x3, x4, x5 = map(int,input().split())

for i in range(5):
    if [x1, x2, x3, x4, x5][i] != i+1:
        print(i+1)