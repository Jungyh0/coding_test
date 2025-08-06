import sys
input = sys.stdin.readline

n = int(input())
S = []
all_list = list(i for i in range(1, 21))

def list_add(num):
    if not num in S:
        S.append(num)

def list_remove(num):
    if num in S:
        S.remove(num)

def check(num):
    if num in S:
        print(1)
    else:
        print(0)

def toggle(num):
    if num in S:
        S.remove(num)
    else:
        S.append(num)

def listr_all():
    global S
    S = all_list.copy()

def list_empty():
    S.clear()

for _ in range(n):
    user_input = input().split()
    input_str = user_input[0]

    if input_str in ["add", "remove", "check", "toggle"]:
        input_num = int(user_input[1])

    if input_str == "add":
        list_add(input_num)
    elif input_str == "remove":
        list_remove(input_num)
    elif input_str == "check":
        check(input_num)
    elif input_str == "toggle":
        toggle(input_num)
    elif input_str == "all":
        listr_all()
    elif input_str == "empty":
        list_empty()