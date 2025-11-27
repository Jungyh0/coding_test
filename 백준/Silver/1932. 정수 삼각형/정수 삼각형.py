n = int(input())

graph = []
for _ in range(n):
    sample = list(map(int, input().split()))   
    graph.append(sample)

dp = list([0] * n for _ in range(n))
dp[0][0] = graph[0][0]

for i in range(1, n):
    for j in range(len(graph[i])):
        if j == 0:
            dp[i][j] = graph[i][j] + dp[i - 1][j]
        elif j == (len(graph[i]) - 1):
            dp[i][j] = graph[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = graph[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[len(dp) - 1]))