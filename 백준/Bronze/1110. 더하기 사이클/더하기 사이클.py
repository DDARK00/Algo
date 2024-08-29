import sys
input = sys.stdin.readline

n = input().strip()
n = "0"+n if len(n) == 1 else n
def two(num):
    temp = "0"+num if len(num) == 1 else num
    r_one = temp[-1]
    temp = int(temp)%10+int(temp)//10
    r_two = str(temp)[-1]
    return str(int(r_one))+str(int(r_two))

copy = two(n)
cnt = 1
while copy !=n:
    cnt+=1
    copy = two(copy)
print(cnt)