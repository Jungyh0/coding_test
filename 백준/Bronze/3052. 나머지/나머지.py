import sys
input = sys.stdin.readline

list = []
for _ in range(10):
    n = int(input())
    if not (n % 42) in list:
        list.append(n % 42)
print(len(list))
