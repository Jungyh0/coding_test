import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

dp = [list(0 for _ in range(n))for _ in range(n)]

m = int(input())

for lenth in range(n):
    for start in range( n - lenth):
        end = start + lenth
        if start == end:
            dp[start][end] = 1
        elif num[start] == num[end]:
            if (start + 1) == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])