import sys
input=sys.stdin.readline

m, n = map(int, input().split())

ans = [""]*(n-m)+list(input().rstrip())
whole = list(input().rstrip())

origin = list(whole)
for i in range(n-m):
    bi = ord(whole[-i-1])-97
    ai = ord(ans[-i-1])-97
    ki = (26+bi-ai)%26
    ans[-m-i-1] = chr(ki+97)
print("".join(ans))