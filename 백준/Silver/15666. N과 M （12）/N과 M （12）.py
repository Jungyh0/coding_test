n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

ans = []
def dfs(start):
    
    last_num = 0

    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n):
        if not arr[i] == last_num:
            last_num = arr[i]
            ans.append(arr[i])
            dfs(i)
            ans.pop()

dfs(0)