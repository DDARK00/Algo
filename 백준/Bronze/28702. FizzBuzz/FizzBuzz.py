import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

if a.isnumeric():
    i = int(a)+3
elif b.isnumeric():
    i = int(b)+2
else:
    i = int(c)+1
ans = ""
if i%3 == 0:
    ans += "Fizz"
if i%5 == 0:
    ans += "Buzz"
if ans == "":
    ans = i
print(ans)