n = int(input())

dp = list(-1 for _ in range(5001))

for i in range(0, 1661):
    for j in range(0, 1001):
        k = (3 * i) + (5 * j)
        if 3 <= k <= 5000:
            if dp[k] == -1:
                dp[k] = i + j
            else:
                dp[k] = min(dp[k], i + j)
print(dp[n])