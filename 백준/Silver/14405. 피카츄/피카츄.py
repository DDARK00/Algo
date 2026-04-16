import sys
input=sys.stdin.readline
s=input().strip()
s=s.split("pi")
s="피카츄".join(s)
s=s.split("ka")
s="피카츄".join(s)
s=s.split("chu")
s="피카츄".join(s)
s=s.split("피카츄")
s="".join(s)

if len(s)==0:
    print("YES")
else:
    print("NO")