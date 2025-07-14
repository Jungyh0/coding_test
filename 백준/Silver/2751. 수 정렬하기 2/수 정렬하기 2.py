import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())

str = list(int(input().strip()) for _ in range(n))

str = list(set(str))
str.sort()

for i in str:
    print(i)