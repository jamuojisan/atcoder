a = sorted(list(map(int, input().split())))

if ((a[0] == a[1] and a[1] == a[2]) and (a[-1] == a[-2])) or ((a[0] == a[1]) and ( a[2] == a[3] and a[-1] == a[-2])):
    print('Yes')
else:
    print('No')
