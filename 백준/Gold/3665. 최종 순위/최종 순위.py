import sys
from collections import defaultdict
input=sys.stdin.readline
# 1sec tc 100 n 500

for _ in range(int(input())):
    n = int(input()) # team count
    
    graph = defaultdict(list)
    degree = [0] * (n+1)
    last = list(map(int, input().split())) # grade

    for i in range(n):
        for j in range(i+1, n):
            graph[last[i]].append(last[j])
            degree[last[j]] += 1
    m = int(input())  # this year

    for _ in range(m):
        a, b = map(int, input().split()) # change team
        if b in graph[a]:
            graph[a].remove(b)
            graph[b].append(a)
            degree[a]+=1
            degree[b]-=1
        else:
            graph[b].remove(a)
            graph[a].append(b)
            degree[b]+=1
            degree[a]-=1
    # print(degree, graph)
    is_IMPOSSIBLE = [0]*(n+1)
    # 1 ~ N, ?, IMPOSSIBLE

    st = []
    flag=True
    for i in range(1, n+1):
        if is_IMPOSSIBLE[degree[i]] == 0:
            is_IMPOSSIBLE[degree[i]] = 1
        else:
            print("IMPOSSIBLE")
            flag=False
            break
        if degree[i] == 0:
            st.append(i)
    if flag:

        while st:
            v = st.pop()
            print(v, end=" ")
            for num in graph[v]:
                degree[num] -=1
                if degree[num] == 0 :
                    st.append(num)
        print()