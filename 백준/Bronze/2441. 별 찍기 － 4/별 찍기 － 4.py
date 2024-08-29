n = int(input())
for i in range(n):
    ans=""
    ans+= " "*i
    ans+= "*"*(n-i)
    print(ans)