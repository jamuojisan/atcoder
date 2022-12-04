N = int(input())

three = N//3
five = N //5
seven = N //7
tf = N//(3*5)
fs = N//(5*7)
ts = N//(3*7)
tfs = N//(3*5*7)

print(three + five + seven - tf - fs - ts + tfs)