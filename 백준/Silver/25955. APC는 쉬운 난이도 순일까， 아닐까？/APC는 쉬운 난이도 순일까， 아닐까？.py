import sys
input=sys.stdin.readline

n=int(input())

lst=input().split()
# 쉬운순
order={"B":1,"S":2,"G":3,"P":4,"D":5}
ok=sorted(lst,key=lambda x:(order[x[0]],-int(x[1:])))
for i in range(n):
    if lst[i] != ok[i]:
        print(f'KO\n{ok[i]} {lst[i]}')
        exit()
print("OK")