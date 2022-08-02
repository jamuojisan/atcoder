n = int(input())

a =  n % 4
if a == 2:
    print(n)
elif a == 3:
    print(n+3)
elif a == 0:
    print(n+2)
else:
    print(n+1) 
