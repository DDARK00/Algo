import sys
input=sys.stdin.readline

n=int(input())

for _ in range(n):
    s=input().rstrip()
    add=0
    for idx, num in enumerate(map(int,s)):
        if idx%2==0:
            num*=2
            if num>9:
                num=num//10+num%10
        add+=num
    if add%10==0:
        print("T")
    else:
        print("F")