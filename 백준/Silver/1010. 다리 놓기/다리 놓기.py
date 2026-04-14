tc  = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = 1
        for j in range(1, n + 1):  
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    print(dp[m][n])