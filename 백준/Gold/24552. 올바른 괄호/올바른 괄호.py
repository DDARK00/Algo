s=input()
cnt=[0,0]
chk={'(':0,')':1}
for c in s:
    cnt[chk[c]]+=1

if cnt[0]<cnt[1]:
    s=s[::-1]
    t='('
else:
    t=')'

answer=0
cnt=[0,0]
for c in s:
    if c==t:
        cnt[1]+=1
        if cnt[0]==cnt[1]:
            cnt=[0,0]
            answer=0
    else:
        cnt[0]+=1
        answer+=1
print(answer)