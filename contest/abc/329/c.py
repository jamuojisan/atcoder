N = int(input())
S = input()

moji = 'abcdefghijklmnopqrstuvwxyz'
from collections import defaultdict
count = defaultdict(int)
S = list(S)
ans = 0
for m in list(set(S)):
    count_list = []
    i = 0
    while(i < len(S)):
       if S[i] == m:
           count = 0
           while(i < len(S) and S[i] == m ):
               count += 1
               i+=1
           count_list.append(count)
       i += 1
    ans += max(count_list)
print(ans)