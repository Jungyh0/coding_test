import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())

str = list(input().strip() for _ in range(n))

str = list(set(str))
str.sort()
str.sort(key = len)

for i in str:
    print(i)