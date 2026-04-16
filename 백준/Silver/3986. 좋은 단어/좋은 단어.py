import sys
input=sys.stdin.readline

ans=0
for _ in range(int(input())):
    s=input().rstrip()
    if len(s)%2:
        continue
    st=[]
    for c in s:
        if st and st[-1]==c:
            st.pop()
        else:
            st.append(c)
    if len(st)==0:
        ans+=1
print(ans)