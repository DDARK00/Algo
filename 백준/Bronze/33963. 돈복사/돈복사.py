n=input()
k=len(n)
n=int(n)
answer=-1
while 10**k>n:
    answer+=1
    n*=2
print(answer)
# HAPPY NEW YEAR~!