import sys
input=sys.stdin.readline

# 모든 수는 결국 사이클을 이룰 것이라는 가정
# 증명 어케함?
# 1->1, 2->4->16->37->58->89->145->42->20->4...
# 3->9->81->65->61->37
# 5 6 7 8 9
# 81 64 5 25 4 16
# 자릿수의 수는 결국0~9->0~81 제곱
# 81+81+81+81 = 324
# 4자리 이상의 수는 반드시 그보다 작게 수렴함
# 반대로 말하면 모든 수는 최종적으로 닫힌 공간에서만 수열을 이룸
# 즉 가능한 수열의 범위<수의 범위
# 비둘기집?

def nxt_num(p):
    q=0
    while p>0:
        q += (p%10)**2
        p//=10
    return q

def solve(a,b):
    chk_a={}
    chk_b={}

    chk_a[a]=1
    while True:
        nxt_a=nxt_num(a)
        if chk_a.get(nxt_a):
            break
        chk_a[nxt_a]=chk_a[a]+1
        a=nxt_a

    chk_b[b]=1
    answer=1e9
    while True: # 앞에서부터
        if chk_a.get(b):
            answer=min(chk_a[b]+chk_b[b],answer)
        nxt_b=nxt_num(b)
        if chk_b.get(nxt_b):
            break
        chk_b[nxt_b]=chk_b[b]+1
        b=nxt_b

    return 0 if answer==1e9 else answer
        
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    k=solve(a,b)
    print(a,b,k)