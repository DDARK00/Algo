import sys
input=sys.stdin.readline

input()
s=input().rstrip()
if s[0]=="A" and s[-1]=="B":
    print("Yes")
else:
    print("No")