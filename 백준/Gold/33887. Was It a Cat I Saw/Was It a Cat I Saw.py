import sys

def mk_pal(depth,select):
    global rst
    if depth<=0:
        if depth==-1:
            rst.append("".join(select)+"".join(select)[:-1][::-1])
        else:
            rst.append("".join(select)+"".join(select)[::-1])
        return

    for i in ["0","1"]:
        select.append(i)
        mk_pal(depth-2,select)
        select.pop()
    return

def mk_candi(size, target):
    global rst
    rst=[] # 10^9 9글자
    select=["1"]
    if size>1:
        mk_pal(size-2,select)
    else:
        rst=select

    return rst

def solve():
    target=int(input())
    size=len(bin(target))-2
    candidate = mk_candi(size,target)

    answer=10e9
    for binary in candidate:
        answer=min(abs(int(binary,2)-target), answer)
    print(answer)

for _ in range(int(input())):
    solve()