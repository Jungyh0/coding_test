import sys
input = sys.stdin.readline

n = list(map(int, input().split()))

check1 = True
check2 = True

for num in range(8):
    if (num + 1) != n[num]:
        check1 = False
        break
for num in range(7, -1, -1):
    if (num + 1) != n[7 - num]:
        check2 = False
        break

if not check1 and not check2:
    print("mixed")
elif check1:
    print("ascending")
elif check2:
    print("descending")
