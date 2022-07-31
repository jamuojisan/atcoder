n = int(input())
moji_dict = {}
for _ in range(n):
    s = input()
    if s not in moji_dict:
        moji_dict[s]=1
        print(s)
    else:
        print(s + f'({moji_dict[s]})')
        moji_dict[s] +=1