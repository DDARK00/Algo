s = input()
s=s.split('-')

answer = sum(map(int,s[0].split('+')))
for i in range(1,len(s)):
    line = sum(map(int,s[i].split('+')))
    answer-=line
print(answer)