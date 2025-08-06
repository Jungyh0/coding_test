import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
answer = []
num_list = list(num for num in range(1, n + 1))
num_list = deque(num_list)

for _ in range(n):
    for i in range(m - 1):
        num_list.rotate(-1)
    answer.append(num_list.popleft())

print(f"<{', '.join(map(str, answer))}>")