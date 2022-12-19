N, M, X, T, D = map(int,input().split())

# M歳のときの身長をもとめる
# Aさんは、身長が毎年Dセンチずつのびる
# N(>M)歳の時の身長はTcm
# AさんはX歳で身長が止まる
zero = T - X*D
if M >= X:
    print(T)
else:
    print(zero + D*M)