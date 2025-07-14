import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    q = []
    str_list = list(map(str, input().strip()))
    check = True
    for c in str_list:
        if c == '(':
            q.append(0)
        else:
            if len(q) == 0:
                check = False
                break
            else:
                q.pop()
    if check and len(q) == 0:
        print("YES")
    else:
        print("NO")