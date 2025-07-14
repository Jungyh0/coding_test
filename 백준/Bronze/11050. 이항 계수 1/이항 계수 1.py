import sys
import math
from queue import PriorityQueue
input = sys.stdin.readline

n, k = map(int, input().split())

print(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))