import sys
input = sys.stdin.readline

speak = []
bingo = [list(map(int, input().split())) for _ in range(5)]
for _ in range(5):
    speak += list(map(int, input().split()))

def check_cul():
    result = 0
    for i in range (5):
        if all(bingo[j][i] == 0 for j in range(5)):
            result += 1
    return result

def check_raw():
    result = 0
    for i in range(5):
        if all(bingo[i][j] == 0 for j in range(5)):
            result += 1
    return result

def check_dal():
    result = 0
    if all (bingo[i][i] == 0 for i in range(5)):
        result += 1
    if all (bingo[i][4 - i] == 0 for i in range (5)):
        result += 1
    return result

for i in range(25):
    found_number = False
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                found_number = True
                break
        if found_number:
            break

    total_bingo_count = check_cul() + check_raw() + check_dal()

    if total_bingo_count >= 3:
        print(i + 1)
        break
