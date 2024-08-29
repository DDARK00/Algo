import sys
n = int(input())

lst = list(map(int,input().split()))
lst = lst[::-1]
st = []
ans = []

for num in lst:
    if st and st[-1]<=num:
        while st and st[-1]<=num:
            st.pop()
        if st:
            ans.append(st[-1])
        else:
            ans.append(-1)
        st.append(num)
    else:
        if st:
            ans.append(st[-1])
        else:
            ans.append(-1)
        st.append(num)

print(*ans[::-1])