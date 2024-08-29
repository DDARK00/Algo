import sys
from collections import deque
input = sys.stdin.readline

# 로봇이 들어올린 무게들의 합을 출력한다.

n, m = map(int,input().split())# 컨테이너 개수, 우선순위의 종류

# 필요 수, 현재 수
lst = deque([tuple(map(int,input().split())) for _ in range(n)]) # 우선순위, 무게
count = [[0,0] for _ in range(m+1)]
for p, w in lst:
    count[p][0]+=1
# 1에 가까울 수록 높은 우선순위를 가지고, M에 가까울 수록 낮은 우선순위
# 우선순위가 낮은 컨테이너를 먼저 적재한다.
# M개의 각 우선순위에 대하여 해당 우선순위를 갖는 컨테이너가 적어도 하나 존재한다.
# m -> 1
pointer = m
st =[]
cost = 0
while lst:
    p, w = lst.popleft()
    if pointer == p:
        if st and st[-1][0] == pointer:
            # 이미 있고 우선순위가 같으면ㅇ
            temp = []
            while st and st[-1][0] == pointer and st[-1][1] < w:
                pp, pw = st.pop()
                cost += pw
                temp.append((pp,pw))
            cost += w
            st.append((p,w))
            while temp:
                np, nw = temp.pop()
                cost += nw
                st.append((np, nw))

        else:
            # 없으면 
            cost+=w
            st.append((p,w))

        count[pointer][1] += 1
        if count[pointer][0] == count[pointer][1]:
            pointer-=1

    else:
        cost+=w
        lst.append((p,w))
print(cost)