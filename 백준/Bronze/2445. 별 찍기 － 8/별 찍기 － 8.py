n=int(input())
l=["*"*i+" "*(2*n-2*i)+"*"*i for i in range(1,n)]
l and print(*l,sep="\n")
print("*"*2*n)
l and print(*reversed(l),sep="\n")