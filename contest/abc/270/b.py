X, Y, Z =map(int, input().split())

if X == 0:
    print(0)
elif X > 0:
    if Y <= 0:
        print(X)
    else:
        if X < Y:
            print(X)
        else:
            if Z > 0 and Z < Y <X:
                print(X)
            elif Z< 0 and Z<Y<X:
                print(X-Z*2)
            else:
                print(-1)
else:
    if Y > 0:
        print(-X)
    else:
        if X > Y:
            print(-X)
        else:
            if Z > 0 and Z > Y >X:
                print(2*Z-X)
            elif Z< 0 and Z>Y>X:
                print(-X)
            else:
                print(-1)
            
    