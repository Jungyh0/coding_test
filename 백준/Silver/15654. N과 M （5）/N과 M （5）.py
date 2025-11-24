n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

result = []

def dfs(start_index):
    if len(result) == m:
        print(*result)
        return
    for i in range(len(arr)):
        if not arr[i] in result:
            result.append(arr[i])
            dfs(i + 1)
            result.pop()  
dfs(0)