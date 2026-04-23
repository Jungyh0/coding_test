n = int(input())

dice_num  = list(map(int, input().split()))

if n == 1:
    dice_num.sort()
    print(sum(dice_num[:5]))
else:
    min_num = []
    for i in range(3):
        min_num.append(min(dice_num[i], dice_num[5 - i]))

    min_num.sort()

    ver = sum(min_num) * 4
    cor = (min_num[0] + min_num[1]) * (8 *n - 12)
    face = min_num[0] * (n - 2) * (5 * n - 6)

    print(ver + cor + face)