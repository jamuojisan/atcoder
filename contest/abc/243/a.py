V, A, B , C = map(int, input().split())

while(1):
    for i, j in zip([A,B,C], ['F','M', 'T']):
        V -= i
        if V <0 :
            print(j)
            exit()
