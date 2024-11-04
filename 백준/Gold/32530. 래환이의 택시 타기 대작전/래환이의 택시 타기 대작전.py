import sys
input=sys.stdin.readline

ans = 0
st = []
n = int(input())
lst = []
for _ in range(n):
    hh, mm = map(int, input().rstrip().split(":"))
    hhmm = hh*60+mm
    if hhmm>=1440:
        hhmm = 1439
    lst.append(hhmm)

lst.sort()

for num in lst:
    if not st:
        ans+=1
        st.append(num)
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