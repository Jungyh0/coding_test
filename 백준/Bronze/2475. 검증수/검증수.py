import sys
import math
input = sys.stdin.readline

num = list(map(int, input().split()))
end_num = 0
for i in range(5):
    end_num += math.pow(num[i], 2)

print(int(end_num % 10))