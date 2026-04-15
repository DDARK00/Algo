import sys
input=sys.stdin.readline

def solve():
    sounds=input().split()

    s=input().rstrip()
    chk={}

    while s!="what does the fox say?" :
        s=s.split(" ")
        for i in range(2,len(s)):
            chk[s[i]]=1
        s=input().rstrip()

    for c in sounds:
        if chk.get(c):
            continue
        print(c,end=" ")
    print()

for _ in range(int(input())):
    solve()