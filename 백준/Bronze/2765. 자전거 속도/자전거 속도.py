import sys
input = sys.stdin.readline

n = 1
while True:
    r, turn, time = map(float, input().split())
    if turn == 0:
        break
    #2 pi r
    pi = 3.1415927
    miles = pi*r*turn/12/5280
    print(f"Trip #{n}: {miles:.2f} {miles/time*3600:.2f}")
    n+=1