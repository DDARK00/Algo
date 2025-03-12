import sys
input=sys.stdin.readline
ans = 0
st = []
n = int(input())
lst = [0]*n
for i in range(n):
    hh,mm = map(int, input().rstrip().split(":"))
    hm = hh*60+mm
    if hm>=1440:
        hm = 1439
    lst[i] = hm

lst.sort()

for num in lst:
    if not st:
        ans+=1
        st = [num]
    else:
        s = st[0] + 10
        e = num - 10

        if s<e:
            ans+=1
            st = [num]
        elif len(st) == 2:
            st = []
        else:
            st.append(num)
print(ans)