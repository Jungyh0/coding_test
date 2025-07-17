import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

num_counts = Counter(num)

m = int(input())
check = list(map(int, input().split()))

result = []
for find_num in check:
    result.append(num_counts[find_num])

print(*result)