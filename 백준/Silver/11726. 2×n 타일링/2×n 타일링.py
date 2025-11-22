dp = [0] * 1001

dp[1] = 1
dp[2] = 2

n = int(input())

for num in range(3, n + 1):
    dp[num] = (dp[num - 1] + dp[num - 2]) % 10007
 
print(dp[n])