n = int(input())

name = ['SK', 'CY']

dp = list(False for _ in range(n + 1))
dp[1] = True

for i in range(2, n + 1):
    if dp[i - 1]:
        dp[i] = False
    else:
        dp[i] = True
if dp[n]:
    print('SK')
else:
    print('CY')