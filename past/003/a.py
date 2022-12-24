s = input()
t = input()
S = s.upper()
T = t.upper()

if s == t:
    print('same')
elif S == T:
    print('case-insensitive')
else:
    print('different')
