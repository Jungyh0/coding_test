import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())

men = []

for i in range(n):
    x, y = map(int, input().split())
    men.append((x, y))

men.sort()
for x, y in men:
    print(x, y)