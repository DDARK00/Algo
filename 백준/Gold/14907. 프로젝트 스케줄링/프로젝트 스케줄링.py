import sys
input=sys.stdin.readline

s=input().rstrip()
deg=[0]*26
answer=[0]*26 # 1000*26
timer=[0]*26
g=[[]for _ in range(26)]

st=[]
while s!='':
    v, c, *k=s.split()
    v=ord(v)-ord('A')
    c=int(c)
    # timer[v]=c
    if k:
        timer[v]=c
        deg[v]=len(*k)
        for i in list(*k):
            j=ord(i)-ord('A')
            g[j].append(v)
    else:
        answer[v]=c
        st.append(v)
    s=input().rstrip()


while st:
    v=st.pop()
    for k in g[v]:
        answer[k]=max(answer[k],answer[v]+timer[k])
        deg[k]-=1
        if deg[k]==0:
            st.append(k)

print(max(answer))