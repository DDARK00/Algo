n = input()

start = 1

# 

while n:

    k = str(start)

    while k:

        if n.startswith(k[0]):

            n = n[1:]

        k = k[1:]

    start +=1

print(start-1)