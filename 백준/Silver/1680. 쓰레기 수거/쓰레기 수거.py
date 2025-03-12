import sys
input=sys.stdin.readline

for _ in range(int(input())):
    w, n = map(int, input().split()) # weight node
    ans = 0
    now_position = 0
    now_w = 0
    for _ in range(n):
        x_i, w_i = map(int, input().split())# dist weight
        ans += x_i - now_position
        now_position = x_i
        if now_w + w_i > w:
            ans += x_i*2
            now_w = w_i
        elif now_w + w_i ==w :
            now_position = 0
            now_w = 0
            ans+= x_i
        else:
            now_w+=w_i
    ans+=now_position
    print(ans)