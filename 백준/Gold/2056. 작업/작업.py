import sys
input=sys.stdin.readline

n = int(input())

before = [0]*(n+1)
time = [0]*(n+1)

lst = [[] for _ in range(n+1)]
cnt = [0]*(n+1)
for  i in range(n):
    idx = i+1
    t, c, *a = map(int, input().split())
    time[idx] = t
    for num in a:
        cnt[idx]+=1
        lst[num].append(idx)

st = []
for i in range(1, n+1):
    if cnt[i] == 0:
        st.append(i)
        cnt[i] = -1
        time[i] += before[i]

    while st:
        v = st.pop()
        for num in lst[v]:
            before[num]= max(before[num], time[v])
            cnt[num]-=1
            if cnt[num] == 0:
                st.append(num)
                cnt[num] = -1
                time[num]+=before[num]
print(max(time))