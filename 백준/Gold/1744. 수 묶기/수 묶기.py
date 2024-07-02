import sys
input = sys.stdin.readline

n = int(input())
minus = []
plus = []
zero = 0

ans = 0

for _ in range(n):
    k = int(input())

    if k>0:
        if k == 1:
            ans+=1

        else:
            plus.append(k)

    elif k == 0:
        zero+=1

    else:
        minus.append(k)

minus.sort(key=lambda x:x)
plus.sort(key=lambda x:-x)

m_half = len(minus)//2

if m_half>0:
    for i in range(m_half):
        ans+=minus[2*i]*minus[2*i+1]

if len(minus)%2 == 1 and zero == 0:
    ans+=minus[-1]

p_half = len(plus)//2

if p_half>0:
    for i in range(p_half):
        ans+= plus[2*i]*plus[2*i+1]

if len(plus)%2 == 1:
    ans+= plus[-1]

print(ans)