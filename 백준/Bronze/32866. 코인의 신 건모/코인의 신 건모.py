
a = int(input())
b = int(input())
# 저는 바보입니다... 퍼센트였어...
ans = ((a / (a*((100-b)/100)) - 1)*100)
print(f'{ans:6f}')