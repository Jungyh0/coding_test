import sys
from queue import PriorityQueue
input = sys.stdin.readline

num, sum = map (int, input().split())

card = list (map (int, input().split()))

sum_list = []
for i in range(num):
    for j in range(i + 1, num):
        one = card[i] + card[j]
        for k in range(j + 1, num):
            sample = card[k] + one
            if sample <= sum:
                sum_list.append(sample)
sum_list.sort()
print(sum_list[len(sum_list) - 1])