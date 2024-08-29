import sys

input = sys.stdin.readline

s = input().rstrip()

#  이모지의전체길이 + 콜론의개수 + 언더바의개수 *5

i = 0

for c in s :

    if c == ":" :

        i+= 2

    elif c == "_" :

        i+= 6

    else :

        i+=1

print (i)