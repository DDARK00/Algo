n=int(input())
t = 1
f = 1
while t != 0:
    print(" "*(n-t)+"*"*t)
    t+=f
    if t>n:
        f = -1
        t -= 2