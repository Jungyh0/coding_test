n, m = map(int, input().split())

arr = (sorted(list(map(int, input().split()))))
visited = [False] * n
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    num = 0

    for i in range(len(arr)):
        if num != arr[i] and not visited[i]:
            result.append(arr[i])
            num = arr[i]
            visited[i] = True
            dfs()
            visited[i] = False
            result.pop()

dfs()