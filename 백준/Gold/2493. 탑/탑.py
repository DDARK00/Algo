import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

answer = [0]*n
st = []

for idx, num in enumerate(lst):
    # 스택보다 작으면 넣고 크면 빼고
    # print('idx, num -->',idx,num)
    while st and st[-1][1]<=num:
        st.pop()

    if st:
        answer[idx] = st[-1][0]+1

    st.append((idx,num))
print(*answer)