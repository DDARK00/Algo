s: str = input()

zero_s = s.split('0')
one_s = s.split('1')
zero_s = list(filter(None, zero_s))
one_s = list(filter(None, one_s))

print(min(len(zero_s), len(one_s)))
