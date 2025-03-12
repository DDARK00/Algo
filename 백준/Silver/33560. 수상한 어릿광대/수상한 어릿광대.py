import sys
input=sys.stdin.readline

n=int(input())

score = 0
time = 0
add_score = 1
add_time = 4
r1, r2, r3, r4 = 0, 0, 0, 0

def end_game():
    global add_score, add_time, score, time, r1, r2, r3, r4
    if score>=125:
        r4+=1
    elif score>=95:
        r3+=1
    elif score>=65:
        r2+=1
    elif score>=35:
        r1+=1
    score = 0
    time = 0
    add_score = 1
    add_time = 4

def get_score():
    global score, time
    time+=add_time
    score+=add_score

for temp in input().split():
    # print(add_score, add_time, score, time, temp)
    if time>240:
         end_game()

    if temp == "1":
        # get_score()
        end_game()
        continue
    elif temp == "2":
        if add_score == 1:
            add_time+=2
        else:
            add_score >>= 1
    elif temp == "3":
        "지문이모호해"
    elif temp == "4":
        time += 56
    elif temp == "5":
        if add_time >1:
            add_time-=1
    else:
        if add_score<32:
            add_score <<=1
    get_score()
print(r1)
print(r2)
print(r3)
print(r4)