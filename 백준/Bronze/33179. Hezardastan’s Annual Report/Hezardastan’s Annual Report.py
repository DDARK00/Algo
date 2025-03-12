ans = 0
input()
for num in input().split():
    ans+= int(num)//2
    ans+= int(num)%2
print(ans)