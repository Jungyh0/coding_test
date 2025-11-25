n = int(input())

coast = []
for _ in range(n):
    sample = list(map(int, input().split()))
    coast.append(sample)

dp = [list([0, 0, 0]) for _ in range(n)]
dp[0] = coast[0]
for index in range(1, n):
    dp[index][0] = coast[index][0] + min(dp[index - 1][1], dp[index - 1][2])
    dp[index][1] = coast[index][1] + min(dp[index - 1][0], dp[index - 1][2])
    dp[index][2] = coast[index][2] + min(dp[index - 1][1], dp[index - 1][0])

print(min(dp[n - 1]))