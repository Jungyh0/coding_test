import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())

men = []

for i in range(n):
    age, name = map(str, input().split())
    men.append((int(age), i, name))

men.sort()
for age, i, name in men:
    print(age, name)