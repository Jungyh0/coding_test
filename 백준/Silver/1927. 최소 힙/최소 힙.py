import sys
input = sys.stdin.readline
import heapq

que = []
n = int(input())

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(que, num)
    else:
        if not que:
            print(0)
        else:
            print(heapq.heappop(que))