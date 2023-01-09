A, B, C, D = map(str,input().split())
a = A.zfill(2) + B.zfill(2) + '00'
b = C.zfill(2) + D.zfill(2) + '01'
if a < b:
    print('Takahashi')
else:
    print('Aoki')
