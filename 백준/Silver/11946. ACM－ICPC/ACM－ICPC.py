import sys
from collections import defaultdict
input=sys.stdin.readline

n,m,q=map(int,input().split())
# 팀 문제 쿼리
question_pass={i:defaultdict(int) for i in range(n)}
answer=[[0,0,i] for i in range(n)] # 문제수 시간 팀번호
for _ in range(q):
    time, team, q_no, wa = input().split()
    team=int(team)-1
    q_no=int(q_no)
    # -1 정답 0... 시도횟수
    if question_pass[team][q_no]==-1:
        continue
    if wa!="AC":
        question_pass[team][q_no]+=1
    else:
        answer[team][0]+=1
        answer[team][1]+=int(time)+20*question_pass[team][q_no]
        question_pass[team][q_no]=-1
answer.sort(key=lambda x:(-x[0],x[1],x[2]))
for solved, times, idx in answer:
    print(idx+1,solved,times)