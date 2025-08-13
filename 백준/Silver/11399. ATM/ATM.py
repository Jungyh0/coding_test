import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0

for rge in range(len(time), -1, -1):
    for index in range(rge):
        result += time[index]

print(result)