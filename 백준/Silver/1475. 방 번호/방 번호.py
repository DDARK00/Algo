s = input()
n0 = s.count('0')
n1 = s.count('1')
n2 = s.count('2')
n3 = s.count('3')
n4 = s.count('4')
n5 = s.count('5')
n6 = s.count('6')
n7 = s.count('7')
n8 = s.count('8')
n9 = s.count('9')
n6 = (n6 + n9) // 2 if (n6 + n9) % 2 == 0 else (n6 + n9) // 2 + 1

lst = [n0, n1, n2, n3, n4, n5, n6, n7, n8]
lst.sort()
print(lst[8])

# 이게 시간초과가 안 날까