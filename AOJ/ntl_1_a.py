n = int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

fac = factorization(n)
print(f'{n}:', end=' ')
for k, soinsu in enumerate(fac):
    for l in range(soinsu[1]):
        if k == len(fac) -1 :
            if l == soinsu[1] -1:
                print(soinsu[0])
            else:
                print(soinsu[0], end=' ')
        else:
            print(soinsu[0], end=' ')
