n = list(input())
if '0' not in n:
    print(-1)

else:
    n = list(map(int, n))
    if sum(n) % 3 == 0:
        n.sort(key=lambda x: -x)
        print(*n,sep="")
    else:
        print(-1)
