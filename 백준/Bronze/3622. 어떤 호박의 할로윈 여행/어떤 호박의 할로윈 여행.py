import sys

from collections import deque

input=sys.stdin.readline

A,a,B,b,P = map(int,input().split())

# 대문자가 밖

if P>= max(A,B) and max(a,b)>=min(A,B):

    print("Yes")

else:

    if A+B<=P:

        print("Yes")

    else:

        print("No")