import sys
input=sys.stdin.readline

n, k = map(int, input().split())
st1 = list(map(int, input().split()))
st2 = list(map(int, input().split()))

sum1 = sum(st1) # 3 1 4    8
sum2 = sum(st2) # 1 5 9    15

for i in range(k):
    tar1, tar2 = 0, 0
    if st1:
        tar1 = st1[-1] # 4
    if st2:
        tar2 = st2[-1] # 9
    tempsum1, tempsum2 = sum1-tar1, sum2-tar2
    # 4        6
    # print(tempsum1, tempsum2, tempsum1-sum2, sum1-tempsum2)
    # print(st1, st2,sum1,sum2)
    if max(tempsum1,sum2) >= max(sum1,tempsum2):
        # 11                      2
        sum2 = tempsum2
        st2.pop()
    else:
        sum1 = tempsum1
        st1.pop()
print(max(sum1,sum2))