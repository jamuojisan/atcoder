S = input()

if S[0] == '1':
    print('No')
    exit()
kumiawase = [[6],[3], [1,7],[0,4],[2,8],[5],[9]]
f = False
beated_index = []
for i, kumi in enumerate(kumiawase):
    f = True
    for j in kumi:
        if S[j]  == '1':
            f = False
    if f:
        beated_index.append(i)
if len(beated_index) == 0:
    print('No')
    exit()
attempt = {0, 6}
if attempt | set(beated_index) == {0, 6}:
    print('No')
    exit()

all_bar = {0, 1,2,3,4,5,6}
tatteirubar = all_bar - set(beated_index)


for beated in beated_index:
    if beated == 0 or beated==6:
        continue
    low_f = False
    up_f = False
    for tatteiru in tatteirubar:
        if beated > tatteiru:
            low_f = True
        if beated < tatteiru:
            up_f = True
    if low_f and up_f:
        print('Yes')
        exit()
    else:
        print('No') 
        exit()


            
        

