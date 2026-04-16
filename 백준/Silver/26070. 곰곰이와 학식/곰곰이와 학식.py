a,b,c=map(int,input().split()) # want
x,y,z=map(int,input().split()) # have

ans=0
ans+=min(a,x)
ans+=min(b,y)
ans+=min(c,z)
a,x=max(0,a-x),max(0,x-a)
b,y=max(0,b-y),max(0,y-b)
c,z=max(0,c-z),max(0,z-c)

# x->y->z->x
# 0 1 2 3 0
# 다 주고 남는다->교환해도 된다
idx=max((x,0),(y,1),(z,2))[1]
item=[(x,a),(y,b),(z,c)]
tmp=0
for i in range(3):
    t=(idx+i)%3
    have,want=item[t]
    have+=tmp
    k=min(have,want)
    ans+=k
    tmp=(have-k)//3
print(ans)