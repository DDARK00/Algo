n = int(input())
l = [" "*i+"*"*(2*n-2*i-1) for i in range(n)]
l += list(reversed(l))[1:]
print(*l,sep='\n')