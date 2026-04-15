x=input()
m=0
t=0
for i,n in enumerate(x[:-1]):
    if n=='*':
        t=i%2
    else:
        m+=int(n)*(1+((i%2)*2))

l=int(x[-1])
for i in range(10):
    k=(m+(i*(1+(t*2))))+l
    if k%10==0:
        print(i)
        break