a, b = input().split()

ar = [0]*max(len(a),len(b))
for i, c in enumerate(a[::-1]):
    ar[i]+=int(c)
for i, c in enumerate(b[::-1]):
    ar[i]+=int(c)
ar.reverse()
print(*ar, sep="")