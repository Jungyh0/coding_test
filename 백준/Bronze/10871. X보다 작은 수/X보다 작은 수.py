import sys
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))

answer = ""

for i in range(n):
    if num[i] < m:
        answer += (str(num[i]) + " ")
print(answer)