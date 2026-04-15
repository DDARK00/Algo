"""
11 11 11 2 2 2
111 11 1 3 2 1
1111 11 11 4 2 2
11111 11 1 5 2 1
111111 11 11 6 2 2
"""
import sys;input=sys.stdin.readline
from math import gcd
a, b = map(int, input().split())
print("1"*gcd(a,b))