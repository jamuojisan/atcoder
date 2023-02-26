import math
score = 1574

Q = sorted([score - 724.4744301*math.log(j, 2) for j in range(1, 101)], reverse=True)

bunsi = sum([Q[i-1]*(0.8271973364**(i)) for i in range(1,101)])
bunbo = sum([0.8271973364**(i) for i in range(1,101)])
r = bunsi/bunbo
print(bunsi, bunbo)
if r>= 400:
    print(r)
else:
    print(400/(math.exp((400-r)/400)))