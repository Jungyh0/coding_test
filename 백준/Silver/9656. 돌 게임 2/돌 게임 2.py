n = int(input())

name = ['SK', 'CY']

dp = list(False for _ in range(n + 1))

for i in range(2, n + 1):
    if not dp[i - 1]:
        dp[i] = True
    else:
        dp[i] = False
if dp[n]:
    print(name[0])
else:
    print(name[1])