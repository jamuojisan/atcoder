n = int(input())
a = list(map(int, input().split()))

def binary_search(val):
    lis = set(a)
    lis = {i for i in lis if i <=val}
    sell_book = (n - len(lis))//2
    count = 0
    for i in range(1,val+1):
        if i not in lis:
            count+=1
    if count <= sell_book:
        return True
    else:
        return False





ok = 0
ng = 3*(10**5)+1

while(ng-ok > 1):
    mid = (ok+ng)//2
    if binary_search(mid):
        ok = mid
    else:
        ng = mid
print(ok)

