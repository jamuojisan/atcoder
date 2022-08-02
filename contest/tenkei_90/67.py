def Base_10_to_n(X, n):
    if (int(X//n)):
        return Base_10_to_n(int(X//n), n)+str(X%n)
    return str(X%n)


n, k = map(str, input().split())
if n == 0:
    print(0)
    exit()
table = str.maketrans('8', '5')
for _ in range(int(k)):
    n = int(n,8)
    n =  Base_10_to_n(n, 9)
    n = str(n)
    n = n.tnslate(table)
    

print(n)