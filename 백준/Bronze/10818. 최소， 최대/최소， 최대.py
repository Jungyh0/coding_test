import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
min = num[0]
max = num[0]

for i in range(n):
    if max < num[i]:
        max = num[i]
    if min > num[i]:
        min = num[i]

print(min,max)