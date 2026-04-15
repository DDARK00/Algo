import sys
from collections import defaultdict
input=sys.stdin.readline

is_prime=defaultdict(lambda :1)
primes=[1]
for i in range(2,10001):
    if not is_prime[i]:
        continue
    primes.append(i)
    for j in range(i+i,10001,i):
        is_prime[j]=0

for _ in range(int(input())):
    k=int(input())
    idx=0
    a=0
    while idx<len(primes):
        if primes[idx]>(k//2):
            break
        if is_prime[k-primes[idx]]:
            a=idx
        idx+=1
    print(primes[a],k-primes[a])
