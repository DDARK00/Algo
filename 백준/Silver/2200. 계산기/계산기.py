import sys
input=sys.stdin.readline

answer=1
n=int(input())
lst=input().split()
for i in range(1, n):
    k=lst[i]
    if k!='0':
        answer+=len(k)+3 # +k*x
    else:
        answer+=2
    # print(answer)
# +k=
k=lst[-1]

if k=='0':
    answer+=1
else:
    answer +=len(k)+2
print(answer)
"""
1 2 3 4 5 0
x^5+2x^4+3x^3+4x^2+5x+0=
x(5+x(4+(x(3+x(2+x(1))))))
"""