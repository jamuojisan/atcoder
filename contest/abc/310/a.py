N, P , Q = map(int , input().split())
D = [*map(int ,input().split())]
print(min(D)+Q if min(D) + Q < P else P)