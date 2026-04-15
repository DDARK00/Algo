import sys
input=sys.stdin.readline

n=int(input())
head,tail=input().rstrip().split("*")

for _ in range(n):
    s=input().rstrip()
    if s.startswith(head):
        a,*b=s.split(head,1)
        if b and b[0].endswith(tail):
            print("DA")
            continue
    print("NE")