import sys
input = sys.stdin.readline
n = int(input())
i = 1
idx = 0
num_list = []
stack = []
op = []

def top(stack):
    if len(stack) > 0:
        return stack[len(stack) - 1]

for _ in range(n):
    nn = int(input())
    num_list.append(nn)

stack.append(i)
op.append("+")

while idx < n:
    if top(stack) == num_list[idx]:
        stack.pop()
        op.append("-")
        idx += 1
    else:
        i += 1
        stack.append(i)
        op.append("+")

    if i > n:
        print("NO")
        break

if len(stack) == 0:
    for i in range(len(op)):
        print(op[i])

