import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

prize = [[0,0,0] for _ in range(n)]
# cnt, num, idx
no = 1
for num in map(int, input().split()):
    isfind = False

    for idx, val in enumerate(prize):
        if val[1] == num:
            isfind = True
            prize[idx][0]+=1
            break
    if not isfind:
        prize[n-1]=[1,num,no]
    no+=1
    prize.sort(key=lambda x: (-x[0],-x[2]))
    # print(prize)

ans = []
for cnt, num, idx in prize:
    if num==0:
        continue
    ans.append(num)
print(*sorted(ans))