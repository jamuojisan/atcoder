def is_cutting(val):
    length = 0
    count = 0
    
    for i in range(n):
        if i == 0:
            length += a[0]
        else:
            length += (a[i]-a[i-1])
        if length >= val:
            count +=1
            length = 0
        if count == k:
            if (l - a[i]) >=val:
                flag = True
            else:
                flag = False
            break
    
    if count < k:
        flag = False
    return flag

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
ok=0
ng = l
count = 0
while(ng -ok>1):
    mid = (ng +ok)//2
    if is_cutting(mid):
        ok = mid
    else:
        ng = mid

print(ok)