obj = {}

for i in range(1,10000):

    a = i

    while i>0:

        a+= i%10

        i//=10

    obj[a] = 1

for i in range(1,10001):

    if not obj.get(i):

        print(i)