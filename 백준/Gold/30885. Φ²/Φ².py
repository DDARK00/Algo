import sys

input=sys.stdin.readline

size = int(input())

lst = list(map(int,input().split()))

# 초기 데이터

# 개념만 보고 수제작성!

link=[{'before':i-1, 'now':i,'next':i+1} for i in range(size)] # before after now idxㅇ

link[0]['before'],link[-1]['next'] = None, None

start = 0 # start idx

def run(start):

    current = start

    while current != None:

        now = link[current]

        

        before = now['before']

        nxt = now['next']

        target = now['now'] # 현재 인덱스

        now_val = lst[target] # 동시에 먹는다

        if before != None and lst[before] <= now_val:

            lst[target]+=lst[before]

            if link[before]['before'] != None:

                link[link[before]['before']]['next'] = target

                link[target]['before'] = link[link[before]['before']]['now']

            else:

                # 없으면 이게 맨 앞

                link[target]['before'] = None

                start = target

        if nxt != None and lst[nxt]<=now_val:

            lst[target]+=lst[nxt]

            link[current]['next'] = link[nxt]['next']

            if link[nxt]['next'] != None:

                link[link[nxt]['next']]['before'] = target

            

        current = link[current]['next']

    return start

while link[start]['next']!= None:

    start = run(start)

print(lst[start])

print(start+1)