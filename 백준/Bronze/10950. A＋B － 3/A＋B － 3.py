import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num1, num2 = map(int, input().split())
    print (num1 + num2)