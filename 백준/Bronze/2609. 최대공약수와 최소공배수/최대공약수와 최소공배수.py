import sys
from queue import PriorityQueue
input = sys.stdin.readline

num = list(map(int, input().split()))

num.sort()

max = 0
min = num[0] * num[1]

def gcd(num1, num2):
    while num2 > 0:
        num1 , num2 = num2, num1 % num2
    return num1

max = gcd(num[1],num[0])
min /= max
    
print(max)
print(int(min))