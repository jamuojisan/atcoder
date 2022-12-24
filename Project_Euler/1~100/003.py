target = 600851475143

def factrization(n):
    a = []
    
    while(n % 2 == 0):
        a.append(2)
        n //=2
    
    f = 3

    while(f*f <= n):
        if (n % f) == 0:
            a.append(f)
            n //= f
        f +=2
        
    if n != 1:
        a.append(n)
    
    return sorted(a)

print(factrization(target)[-1])