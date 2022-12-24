import numpy as np
a, b, x = map(int,input().split())
print(180*np.arctan(2*(b - (x/(a**2)))/a)/np.pi)

print(180*np.arctan(b/(2*x/(a*b)))/np.pi)