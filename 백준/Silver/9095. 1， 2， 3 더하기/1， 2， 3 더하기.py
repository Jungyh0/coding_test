import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[m])