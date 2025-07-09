import sys
from queue import PriorityQueue
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    list_num = list(map(int, str(n).strip()))
    st = 0
    ed = len(list_num) - 1
    pal = True
    while st < ed:
        if list_num[st] != list_num[ed]:
            print("no")
            pal = False
            break
        else:
            st += 1
            ed -= 1
    if pal:
        print("yes")