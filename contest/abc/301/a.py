N = int(input())
S = input()
t = S.count('T')
a = N-t
print('AT'[t>a or t==a and S[-1] == 'A'])