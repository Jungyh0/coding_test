import sys
import bisect
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
LIS = [*map(int, input().split())]

A = [LIS[0]]

for i in LIS:
    if A[-1] < i:
        A.append(i)
    else:
        idx = bisect_left(A,i)
        A[idx] = i

print(len(A))
