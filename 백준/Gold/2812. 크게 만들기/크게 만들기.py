import sys
input=sys.stdin.readline

n,k=map(int,input().split())
st=[]
s=input().rstrip()
st.append(int(s[0]))
for i in range(1, n):
    m=int(s[i])
    while k>0 and st and st[-1]<m:
        st.pop()
        k-=1
    st.append(m)
while k>0:
    st.pop()
    k-=1
print(*st,sep="")