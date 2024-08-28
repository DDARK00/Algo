import sys
input = sys.stdin.readline

lst = list(input().rstrip())

n=int(input())

st = []

for _ in range(n):
    a = input().rstrip()
    # print(lst)
    if a[0] == "P":
        lst.append(a[2])
    elif a[0] == "B":
        if lst:
            lst.pop()
    elif a[0] == "L":
        if lst:
            st.append(lst.pop())
    else: # D
        if st:
            lst.append(st.pop())
print(*lst, sep="",end="")
st.reverse()
print(*st,sep="")