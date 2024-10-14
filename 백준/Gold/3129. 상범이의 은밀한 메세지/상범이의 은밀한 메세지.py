import sys
input=sys.stdin.readline

s = input().rstrip() # pass
cs = input().rstrip() # origin

target = ""
for k in range(len(s)-len(cs)+1):
    key = ""
    for i in range(len(cs)):
        s_word = ord(s[i+k])
        cs_word = ord(cs[i])
        a = chr((26+cs_word-s_word)%26+97)
        key+=a

    start = len(key)//2
    find = False
    for q in range(start, 0, -1):
        t = key[:q]
        tail = key[q:]
        cnt = 1
        while len(tail)>=q:
            head = tail[:q]
            if head == t:
                tail = tail[q:]
                cnt+=1
                continue
            else:
                break
        if cnt >= (len(key)//q):
            target = t
            find = True
            break
    if find:
        break

k = q - k%q
target = target[k:] + target[:k]

for idx, c in enumerate(s):
    key_c = target[idx%len(target)]
    ans = (26+ord(key_c)-97+ord(c)-97)%26
    print(chr(97+ans), end="")

# 브루트포스쪽이 좀 찝찝한데;