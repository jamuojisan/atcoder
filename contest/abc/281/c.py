N, T = map(int, input().split())
A = [*map(int, input().split())]
S = [0]
for i in A:
    S.append(S[-1] + i)

T %= S[-1]
import bisect

index = bisect.bisect(S, T)
if index == 0:
    print(index+1, T)
elif index == len(S)-1:
    print(index, T - S[index-1])
else:
    print(index, T - S[index-1])


